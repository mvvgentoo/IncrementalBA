# -*- coding: utf-8 -*-

import numpy as np

class Matrix:
   def __init__(self, arr, datatype):
       self.dat = np.array(arr, dtype = datatype)
       self.dtype = datatype

   @classmethod
   def FromPlain(cls, i, j, arr):
       return cls(np.array(arr).reshape(i,j))
       
   @classmethod
   def zeros(cls, i, j, datatype):
       arr = [0]*(i*j)
       return cls(np.array(arr).reshape(i,j), datatype)    
       
   def __str__(self):
       return str(self.dat)
       
   def __getitem__(self, i, j):
       return self.dat[i,j]
       
   def __setitem__(self, i, value):        
       self.dat[i] = value
       
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
       
