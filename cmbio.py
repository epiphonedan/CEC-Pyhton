import numpy as np
a=np.array([(8,9,10),(11,12,13)])
print(a)
print("\n"*2)
a=a.reshape(3,2)
print(a)

a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print("\n"*1)
print(a[1,2])

a=np.array([(1,2,3,4),(3,4,5,6)])
print(a[0:,1])