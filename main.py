# -*- coding: utf-8 -*-

from src.math import *
from src.io import *
from src.graph import *
from src.containers import *

import os;

print(os.getcwd() )


filename = "Enter filename here"

dataInfo = ReadingAssistant.FillDataStructures(filename)

print(len(dataInfo.table[0,1] ) )
print(dataInfo.table[0,1] )
