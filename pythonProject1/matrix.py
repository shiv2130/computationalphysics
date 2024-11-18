import numpy as np
m1= np.array([[1, 2, 1], [2, 2, 3], [-1, -3, 0]])
m2 = np.array([0, 0, 2])
print(m1.ndim)
print(m2.ndim)
print(np.linalg.solve(m1, m2))
