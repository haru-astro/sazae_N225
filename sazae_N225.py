from numpy.core.fromnumeric import ptp
import pandas as pd
import matplotlib.pyplot as plt

dfG = pd.read_excel('sazae_N225_gu-.xlsx')
dfC = pd.read_excel('sazae_N225_choki.xlsx')
dfP = pd.read_excel('sazae_N225_pa-.xlsx')
gu = dfG['gu-']
cho = dfC['choki']
pa = dfP['pa-']
df = pa.mean()

f = pd.concat([gu,cho,pa], axis=1)

size = f.abs().max().max()*1.1
boxplot = f.boxplot(column=['gu-', 'choki', 'pa-'],showmeans=True)
boxplot.plot()
plt.ylim([-size,size])
plt.figure(figsize=(4,4),dpi=500)
plt.show()