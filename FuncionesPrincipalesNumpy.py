import numpy as np
#definamos numeros aleatorios del 1 al 20 en un vector
arr = np.random.randint(1, 20, 10)
print(arr)
#ahora lo llevaremos a una estructura matricial
matriz = arr.reshape(2,5)
print(matriz)
#con max voy a traer el numero mas grande que tenga nuestro arr
maximo = arr.max()
print(maximo)
maximo = matriz.max()
print(maximo)
#crearemos un array de 2 dimensiones
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
#¿que pasa cuando quieres unir el array b con el array a?
#con el operador concatenar se puede hacer esto
c = np.concatenate((a, b), axis = 0)
print(c)