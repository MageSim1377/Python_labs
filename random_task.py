from faker import Faker
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


fake = Faker("ru_RU")

def generate_cake(name):
    cake = {
        #'name': fake.random_element(elements=['Красный бархат', 'Киевский', 'Очень вкусный', 'Просто вкусный']),
        'name': name,
        'mass': fake.random_int(1, 100) / 10,
        'price_per_kg': fake.random_int(10, 40),
        'produced': fake.random_int(20, 200),
        
    }
    cake['sold'] = fake.random_int(20, cake['produced'])
    #cake['price'] = cake['price_per_kg'] * cake['mass']
    # cake['remainder'] = cake['produced'] - cake['sold']
    # cake['full_realisation_volume'] = float(cake['sold'] * cake['price'])

    return cake

names = ['Красный бархат', 'Киевский', 'Очень вкусный', 'Просто вкусный', 'Повседневный']
cakes = [generate_cake(name) for name in names]

df = pd.json_normalize(cakes)

print(df.head(5))

df = (df.assign(price=df['price_per_kg'] * df['mass'])
      .assign(remainder=df['produced'] - df['sold'])
      .assign(full_realisation_volume=lambda x: (x['sold'] * x['price'])))

print(df.head(5))




fig, ax = plt.subplots(2, 2, figsize=(15, 10))

axes = np.ravel(ax)

data = df[['name', 'full_realisation_volume']]
axes[0].pie(
    data['full_realisation_volume'],
    labels=data['name'],
    autopct='%1.1f%%'
)
axes[0].set_title('Full realisation volume')


data = df[['name', 'remainder']]
axes[1].bar(
    data['name'],
    data['remainder']
)
axes[1].set_title('Remainder')


data = df[['name', 'produced', 'sold']]
w = 0.4
x = np.arange(len(data))
axes[2].bar(
    x - w/2,
    data['produced'],
    width = w,
    color='blue'
)
axes[2].bar(
    x + w/2,
    data['sold'],
    width = w,
    color = 'red'
)
axes[2].set_xticks(x)
axes[2].set_xticklabels(data['name'])
axes[2].set_title('Produced')


data = df[['name', 'price_per_kg']]
axes[3].bar(
    data['name'],
    data['price_per_kg']
)
axes[3].set_title('Price per kg')


plt.show()