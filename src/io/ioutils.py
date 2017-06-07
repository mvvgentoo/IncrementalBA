# -*- coding: utf-8 -*-

if __name__ == '__main__':
    pass    
else:
    from .parserfactory import FileParserFactory
    from ..containers import Table
    from ..graph import GraphInfo
    

class FileWrapper:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return str(self.name)
      

class DataInfoWrapper:
    def __init__(self, numImg):
        self.numImg = numImg
        self.table = Table.zeros(numImg, numImg)
        self.graph = GraphInfo(numImg)
        self.imageNames = [""]*numImg
        
    def SetTable(self, i,j,data):
        self.table[i,j] = data
        
    def SetGraphEdge(self, i, j, weight):
        self.graph.AddEdge(i,j,weight)
        
    def AddImageName(self, i, name):
        if self.imageNames[i] == "":
            self.imageNames[i] = name
        
    def GetNumberOfImages(self):
        return self.numImg
        
    def GetTable(self):
        return self.table
    
    def GetGraphInfo(self):
        return self.graph
        
    def GetImageNameList(self):
        return self.imageNames
        
    def GetTableElement(self, i, j):
        return self.table[i,j]
        
class ReadingAssistant:
    @classmethod
    def GetNumImagesInFile(cls,filename):
        reader = FileParserFactory.CreatePointFileParser(filename)
        
        lst = []
        [left, right] = [0, 0]
        num = 0
        while reader.GetNextData(lst) :
            data = reader.GetCurrentMetadata()
            left = data["left"]["num"]
            right = data["right"]["num"]
            num = max(num,max(left,right) )
            lst = []
            
        return num + 1
    
    @classmethod
    def FormDataTableAndGraph(self, filename, table, graph):
        reader = FileParserFactory.CreatePointFileParser(filename)
        
        lst = []        
        while reader.GetNextData(lst) :
            data = reader.GetCurrentMetadata()
            left = data["left"]["num"]
            right = data["right"]["num"]
            print(lst)
            table[left, right] = lst
            graph.AddEdge(left, right, 1.0 / len(lst))

            lst=[]
            
    
    @classmethod
    def FillDataStructures(self, filename):        
        reader = FileParserFactory.CreatePointFileParser(filename)
        
        lst = []
        [left, right] = [0, 0]
        num = 0
        dataarr = []
                
        while reader.GetNextData(lst) :
            data = reader.GetCurrentMetadata()
            left = data["left"]["num"]
            right = data["right"]["num"]
            leftName = data["left"]["name"]
            rightName = data["right"]["name"]                                                        
            num = max(num,max(left,right) )
            dataarr.append([left, right, leftName, rightName, lst])
            lst = []
            
        numImg = num + 1
        
        dataInfoWrapper = DataInfoWrapper(numImg)
        
        for val in dataarr:
            dataInfoWrapper.SetTable(val[0], val[1], val[4])
            dataInfoWrapper.SetGraphEdge(val[0], val[1], 1.0 / len(val[4]) )
            dataInfoWrapper.AddImageName(val[0], val[2])                     
            dataInfoWrapper.AddImageName(val[1], val[3])                     
            
        return dataInfoWrapper    
