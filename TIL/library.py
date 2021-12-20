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

import numpy as np

# NaN 결측치 비어있는값

np.random.rand(10)

arr=np.arrange(1,11)
np.random.choice(arr,size=5,replace=False)

arr1d=np.random.randint(0,10,size=4)
arr1d

arr2d=np.random.randint(1,10,size=(3,3))

import numpy as np
import pandas as pd

weight = pd.DataFrame([
  [76.4, 'kg'],
  [75.7, 'kg'],
  [76, 'kg'],
  [76.2, 'kg']
])
weight