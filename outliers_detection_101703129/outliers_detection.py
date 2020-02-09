# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 12:15:10 2020

@author: Ayush Garg
"""

import numpy as np
import csv
from io import StringIO

def outlier(data):
    rows = []
    outliers = []
    buffer = StringIO()
    data.to_csv(buffer)
    buffer.seek(0)
    data1 = csv.reader(buffer)
    fields = next(data1)
    for row in data1:
        rows.append(int(row[-1]))
    sorted(rows)
    quantile1, quantile3 = np.percentile(rows,[25,75])
    iqr_value = quantile3-quantile1
    lower_bound_val = quantile1 -(1.5 * iqr_value) 
    upper_bound_val = quantile3 +(1.5 * iqr_value)
    for value in rows:
        if value not in range(int(lower_bound_val),int(upper_bound_val)):
            outliers.append(value)
    print("Outliers: ",outliers)
    print("No. of outliers or no. of rows to be removed: ",len(outliers))