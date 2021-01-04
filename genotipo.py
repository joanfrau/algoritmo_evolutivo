import random
import copy
import matplotlib.pyplot as plt
import matplotlib.colors

class genotipo():

    def __init__(self, inputs: dict):

        self.inputs = inputs
        self.cod = self.generar_genotipo()
        # self.plot_genotipo()
        self.fitness = self.calcular_fitness() #TODO: hay que escribir está función, y una vez escrita el fitness será un atributo de cada genotipo que se calcula al inicializar el genotipo

    def generar_genotipo(self):
        '''
        Función que inicializa el genotipo definiendo la matriz genotipo.cod (m x t),
        donde el elemento ij representa la asignatura asignada a la clase i en la franja j.
        :return:
        '''
        n_clases = len(self.inputs['clases']) # numero clases
        n_franjas = len(self.inputs['franjas']) # numero horas lectivas
        cod = [[0]*n_franjas for _ in range(n_clases)] # Inicializamos matriz del genotipo
        f_disp_clases = [[i for i in range(n_franjas)] for _ in range(n_clases)] # Franjas que quedan sin asignar a cada clase
        HCA_disp = copy.deepcopy(self.inputs['HCA']) # Se usa para ir restando horas a medida que se asignan
        h_pend_clases = [sum(horas) for horas in HCA_disp]
        while sum(h_pend_clases) > 0:
            for clase in range(n_clases):
                for asign in range(len(self.inputs['asignaturas'])):
                    if HCA_disp[clase][asign] != 0:
                        franja = random.choice(f_disp_clases[clase]) # Se escoge franja random entre las que quedan sin asignar
                        cod[clase][franja] = asign + 1 # Se asigna la asignatura a esa franja
                        f_disp_clases[clase].remove(franja)
                        HCA_disp[clase][asign] += -1
            h_pend_clases = [sum(horas) for horas in HCA_disp] # Horas que quedan por asignar a cada clase
        return cod

    def calcular_fitness(self):
        '''
        Calcular fitness del genotipo
        :return:
        '''
        # TODO: completar
        pass

    def plot_genotipo(self):
        dias = ['L', 'M', 'X', 'J', 'V']
        n_clases = len(self.inputs['clases'])
        fig = plt.figure(figsize=(25, 13))
        colors = plt.cm.tab20.colors

        for c in range(1,n_clases + 1):
            ax = fig.add_subplot(round(n_clases/2.0), round(n_clases/2.0), c)
            ax.yaxis.grid()
            ax.set_xlim(0.5, len(dias) + 0.5)
            ax.set_ylim(14.1, 7.9)
            ax.set_xticks(range(1, len(dias) + 1))
            ax.set_xticklabels(dias)
            ax.set_ylabel('Hora')
            clase_label = self.inputs['clases'][c - 1]
            horas_acum = 0
            for ndia in range(len(dias)):
                horas_en_dia = sum(dias[ndia] in f for f in self.inputs['franjas'])
                asignaturas_en_dia = self.cod[c - 1][horas_acum:horas_en_dia + horas_acum]
                for franja, asign in enumerate(asignaturas_en_dia):
                    if asign != 0:
                        ax.fill_between([ndia + 0.5, ndia + 1.46], [franja + 8, franja + 8], [franja + 9, franja + 9],
                                         color=colors[asign], edgecolor='k',linewidth=0.5)
                        asign_label = self.inputs['asignaturas'][asign - 1]
                        ax.text(ndia + 1.00, franja + 8.5, asign_label, ha='center', va='center', fontsize=12)

                horas_acum += horas_en_dia

            plt.title(clase_label)#, y=1.15)

        fig.show()

def mutar_genotipo(genotipo_a_mutar: genotipo):
    genotipo_mutado = genotipo_a_mutar
    # TODO: completar
    return genotipo_mutado

def combinar_genotipo(padre1: genotipo, padre2: genotipo):
    hijo = padre1 + padre2
    # TODO: completar
    return hijo