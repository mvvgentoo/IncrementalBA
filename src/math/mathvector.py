# -*- coding: utf-8 -*-
import numpy as np

class MathVector:
   def __init__(self, arr):
       self.dat = np.array(arr)
       
   def __matmul__(self, B):
       return MathVector(np.cross(self.dat, B.dat) )
