# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 08:59:35 2016

@author: Gary
"""

import numpy as np
import pandas as pd
import os


myFile = "newData.csv"

os.system("CppPython01.exe -newData.csv")

df = pd.read_csv("dataGen.csv")