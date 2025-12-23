import numpy as np


a = np.random.randint(40, 60, size=12)

print(a)

if a[1:8].sum() > a[9:12].sum() + a[0]:
    print('Summer is more expensive')
else:
    print('Winter is more expensive')

#print(a[a == np.max(a)])

#print("The most expensive months", np.sort(np.where(a == np.max(a))))
#print("The most expensive months", np.sort(a, -1)[::-1])
#print("The most expensive months", np.argsort(a)[::-1])
print("The most expensive months", np.argsort(a)[::-1][:a[a == np.max(a)].size] + 1)