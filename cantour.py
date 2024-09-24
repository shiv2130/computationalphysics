import matplotlib.pyplot as plt 
import numpy as np 
feature_X = np.linspace(0, 3.0, 30)
feature_Y = np.linspace(0, 3.0, 30)
[X, Y] = np.meshgrid(feature_X, feature_Y)
Z = X**2 + Y**2
plt.contourf(X, Y, Z) #contour fill for filling the plot
plt.show()