#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:26:40 2022

@author: boris
"""

import pandas as pd
import numpy as np
import seaborn as sns


url = 'https://github.com/bdemeshev/om_ts/raw/main/data/marriages_original.xls'

marr = pd.read_excel(url)


from sktime.datasets import load_airline
from sktime.utils.plotting import plot_series

