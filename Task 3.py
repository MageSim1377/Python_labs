import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(figsize=(5, 5))

ax.axis('off')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

mainColor = '#999999'

ax.add_patch(patches.Circle((0, 0), 3, color=mainColor))

ax.add_patch(patches.Polygon([(0, -2.9), (-5.2, -3.2), (-6.5, -0.6), (0, 2)], closed=True, facecolor=mainColor))

ax.add_patch(patches.Polygon([(0, 0), (-0.5, 5), (0.8, 4.6), (1.4, 3.8), (2, 3.1), (2.5, 1.5), (3, 0)], closed=True, facecolor=mainColor))

ax.add_patch(patches.Polygon([(-6.04, -1.59), (-6.5, -0.6), (-5.7, -0.3), (-5.7, -1.2)], closed=True, facecolor='#000000'))

ax.add_patch(patches.Polygon([(-5.5, -2.5), (-4.8, -2.2), (-2.2, -2.09), (-4.8, -2.34), (-5.45, -2.63)], closed=True, facecolor='#000000'))

ax.add_patch(patches.Polygon([(-1.9, 0.82), (-1.3, 1.51), (0.11, 1.61), (-1.3, 1.45)], closed=True, facecolor='#000000'))

ax.add_patch(patches.Polygon([(-1.3, 1.48), (-1.25, 1.15), (-1.1, 1.0), (-1.05, 1.25)], closed=True, facecolor='#FFFFFF'))

ax.add_patch(patches.Polygon([(-5.5, -1.76), (-2, -1.76), (-2, -1.86), (-5.5, -1.86)], closed=True, facecolor='#000000'))
ax.add_patch(patches.Polygon([(-5.5, -1.76), (-2, -1.96), (-2, -2.06), (-5.5, -1.86)], closed=True, facecolor='#000000'))


plt.show()