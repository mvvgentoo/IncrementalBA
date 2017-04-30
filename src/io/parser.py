# -*- coding: utf-8 -*-

class FileParser:
    def __init__(self, filename, headerStringParser, dataParser):
        self.filename = filename
        self.headerParser = headerStringParser
        self.dataParser = dataParser
        self.scannerObj = open(filename, "r")
        self.currentHeader = ""
        self.prevHeader = ""
    
    def CheckHeaderLine(self, headerLine):
        return self.headerParser.CheckHeaderLine(headerLine)

    def GetHeader(self):         
        expression = " "       
       
        while True:       
           try:
               line = next(self.scannerObj).strip()
               print(line)
               stripped = line.replace(expression, "")
       
               if self.CheckHeaderLine(stripped):           
                   self.prevHeader = self.currentHeader
                   self.currentHeader = line
                   return True
           except:
               return False

    def GetCurrentMetadata(self):
        return self.headerParser.GetHeaderMetadata(self.currentHeader)
   
   
    def GetCurrentHeader(self):
        return self.currentHeader
   
    def GetNextData(self, pairList):
   
        hasHeader = self.GetHeader()
        
        if not hasHeader:
            return False				             
        
        return self.dataParser.GetNextData(self.scannerObj, pairList)        
                