import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from datetime import datetime, timedelta

df = pd.read_excel('s7_data_sample_rev4_50k.xlsx')

fig, ax = plt.subplots(figsize=(7, 7))
#((airports, dates), (onlineMethod, offlineMethod))
print(df.head())
#print(df.describe())

#df.fillna('Not FFP', inplace=True)
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
data = df[['FFP_FLAG', 'REVENUE_AMOUNT']].groupby('FFP_FLAG').sum().reset_index()
print(data.head(5))
ax.bar(data['FFP_FLAG'], data['REVENUE_AMOUNT'])
ax.set_title('Revenue from FFP and not FFP, $')

airportsData = df.groupby(['ORIG_CITY_CODE']).size().reset_index(name='count').sort_values('count', ascending=False)[:20]
airportsOtherData = df.groupby(['DEST_CITY_CODE']).size().reset_index(name='count').sort_values('count', ascending=False)[:20]
w = 0.4
x = np.arange(len(airportsData['ORIG_CITY_CODE']))
airports.bar(x - w/2, airportsData['count'], width=w, color='red', label='Departure')
airports.bar(x + w/2, airportsOtherData['count'], width=w, color='blue', label='Destination')
airports.set_title("Most frequent airports", loc='center')
airports.set_xticks(x, airportsData['ORIG_CITY_CODE'])
airports.set_xticklabels(airportsData['ORIG_CITY_CODE'], rotation=90, ha='center', fontsize=6)
airports.legend(ncols=2)

#print(df['FLIGHT_DATE_LOC'].dtypes)
df['month'] = pd.to_datetime(df['FLIGHT_DATE_LOC']).dt.month
dateData = df.groupby('month').sum().reset_index()
dates.bar(dateData['month'], dateData['REVENUE_AMOUNT'])
dates.set_title("Flights per month statistics, $", loc='center')

online = df[df['SALE_TYPE'] == 'ONLINE'][['month', 'SALE_TYPE']].groupby('month').size().reset_index(name='count')
offline = df[df['SALE_TYPE'] == 'OFFLINE'][['month', 'SALE_TYPE']].groupby('month').size().reset_index(name='count')
print('\n')
print(online['count'].describe())
print('\n')
print(offline['count'].describe())
#online = airportsData[airportsData['SALE_TYPE'] == 'ONLINE'].groupby('ORIG_CITY_CODE').size().reset_index(name='count')
#offline = airportsData[airportsData['SALE_TYPE'] == 'OFFLINE'].groupby('ORIG_CITY_CODE').size().reset_index(name='count')
#print(online)
onlineMethod.bar(online['month'], online['count'])
offlineMethod.bar(offline['month'], offline['count'])
onlineMethod.set_xticklabels(online['month'], rotation=90, ha='center', fontsize=10)
offlineMethod.set_xticklabels(offline['month'], rotation=90, ha='center', fontsize=10)
onlineMethod.set_title("Online", loc='center')
offlineMethod.set_title("Offline", loc='center')
onlineMethod.set_ylim(0, 4500)
offlineMethod.set_ylim(0, 4500)
"""


#plt.show()

