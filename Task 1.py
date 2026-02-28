import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.exp(np.cos(np.radians(x))) + np.log((np.cos(np.radians(x)))**2 + 1) * np.sin(np.radians(x))


def h(x):
    return -np.log((np.cos(np.radians(x)) + np.sin(np.radians(x)))**2 + 2.5) + 10  


plt.xlabel("X")
plt.ylabel("Y")
plt.title("Plots of some trigonometric functions")
plt.axis([-400, 400, -15, 15])
plt.grid(True)


x = np.linspace(-360, 360, 360)
y1 = list(map(f, x))

y2 = list(map(h, x))


#print(y)


plt.plot(x, y1, color="blue")
plt.plot(x, y2, color="red")


plt.show()


#print("I'm here!")