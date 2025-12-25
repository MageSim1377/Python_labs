import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


df = pd.read_excel('lab_4_part_5.xlsx', header=1)

#print(df.head())

print(df.groupby('точка').size().reset_index(name='count'))

fig, axes = plt.subplots(2, 4, figsize=(10, 7))

data = df[['точка', 'товар', 'Продажи']]
#data['place and product'] = df['точка'] + ' ' + df['товар']
#print(data)

ax = np.ravel(axes)
places = data['точка'].unique()
for i in range(7):
    axData = data[data['точка'] == places[i]].groupby('товар').sum().reset_index()[:20]
    #print(axData)
    ax[i].bar(axData['товар'], axData['Продажи'])
    ax[i].set_xticklabels(axData['товар'], rotation=90, ha='center', fontsize=5)
    ax[i].set_title(f"Place {i + 1}", loc='center')



#axes[0].bar()

df['month'] = pd.to_datetime(df['Дата']).dt.month
df['year'] = pd.to_datetime(df['Дата']).dt.year
sns.lmplot(data=df, x='month', y='Продажи')

plt.show()
