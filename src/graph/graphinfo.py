# -*- coding: utf-8 -*-

import numpy as np

if __name__ == '__main__':    
    pass    
else:   
    from ..containers.matrix import Matrix
    from ..containers.datatypes import DataTypes


class GraphInfo:
    def __init__(self, n):
        self.dim = n
        self.AdjacencyTable = Matrix.zeros(n,n, DataTypes.BoolType() )
        self.WeightTable = Matrix.zeros(n,n, DataTypes.DoubleType() )

    def AddEdge(self,u,v,weight):        
        [i,j] = [u,v] if u < v else [v,u]
        self.AdjacencyTable[i,j] = True
        self.WeightTable[i,j] = weight    
        
    def __str__(self):
        return str(self.AdjacencyTable)
        
    def GetWeight(self, u, v):
        if u < v:
            return self.WeightTable[u,v]
        else:
            return self.WeightTable[v,u]
        
    def HasEdge(self, u, v):
        if u < v:
            return self.AdjacencyTable[u,v]
        else:
            return self.AdjacencyTable[v,u]
            