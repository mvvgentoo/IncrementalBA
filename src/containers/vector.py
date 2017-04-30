# -*- coding: utf-8 -*-

import numpy as np

class Vector:
   def __init__(self, arr):
       self.dat = np.array(arr)
       
   def __matmul__(self, B):
       return Vector(np.cross(self.dat, B.dat) )
