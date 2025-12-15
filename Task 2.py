import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 5/(x**2 - 9)


plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis([-15, 15, -10, 10])

x = np.linspace(-10, 10, 100)
y = list(map(f, x))

plt.plot(x, y)

plt.show()