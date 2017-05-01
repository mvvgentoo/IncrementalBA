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

print(len(tbl))
print(tbl)
