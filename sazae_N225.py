import pandas as pd
import matplotlib.pyplot as plt

dfG = pd.read_excel('sazae_N225_gu-.xlsx')
dfC = pd.read_excel('sazae_N225_choki.xlsx')
dfP = pd.read_excel('sazae_N225_pa-.xlsx')
gu = dfG['gu-']
cho = dfC['choki']
pa = dfP['pa-']
df = pa.mean()
print(df)

f = pd.concat([gu,cho,pa], axis=1)

boxplot = f.boxplot(column=['gu-', 'choki', 'pa-'])
boxplot.plot()
plt.ylim([-50,50])
plt.show()