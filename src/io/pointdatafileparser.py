# -*- coding: utf-8 -*-

class PointDataFileParser:
    def __init__(self):
        pass
    
    def GetNextData(self,scannerObj, pairList):
        flag = True
        start = True
        
        while flag:
            try:
                line = next(scannerObj).strip()
                while len(line) == 0 and start:
                    line = next(scannerObj).strip()
                    start = False
                    
                arr = line.split(" ")
                temp = [0.0]*4   
                
                i = 0
                for val in arr:
                    try:
                        temp[i] = float(val)
                        i = i + 1
                    except:
                        flag = False
                        break
                    
                if flag:    
                    pairList.append(temp)
            except:
                return False
                        
        
        return True