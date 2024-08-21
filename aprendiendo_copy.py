import numpy as np
arr= np.arange(0, 11)
print(arr)
trozo_de_arr = arr[0:6]
print(trozo_de_arr)
#A todo mi array le quiero quitar todos los valores y dejarlos en 0
trozo_de_arr[:] = 0
print(trozo_de_arr)
#si ahora imprimimos el arr, veras que todos los valores han sido cambiados
print(arr)
#para solucionar este problema, podemos usar la funcion copy()
arr_copy = arr.copy()
print(arr_copy)
arr_copy[:] = 100
print(arr_copy)
#no obstante la lista original no ha sido cambiada
print(arr)
