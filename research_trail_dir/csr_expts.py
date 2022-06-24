#sparce matrix
import numpy as np
from scipy.sparse import csr_matrix

A=np.array([
    [1,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,1,0,0,0],
    [0,0,1,0,0,0,0,1,0]
])
print(A)
B=csr_matrix(A)
print(B)
print(type(B))

#To reverse the operation
C=B.todense()
print(C)