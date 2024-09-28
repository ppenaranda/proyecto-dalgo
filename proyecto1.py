import sys





numeros = [
    [0, 9, 1, 10, 0],
    [-1, 5, 5, 25, 5],
    [1, 14, 12, 5, 7],
    [5, 5, 4, 15, 2],
    [55, 3, 0, 4, 1]
]
def remove_extremes(lst, m):
    if m * 2 > len(lst):  # Verificar que no se elimine más de lo que la lista puede soportar
        return []
    return lst[m:-m]



def exploracion(piramide):
    
    simulacionDeCeldas = [[0 for celda in range(len(piramide[0]))] for fila in range (len(piramide))] #dp
    """
    El simulacion de Camaras fue hecho en caso de conflictos, se tienen dudas aun de qué
    prioridad tiene un explorador con otro. 

    """
    
    
    """
    Se hará en top bottom desde el punto de encuentro reduciendo de a una las opciones y sumando
    """

    
    for pasosSallah in range((len(piramide)//2)-1, len(piramide), 1 ):
        pasoRealSallah = (len(piramide)//2) + pasosSallah
        if pasoRealSallah > len(piramide)-1:
            break
        #verificamos si son solo rectanngulos primero
        if pasoRealSallah < len(piramide) and len(simulacionDeCeldas[0])>=pasoRealSallah:
            pasoSiguienteSallah = remove_extremes(piramide[pasoRealSallah], pasosSallah)
            pasoActualSallah = piramide[pasoRealSallah-1]
            
            for celda in range(len(pasoSiguienteSallah)):
                if celda == 0 :
                    """
                    Hallar el maximo del medio
                    """
                    maximo = 0
                    
                    if pasoActualSallah[celda]>0:
                        maximo = max(maximo, pasoActualSallah[celda]+pasoSiguienteSallah[celda])
                    if pasoActualSallah[celda+1]>0:
                        maximo = max(maximo, pasoActualSallah[celda+1]+pasoSiguienteSallah[celda])
                    if pasoActualSallah[celda+2]>0:
                        maximo = max(maximo, pasoActualSallah[celda+2]+pasoSiguienteSallah[celda])
                    
                    simulacionDeCeldas[pasoRealSallah][celda+1] = maximo
                    piramide[pasoRealSallah][celda+1] = 0
                elif 0<celda<len(pasoSiguienteSallah)-1:
                    maximo=0
                    
                    if pasoActualSallah[celda-1]>0:
                        maximo = max(maximo, pasoActualSallah[celda]+pasoSiguienteSallah[celda])
                        
                    if pasoActualSallah[celda]>0:
                        maximo = max(maximo, pasoActualSallah[celda+1]+pasoSiguienteSallah[celda])
                        
                    if pasoActualSallah[celda+1]>0:
                        maximo = max(maximo, pasoActualSallah[celda+2]+pasoSiguienteSallah[celda])
                
                    simulacionDeCeldas[pasoRealSallah][celda+1] = maximo
                    piramide[pasoRealSallah][celda+1] = 0

                elif celda == len(pasoSiguienteSallah)-1:
                    maximo = 0
                    if pasoActualSallah[celda]>0:
                        
                        maximo = max(maximo, pasoActualSallah[celda]+pasoSiguienteSallah[celda])
                    if pasoActualSallah[celda+1]>0:
                        
                        maximo = max(maximo, pasoActualSallah[celda+1]+pasoSiguienteSallah[celda])
                    if pasoActualSallah[celda+2]>0:
                        
                        maximo = max(maximo, pasoActualSallah[celda+2]+pasoSiguienteSallah[celda])
                    
                    simulacionDeCeldas[pasoRealSallah][celda+1] = maximo
                    piramide[pasoRealSallah][celda+1] = 0
    
    for paso in range(len(piramide)//2,-1,-1):
        if piramide[1][1] == -1 and piramide[1][0]==-1 and piramide[1][len(piramide[0])-1]==-1 and piramide[1][len(piramide[0])-2]==-1:
            break
        if paso == 0:
            simulacionDeCeldas[0][0] = max(simulacionDeCeldas[1][0], simulacionDeCeldas[1][1])
            simulacionDeCeldas[0][len(piramide[0])-1] = max(simulacionDeCeldas[1][len(piramide[0])-1], simulacionDeCeldas[1][len(piramide[0])-2])
            
        if paso > 0:
            columnas = len(piramide[0])
            
            if paso <= columnas:
                
                opcionesPasoAnterior = piramide[paso-1][:paso]
                opcionesPasoAnteriorMarion = piramide[paso-1][len(piramide[paso-1])-paso:] 
            else:
                opcionesPasoAnterior = piramide[paso-1]
                opcionesPasoAnteriorMarion = opcionesPasoAnterior
            opcionesPasoAnteriorMarion = piramide[paso-1][len(piramide[paso-1])-paso:] 

            mitadEnteraDelpaso = piramide[paso][:paso+1]
            mitadEnteraDelPasoMarion = piramide[paso][len(piramide[paso-1])-paso-1:]

            for celdaMarion in range(len(opcionesPasoAnteriorMarion)):

                if celdaMarion == len(opcionesPasoAnteriorMarion)-1 and opcionesPasoAnteriorMarion[celdaMarion] > 0:
                    
                    maximo = 0

                    if mitadEnteraDelPasoMarion[len(mitadEnteraDelPasoMarion)-2]>0:
                        maximo = max(
                            mitadEnteraDelPasoMarion[len(mitadEnteraDelPasoMarion)-2]+ opcionesPasoAnteriorMarion[celdaMarion], 
                                     maximo
                                     )
                        
                    if mitadEnteraDelPasoMarion[len(mitadEnteraDelPasoMarion)-1]>0:
                        maximo = max(
                            mitadEnteraDelPasoMarion[len(mitadEnteraDelPasoMarion)-1]+ opcionesPasoAnteriorMarion[celdaMarion], 
                            maximo
                            )
                    
                    simulacionDeCeldas[paso-1][len(piramide[paso])-celdaMarion]= maximo
                    piramide[paso-1][len(piramide[paso])-celdaMarion]=0
                
                elif celdaMarion < len(opcionesPasoAnteriorMarion)-1:
                    maximo = 0
                    if piramide[paso-1][len(simulacionDeCeldas[paso-1])//2+celdaMarion+1]>=0:

                        if mitadEnteraDelpaso[celdaMarion-1]>=0:
                            maximo = max(
                                mitadEnteraDelPasoMarion[celdaMarion-1]+opcionesPasoAnteriorMarion[celdaMarion], 
                                maximo)
                            
                        if mitadEnteraDelpaso[celdaMarion]>=0:
                            maximo = max(
                                mitadEnteraDelPasoMarion[celdaMarion]+opcionesPasoAnteriorMarion[celdaMarion], 
                                maximo) 
                            
                        if mitadEnteraDelpaso[celdaMarion+1]>=0:
                            maximo = max(
                                mitadEnteraDelPasoMarion[celdaMarion+1]+opcionesPasoAnteriorMarion[celdaMarion], 
                                        maximo)
                    
                    simulacionDeCeldas[paso-1][len(simulacionDeCeldas[paso-1])//2+celdaMarion+1]=maximo
                    piramide[paso-1][len(simulacionDeCeldas[paso-1])//2+celdaMarion+1]=0
                elif celdaMarion==0 and len(simulacionDeCeldas[0])==len(mitadEnteraDelPasoMarion):
                    """
                    Este solo sirve si falta poco
                    """
                    maximo=0
                    if mitadEnteraDelPasoMarion[celdaMarion]>-1:
                        maximo = max(
                            mitadEnteraDelPasoMarion[celdaMarion]+opcionesPasoAnteriorMarion[celdaMarion+1],
                            maximo
                        )
                    if mitadEnteraDelPasoMarion[celdaMarion+1]>-1: 
                        
                        maximo = max(
                            mitadEnteraDelPasoMarion[celdaMarion+1]+opcionesPasoAnteriorMarion[celdaMarion+1],
                            maximo
                        )
                    
                    simulacionDeCeldas[paso-1][1]=maximo
                    piramide[paso-1][1]=0
                             
                            
            for celda in range(len(opcionesPasoAnterior)):
                if celda == 0 and opcionesPasoAnterior[celda]>0: #Esta pegado a la pared 
                    maximo = 0
                    if mitadEnteraDelpaso[0]>0:
                        maximo = max(mitadEnteraDelpaso[0]+opcionesPasoAnterior[celda], maximo)
                    if mitadEnteraDelpaso[1]>0:
                        maximo = max(mitadEnteraDelpaso[1]+opcionesPasoAnterior[celda], maximo)
                    simulacionDeCeldas[paso-1][celda] = maximo
                    piramide[paso-1][celda] = 0
                    
                elif len(opcionesPasoAnterior)+1>celda > 0 and paso > 0 and opcionesPasoAnterior[celda]>0:
                    #Cuando esta en todo el medio
                    maximo = 0
                    if mitadEnteraDelpaso[celda-1]>-1:
                        maximo = max(maximo, mitadEnteraDelpaso[celda-1]+opcionesPasoAnterior[celda])
                    if mitadEnteraDelpaso[celda]>1:
                        maximo = max(maximo, mitadEnteraDelpaso[celda]+opcionesPasoAnterior[celda])
                    
                    if mitadEnteraDelpaso[celda+1]>1:
                        maximo = max(maximo, mitadEnteraDelpaso[celda+1]+opcionesPasoAnterior[celda])
                    

                    simulacionDeCeldas[paso-1][celda] = maximo
                    piramide[paso-1][celda] = 0
                elif celda == len(mitadEnteraDelpaso)-1: # cuando indiana esta pegado en la otra pared
                    if mitadEnteraDelpaso[celda-1]>-1:
                        maximo = max(maximo,mitadEnteraDelpaso[celda-1]+opcionesPasoAnterior[celda])
                    if mitadEnteraDelpaso[celda]>-1:
                        maximo = max(maximo,mitadEnteraDelpaso[celda]+opcionesPasoAnterior[celda])
                    simulacionDeCeldas[paso-1][celda]=maximo
                    piramide[paso-1][celda]=0

    simulacionDeCeldas[len(simulacionDeCeldas)-1][len(simulacionDeCeldas)//2]=max(
        simulacionDeCeldas[len(simulacionDeCeldas)-2][(len(simulacionDeCeldas)//2)-1],
        simulacionDeCeldas[len(simulacionDeCeldas)-2][(len(simulacionDeCeldas)//2)],
        simulacionDeCeldas[len(simulacionDeCeldas)-2][(len(simulacionDeCeldas)//2)+1],
    )   
        
    print(
        simulacionDeCeldas[0][0],
        simulacionDeCeldas[len(simulacionDeCeldas)-1][len(simulacionDeCeldas)//2],
        simulacionDeCeldas[0][len(simulacionDeCeldas[0])-1]
            )        
         
            
    return (simulacionDeCeldas[0][0] +simulacionDeCeldas[0][len(simulacionDeCeldas[0])-1]+simulacionDeCeldas[len(simulacionDeCeldas)-1][len(simulacionDeCeldas)//2])     
                           


numerocasos = int(sys.stdin.readline())

for _ in range(numerocasos):
    r, c = map(int, sys.stdin.readline().strip().split())

    matriz = []
    for _  in range(r):
        fila = list(map(int, sys.stdin.readline().split()))
        matriz.append(fila)

    print(exploracion(matriz))