# -*- coding: utf-8 -*-
"""ParetoChart_JB.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gxcHtvIQolVweLsxL30TcCK_vxD1IzcV
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

#upload the helpDesk.csv to your google drive
df = pd.read_csv("./HelpDesk.csv")

# print(df)

#set reason column as index for use in plots
df.index = df['reason']

#descending order
df = df.sort_values(by='importance(1-10)', ascending = False)

# print(df)

#cumlative percentage column is created w/ cumsum function
df['cumlativePercentage'] = df['importance(1-10)'].cumsum()/df['importance(1-10)'].sum()*100

#make sure only 2 decimals points are shown
df['cumlativePercentage'] = df['cumlativePercentage'].apply(lambda x: round(x,2))

print(df)


fig, ax = plt.subplots()

ax.bar(df.index, df['importance(1-10)'], color='C3')

#show labels diagonally
ax.set_xticklabels( df['reason'], rotation = 45)

#ax2 and ax1 will be shown at same time with twinx func
ax2 = ax.twinx()

ax2.plot(df.index, df['cumlativePercentage'], color='C9', marker='D', ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())



ax.tick_params(axis='y', colors='C2')
ax2.tick_params(axis='y', colors='C1')



for index, v in df.iterrows():
    label = round(v['cumlativePercentage'],1)
    plt.annotate(label, xy=(v['reason'], v['cumlativePercentage']), color='C1')

plt.show()

