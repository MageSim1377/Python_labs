import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('s7_data_sample_rev4_50k.xlsx')

fig, ((airports, dates), (onlineMethod, offlineMethod)) = plt.subplots(2, 2, figsize=(10, 7))

print(df.head())
print(df.describe())

airportsData = df.groupby(['ORIG_CITY_CODE']).size().reset_index(name='count').sort_values('count', ascending=False)[:20]
airportsOtherData = df.groupby(['DEST_CITY_CODE']).size().reset_index(name='count').sort_values('count', ascending=False)[:20]
w = 0.4
x = np.arange(len(airportsData['ORIG_CITY_CODE']))
airports.bar(x - w/2, airportsData['count'], width=w/2, color='red')
airports.bar(x + w/2, airportsOtherData['count'], width=w/2, color='blue')
airports.set_title("Most frequent airports", loc='center')
airports.set_xticks(x, airportsData['ORIG_CITY_CODE'])
airports.set_xticklabels(airportsData['ORIG_CITY_CODE'], rotation=90, ha='center', fontsize=10)

#print(df['FLIGHT_DATE_LOC'].dtypes)
df['month'] = pd.to_datetime(df['FLIGHT_DATE_LOC']).dt.month
dateData = df.groupby('month').size().reset_index(name='count')
dates.bar(dateData['month'], dateData['count'])
dates.set_title("Flights per month statistics", loc='center')

online = df[df['SALE_TYPE'] == 'ONLINE'][['month', 'SALE_TYPE']].groupby('month').size().reset_index(name='count')
offline = df[df['SALE_TYPE'] == 'OFFLINE'][['month', 'SALE_TYPE']].groupby('month').size().reset_index(name='count')
#online = airportsData[airportsData['SALE_TYPE'] == 'ONLINE'].groupby('ORIG_CITY_CODE').size().reset_index(name='count')
#offline = airportsData[airportsData['SALE_TYPE'] == 'OFFLINE'].groupby('ORIG_CITY_CODE').size().reset_index(name='count')
#print(online)
onlineMethod.bar(online['month'], online['count'])
offlineMethod.bar(offline['month'], offline['count'])
onlineMethod.set_xticklabels(online['month'], rotation=90, ha='center', fontsize=10)
offlineMethod.set_xticklabels(offline['month'], rotation=90, ha='center', fontsize=10)
onlineMethod.set_title("Online", loc='center')
offlineMethod.set_title("Offline", loc='center')



plt.show()