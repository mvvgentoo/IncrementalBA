# -*- coding: utf-8 -*-

import numpy as np

if __name__ == '__main__':
    pass    
else:   
    from .datatypes import DataTypes
    

class Matrix:
   def __init__(self, arr, datatype = DataTypes.DoubleType()):
       self.dat = np.array(arr, dtype = datatype)
       self.dtype = datatype

   @classmethod
   def FromPlain(cls, i, j, arr, datatype = DataTypes.DoubleType()):
       return cls(np.array(arr).reshape(i,j), datatype)
       
   @classmethod
   def zeros(cls, i, j, datatype = DataTypes.DoubleType()):
       arr = [0]*(i*j)
       return cls(np.array(arr).reshape(i,j), datatype)    
       
   def __str__(self):
       return str(self.dat)
       
   def __getitem__(self, i):
       return self.dat[i]
       
   def __setitem__(self, i, value):        
       self.dat[i] = value
       
   def GetArray(self):
       return self.dat
       
   def __sub__(self, B):
       return Matrix(self.dat - B.dat, self.dtype)
       
   def __add__(self, B):
       return Matrix(self.dat + B.dat, self.dtype)    
       
   #matrix multiplication    
   def __mul__(self, B):
       return Matrix(self.dat.dot(B.dat), self.dtype)
       
   #elementwise product    
   def __matmul__(self,B):
       return Matrix(self.dat * B.dat, self.dtype)
       
