# -*- coding: utf-8 -*-
import numpy as np

if __name__ == '__main__':
    pass
else:
    from ..containers import Vector, DataTypes

class MathVector(Vector):
   def __init__(self, arr):
       Vector.__init__(self, arr, DataTypes.DoubleType())
       
   def __matmul__(self, B):
       return MathVector(np.cross(self.dat, B.dat) )
