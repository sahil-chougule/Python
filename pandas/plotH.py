import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D", "e"])
y = np.array([3, 8, 10, 10, 18])
plt.barh(x, y)
plt.show()