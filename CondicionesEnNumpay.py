import numpy as np
ar = np.linspace(1, 10, 10, dtype="int8")
print(ar)
indices_con = ar > 5
print(indices_con)
print(ar[indices_con])
print(ar[(ar>5)&(ar < 9)])
ar [(ar > 5)] = 99
print(ar)
