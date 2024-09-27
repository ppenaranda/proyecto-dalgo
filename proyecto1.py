numeros = [
    [0, 9, 1, 10, 0],
    [-1, 1, 5, -1, 5],
    [1, 5, 1, 5, 7],
    [5, 5, 5, 15, 2],
    [55, 3, 0, 4, 1]
]

"""
QUEREMOS QUE BURRO NOS BAILE LA PELUSA
"""


def calcular():
    """
    @params:
    @returns: Tupla con la proxima celda de posición del explorador
    
    """
    pass

def exploracion(piramide):
    filaDeCamaras = [0 for celda in range(len(piramide[0]))]
    simulacionDeCeldas = [filaDeCamaras for fila in range (len(piramide))] #dp
    print(simulacionDeCeldas)
    """
    El simulacion de Camaras fue hecho en caso de conflictos, se tienen dudas aun de qué
    prioridad tiene un explorador con otro. 
    """
    
    sumaIndiana = 0
    coordenadasIndiana = [0,0]

    for paso in range ((len(piramide)//2)+1):        
        fila = piramide[paso]
        if paso == len(piramide)//2:
            print("ya todos llegaron a la mitad")
        else:
            siguienteFila = piramide[paso+1]
            if coordenadasIndiana[1] == 0:
                opcionesIndiana=[siguienteFila[0], siguienteFila[1]]
                maximaReliquia = max(opcionesIndiana)
                if  maximaReliquia == siguienteFila[0]:
                    coordenadasIndiana = [siguienteFila, siguienteFila[0]]
                elif maximaReliquia ==  siguienteFila[1]:
                    coordenadasIndiana = [siguienteFila, siguienteFila[1]]
            elif coordenadasIndiana[1] > 0:

    
    