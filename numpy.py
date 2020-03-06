import numpy as np
import sys
print("USO DE MEMORIA PYTHON")
S=range(1000)
print(sys.getsizeof(5)*len(S))
print("\n"*1)
print("USO DE MEMORIA NUMPY")
D=np.arange(1000)
print(D.size*D.itemsize)