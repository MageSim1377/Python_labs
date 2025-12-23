import numpy as np


lengths = "20 8 9 18 5 12 16 16 6 7"
velocities = "44 70 44 66 46 38 38 37 66 67"
k = 4
p = 7


lenArr = np.array(list(map(float, lengths.split())))
velArr = np.array(list(map(float, velocities.split())))


#print(len(lenArr))
#print(lenArr)
passedWay = lenArr[k:p+1]
t = (passedWay / velArr[k:p+1]).sum()



print(f"S = {passedWay.sum()} km")
print(f"T = {t} h")
print(f"V = {passedWay.sum()/t} km/h")