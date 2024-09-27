numeros = [
    [0, 9, 1, 10, 0],
    [2, 6, 5, -1, 5],
    [-1, 5, 1, 5, 7],
    [5, 5, 6, 15, 2],
    [55, 3, 0, 4, 1],
    [0, 9, 1, 10, 0],
    [2, 6, 5, -1, 5],
    [-1, 5, 1, 5, 7],
    [5, 5, 5, 15, 2],
    [55, 3, 0, 4, 1],
    [2, 6, 5, -1, 5],

]

"""
QUEREMOS QUE BURRO NOS BAILE LA PELUSA
"""


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
                if  maximaReliquia == siguienteFila[0] and maximaReliquia != -1:
                    sumaIndiana += siguienteFila[0]
                    coordenadasIndiana = [paso+1, 0]
                elif maximaReliquia ==  siguienteFila[1] and maximaReliquia != -1:
                    sumaIndiana += maximaReliquia
                    coordenadasIndiana = [paso+1, 1]
                else: 
                    print("Indiana se perdió en el tiempo")
        
            elif coordenadasIndiana[1] > 0:
                
                centro = siguienteFila[coordenadasIndiana[1]]
                izquierda = siguienteFila[coordenadasIndiana[1]-1]
                derecha = siguienteFila[coordenadasIndiana[1]+1]
                maximaReliquia =  max(centro, izquierda, derecha)
                print(izquierda, centro, derecha)
                if  maximaReliquia == centro and maximaReliquia != -1:
                    coordenadasIndiana= [paso+1, coordenadasIndiana[1]]
                    sumaIndiana+=maximaReliquia
                elif maximaReliquia == izquierda and maximaReliquia  != -1:
                    coordenadasIndiana = [paso+1, coordenadasIndiana[1]-1]
                    sumaIndiana+=maximaReliquia
                elif  maximaReliquia == derecha and maximaReliquia != -1:
                    coordenadasIndiana = [paso+1, coordenadasIndiana[1]+1]
                    sumaIndiana+=maximaReliquia
                else:
                    print("Indiana se perdió en el tiempo")
            print(coordenadasIndiana)
            print(sumaIndiana)
    
    

            
    
exploracion(numeros)