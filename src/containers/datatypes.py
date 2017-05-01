# -*- coding: utf-8 -*-

import numpy as np

class DataTypes:
    def __init__(self):
        raise NotImplementedError
    
    @classmethod
    def DoubleType(cls):
        return np.float64
        
    @classmethod
    def IntegerType(cls):
        return np.int64
        
    @classmethod
    def BoolType(cls):
        return np.bool    
        
        