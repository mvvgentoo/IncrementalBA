# -*- coding: utf-8 -*-

class Table:
    def __init__(self, rows, cols, arr):
       self.dat = arr
       self.rows = rows
       self.cols = cols
       
    @classmethod
    def zeros(cls, i, j):
       arr = [0]*(i*j)
       return cls(i,j,arr)
       
    def __str__(self):
       res = "{" + str(self.dat[0 : self.cols]) + "\n"
       for i in range(1, self.rows - 1):
          res = res + " " + str(self.dat[i * self.cols : (i+1) * self.cols]) + "\n"
       res = res + " " + str(self.dat[(self.rows - 1) * self.cols : self.rows * self.cols]) + "}"
       return res
       
    def __getitem__(self, ind):
       [i,j] = [ind[0], ind[1]]         
       return self.dat[i * self.rows + j]
       
    def __setitem__(self, ind, value):        
       self.dat[ind[0] * self.rows + ind[1]] = value