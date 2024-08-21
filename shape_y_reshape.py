import numpy as np
arr = np.random.randint(1, 10,(3,2))
print("Forma original: ", arr.shape)
print(arr)
#cambiamos la forma del arreglo a una forma de (1,6)
arr_reshape = arr.reshape(1,6)
#imprimimos la nueva forma
print("arreglo despues del reshape: ", arr_reshape.shape)