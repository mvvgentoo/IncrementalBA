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
   
   @classmethod
   def identity(cls, n, datatype = DataTypes.DoubleType()):
       return cls(np.identity(n), datatype)   
   
   @classmethod
   def skew(cls, v, datatype = DataTypes.DoubleType()):
       arr=[0,-v[2],v[1],v[2],0,-v[0],-v[1],v[0],0]       
       return cls(np.array(arr).reshape(3,3), datatype)

   @classmethod
   def skewSquare(cls, v, datatype = DataTypes.DoubleType()):
       arr=np.array([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
       res = arr.dot(arr)
       return cls(np.array(res).reshape(3,3), datatype)

   
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
       
   def trace(self):
       return np.trace(self.dat)
       
   def onScalar(self, scalar):
       return Matrix(np.dot(self.dat, scalar))
       
   
       
   
       
