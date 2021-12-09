import numpy as np

arrid=np.array([1,2,3,4])
arrid

arrid.shape

arrN=np.arange(1,31).reshape(3,10)
arrN

display(arrN[1,5])

display(arrN[2,-2])

display(arrN[1,3:6])

display(arrN[-2:,-3])

display(arrN[:2,8:])

arrn=np.arange(1,51).reshape(5,10)
arrn

display(arrn[1:4,3:7])

display(arrn[1:4,1])

arr=np.arange(1,46)
arr
np.random.choice(arr,size=6,replace=False)