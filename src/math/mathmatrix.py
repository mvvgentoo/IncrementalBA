# -*- coding: utf-8 -*-

import numpy as np

if __name__ == '__main__':
    pass
else:
    from ..containers import Matrix     
       
class MathMatrix(Matrix):
    def __init__(self, arr):
       Matrix.__init__(self, arr, np.float64)
       
    @classmethod
    def zeros(cls, i, j):
       arr = [0]*(i*j)
       return cls(np.array(arr).reshape(i,j))     
       
    def svd(self):
        return  np.linalg.svd(self.dat, full_matrices=True)
        
    
       
class IntMatrix(Matrix):
   def __init__(self, arr):
       Matrix.__init__(self, arr, np.int64)
