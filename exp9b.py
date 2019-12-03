# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:53:40 2019

@author: Nicole Sophia
"""

import pandas as pd

dim = pd.DataFrame({"Box": ['Box1', 'Box1', 'Box1', 'Box2', 'Box2', 'Box2'],
                    "Dimension": ["Length", "Width", "Height", "Length", "Width", "Height"],
                    "Value": [6, 4, 2, 5, 3, 4]})

tidydim = dim.pivot_table(index= ['Box'], columns = 'Dimension', values = 'Value')
tidydim['Volume'] = tidydim.Length*tidydim.Height*tidydim.Width

print(tidydim)
