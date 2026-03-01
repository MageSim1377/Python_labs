import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from datetime import datetime, timedelta


df = pd.read_excel('lab_4_part_5.xlsx', header=1)

print(df.head())

print(df.groupby('точка').size().reset_index(name='count'))


data = df[['точка', 'товар', 'Продажи']]
"""
fig, axes = plt.subplots(1, 1, figsize=(10, 7))

#data['place and product'] = df['точка'] + ' ' + df['товар']
#print(data)
ax = np.ravel(axes)
df['month'] = pd.to_datetime(df['Дата']).dt.month
df['year'] = pd.to_datetime(df['Дата']).dt.year
places = data['точка'].unique()

#i = 7
for i in range(7):
    axData = data[data['точка'] == places[i]].groupby('товар').sum().reset_index()[:20]
    #print(axData)
    ax[i].bar(axData['товар'], axData['Продажи'])
    ax[i].set_xticklabels(axData['товар'], rotation=45, ha='center', fontsize=8)
    ax[i].set_title(f"{places[i]}", loc='center')
    print(axData.describe())
"""






sales = df.groupby('товар')['Продажи'].sum().sort_values(ascending=False)

# plt.figure(figsize=(8, 8))
# plt.pie(sales.values[:10], 
#         labels=sales.index[:10], 
#         autopct='%1.1f%%')
# plt.title('10 most popular products')

# plt.show()


#------------------------------------------------------------------------
"""
products = sales.index[:10].unique()
print(products)
for i in range(10):
    df['month'] = pd.to_datetime(df['Дата']).dt.month

    days = df[df['товар'] == products[i]].groupby('Дата')['Продажи'].sum().reset_index()
    days = days.assign(date=pd.to_datetime(days['Дата']))

    firstDay = days['date'].min()
    days = days.assign(days_amount = (days['date'] - firstDay).dt.days)

    x_train = days[['days_amount']]
    y_train = days['Продажи']

    reg = linear_model.LinearRegression()
    reg.fit(x_train, y_train)
    tomorrow = (datetime.now() + timedelta(days=1) - firstDay).days
    print(f"Sales of {products[i]} tomorrow: {reg.predict(pd.DataFrame([[tomorrow]], columns=['days_amount']))[0]:.1f}")

"""
#------------------------------------------------------------------------
"""
df['month'] = pd.to_datetime(df['Дата']).dt.month

days = df.groupby('Дата')['Продажи'].sum().reset_index()
days = days.assign(date=pd.to_datetime(days['Дата']))

firstDay = days['date'].min()
days = days.assign(days_amount = (days['date'] - days['date'].min()).dt.days)

x_train, x_test, y_train, y_test = train_test_split(days[['days_amount']], days['Продажи'], random_state=0)

reg = linear_model.LinearRegression()
reg.fit(x_train, y_train)
score = reg.score(x_test, y_test)
tomorrow = (datetime.now() + timedelta(days=1) - firstDay).days
#print(f"Sales tomorrow: {reg.predict(pd.DataFrame([[tomorrow]], columns=['days_amount']))[0]:.1f}")
"""
#------------------------------------------------------------------------



"""
df['month'] = df['Год-мес'] % 100

plt.figure(figsize=(7, 4))
data = df[['month', 'Продажи']].groupby('month').sum().reset_index()
plt.plot(data['month'], data['Продажи'])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
"""



"""
df['month'] = pd.to_datetime(df['FLIGHT_DATE_LOC']).dt.month

days = df.groupby('ISSUE_DATE')['ORIG_CITY_CODE'].count().reset_index()
days = days.assign(date=pd.to_datetime(days['ISSUE_DATE']))

firstDay = days['date'].min()
days = days.assign(days_amount = (days['date'] - days['date'].min()).dt.days)

x_train, x_test, y_train, y_test = train_test_split(days[['days_amount']], days['ORIG_CITY_CODE'], random_state=0)

reg = linear_model.LinearRegression()
reg.fit(x_train, y_train)
score = reg.score(x_test, y_test)
#tomorrow = datetime.now() + timedelta(days=1)
tomorrow = (datetime.now() + timedelta(days=1) - firstDay).days
print(f"Flights tomorrow: {reg.predict(pd.DataFrame([[tomorrow]], columns=['days_amount']))[0]//1}")
print(f"Accuracy: {score*100:.2f}")

"""
