# -*- coding: utf-8 -*-

import re

class PairFileHeaderParser:
    def __init__(self):
        pass
    
    def CheckHeaderLine(self, headerLine):
        expression = " "
        if len(headerLine) != 0:
            stripped = headerLine.replace(expression, "")                
        
            if len(stripped) and stripped.startswith("#"):
                return True        
        
        return False;
        
    def GetHeaderMetadata(self, header):
        metadataMap = {}
            
        arr = header.split("#");
        delims = "[(),x]+";
        tokens = re.split(delims, arr[1]);
        
        metadataMap["left"]   = {"num" : int(tokens[0].split("r")[1]), "name" :  tokens[2].replace(" ", "")}
        metadataMap["right"]  = {"num" : int(tokens[1]), "name" : tokens[3].replace(" ", "")}
        
        return metadataMap
   