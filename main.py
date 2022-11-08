import numpy as np
import sys

if len(sys.argv) == 8:
    semilla = int(sys.argv[1])
    nodos = str(sys.argv[2])
    numero_hormigas = int(sys.argv[3])
    numero_iteraciones = int(sys.argv[4])
    evaporacion_feromona = float(sys.argv[5])
    valor_heuristica = float(sys.argv[6])
    probabilidad_limite = float(sys.argv[7])
    print("Semilla: ", semilla, "Matriz de nodos y coordenadas: ", nodos, "Numero de hormigas: ", numero_hormigas, "Numero de iteraciones maximas: ", numero_iteraciones, "factor de evaporacion de la feromona: ", evaporacion_feromona, "Peso del valor de la heuristica: ", valor_heuristica, "Valor de la probabilidad limite: ", probabilidad_limite, sep='\n')
else:
    print("Error en la entrada de los parametros", "Los paramentros a ingresar son: semilla, Matriz de nodos y coordenadas, Tamaño de la poblacion, Numero de iteraciones maximas, factor de evaporacion de la feromona, peso del valor de la heuristica, Valor de la probabilidad limite", sep='\n')
    sys.exit(0)

np.random.seed(semilla)



def crear_solucion_inicial():   # Creamos un arreglo mezclado con los valores de 0 hasta numero_nodos - 1 sin repetir 
    solucion_inicial = np.arange(numero_nodos)
    np.random.shuffle(solucion_inicial)
    return solucion_inicial

def crear_matriz_distancias():  # Creamos una matriz de numero_nodos x numero_nodos con 0s y 1s en la diagonal, luego reemplazamos la diagonal superior con las distancias de los nodos i, j y para hacerla simetrica le sumamos la transpuesta
    matriz_distancias = np.full((numero_nodos,numero_nodos),0, dtype=float) + np.eye(numero_nodos, dtype=int)
    for i in range(numero_nodos):
        for j in range(i + 1, numero_nodos):
            distancia = np.sqrt(np.sum(np.square(nodos[i]-nodos[j])))
            matriz_distancias[i][j] = distancia
    matriz_distancias = matriz_distancias + matriz_distancias.T
    return matriz_distancias

def calcular_distancia_hormiga(arr):    # Sumamos en una variable auxiliar las distancias de los valores del arreglo en la matriz de distancia
    aux = 0
    for i in range(arr.shape[0] - 1):
        aux += matriz_distancias[arr[i]][arr[i + 1]]
    aux += matriz_distancias[arr[0]][arr[arr.shape[0] - 1]]
    return aux






nodos = np.genfromtxt(nodos, dtype = float, delimiter=' ', skip_header = 6, skip_footer=1, usecols=(1,2))
numero_nodos = nodos.shape[0]
matriz_distancias = crear_matriz_distancias()
