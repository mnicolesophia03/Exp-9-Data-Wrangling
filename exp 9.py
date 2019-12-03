# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:23:25 2019

@author: Nicole Sophia
"""

import pandas as pd

math = pd.DataFrame({"Student": ["Ice Bear", "Panda", "Grizzly"],
                     "Math": [80, 95, 79]})

elecs = pd.DataFrame({"Student": ["Ice Bear", "Panda", "Grizzly"],
                     "Electronics": [85, 81, 83]})

geas = pd.DataFrame({"Student": ["Ice Bear", "Panda", "Grizzly"],
                     "GEAS": [90, 79, 93]})

esat = pd.DataFrame({"Student": ["Ice Bear", "Panda", "Grizzly"],
                     "ESAT": [93, 89, 88]})

merge = pd.merge(pd.merge(math, elecs, on='Student'), geas, on='Student')
mergef = pd.merge(merge, esat, on='Student')

print(mergef)

print(pd.melt(mergef, id_vars=["Student"], var_name='Subject', value_name='Grades'))