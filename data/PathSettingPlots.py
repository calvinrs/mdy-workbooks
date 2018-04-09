# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:43:56 2018

@author: stewarca
"""

import matplotlib.pyplot as plt
import xlwings as xw
import pandas as pd

thisSheet = xw.Book("EndDec2017_Path_Setting_Tool_G.xlsm").sheets("General")

df = thisSheet.range('B5').options(pd.DataFrame,index=True, header=1,expand='table').value
df.head()

#df.plot()

fig = plt.figure(figsize=(8,6))
plt.subplot(2, 1, 1)
plt.plot(df.S,ls='--')
plt.plot(df.M,ls='--')
plt.plot(df.L,ls='--')
plt.plot(df.r)

plt.axvline(x=10,ls='--',color='m')
plt.axvline(x=30,ls='--',color='m')

plt.legend()
plt.title("Path Setting - curve blending over time")
plt.xlabel("time")
plt.ylabel("rate")

#thisSheet.pictures.add(fig, name='CurveBlend', update=True)


#fig = plt.figure()
plt.subplot(2, 1, 2)
plt.plot(df["weight on S"],ls='--')
plt.plot(df["weight on M"],ls='--')
plt.plot(df["weight on L"],ls='--')

plt.axvline(x=10,ls='--',color='m')
plt.axvline(x=30,ls='--',color='m')

plt.legend()
#plt.title("Path Setting - weights on paths")
plt.xlabel("time")
plt.ylabel("weight")

#thisSheet.pictures.add(fig, name='Weights', update=True)

thisSheet.pictures.add(fig, name='Paths', update=True)

# =============================================================================
# if __name__ == '__main__':
#     # Expects the Excel file next to this source file, adjust accordingly.
#     xw.Book("EndDec2017_Path_Setting_Tool_G.xlsm").set_mock_caller()
#     compareBHCFiles()
# =============================================================================
