# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 03:38:45 2020

@author: ppangatungan
"""

import pandas as pd 

df = pd.read_csv('DataSeerGrabPrizeData.csv')

df.describe()

df.dropna()

df.describe()

df.to_csv('grab_on_spyder.csv', index=False)