import numpy as np
import scipy.integrate as integrate


integr = integrate.quad(lambda x: np.exp(-(x**2)), -100, 100)[0]
print("Squared ntegral from e**-x**2 at [-100, 100] =", integr**2)


twoIntegr = integrate.dblquad(lambda x, y: 1, -1, 1, lambda x: -np.sqrt(1 - x**2), lambda x: np.sqrt(1 - x**2))[0]

print("Square of circle with center at point [0, 0] and radius = 1 =", twoIntegr)