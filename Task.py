import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_excel('lab_4_part_5.xlsx', header=1)

print(df.head())

print(df.groupby('точка').size().reset_index(name='count'))

"""
fig, axes = plt.subplots(2, 4, figsize=(10, 7))

data = df[['точка', 'товар', 'Продажи']]
#data['place and product'] = df['точка'] + ' ' + df['товар']
#print(data)

ax = np.ravel(axes)
df['month'] = pd.to_datetime(df['Дата']).dt.month
df['year'] = pd.to_datetime(df['Дата']).dt.year
places = data['точка'].unique()
for i in range(7):
    axData = data[data['точка'] == places[i]].groupby('товар').sum().reset_index()[:20]
    #print(axData)
    ax[i].bar(axData['товар'], axData['Продажи'])
    ax[i].set_xticklabels(axData['товар'], rotation=90, ha='center', fontsize=5)
    ax[i].set_title(f"Place {i + 1}", loc='center')
"""


"""
sales = df.groupby('товар')['Продажи'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 8))
plt.pie(sales.values[:10], 
        labels=sales.index[:10], 
        autopct='%1.1f%%')
plt.title('10 most popular products')

plt.show()
"""

df['month'] = df['Год-мес'] % 100

plt.figure(figsize=(7, 4))
data = df[['month', 'Продажи']].groupby('month').sum().reset_index()
plt.plot(data['month'], data['Продажи'])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()