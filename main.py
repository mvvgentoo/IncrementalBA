# -*- coding: utf-8 -*-

from src.math import *
from src.io import *
from src.graph import *
from src.containers import *

import os
import sys

print(os.getcwd() )

filename = sys.argv[1]

dataInfo = ReadingAssistant.FillDataStructures(filename)

tbl = dataInfo.GetTableElement(0,1)

graphAnalysisTool=GraphAnalysis()

components = graphAnalysisTool.GetAllConnectedComponent(dataInfo.GetGraphInfo())
for comp in components:
   print(comp)

paths = graphAnalysisTool.GetOptimalPathsFrom(dataInfo.GetGraphInfo(), 0)   
for key in paths.keys():
   print(key, paths[key])
    