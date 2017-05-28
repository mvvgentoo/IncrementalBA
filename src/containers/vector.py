# -*- coding: utf-8 -*-

import numpy as np

if __name__ == '__main__':
    pass    
else:   
    from .datatypes import DataTypes

class Vector:
   def __init__(self, arr, datatype = DataTypes.DoubleType()):
       self.dat = np.array(arr, dtype = datatype)
       self.dtype = datatype
       
   def __str__(self):
       return str(self.dat)
       
   def __getitem__(self, i):
       return self.dat[i]
       
   def __setitem__(self, i, value):        
       self.dat[i] = value
       
   def GetArray(self):
       return self.dat

   def norm(self, n):
       return np.linalg.norm(self.dat, n)

   def euclidNorm(self):
       return

   def onScalar(self, scalar):
       return Vector(np.dot(self.dat, scalar))