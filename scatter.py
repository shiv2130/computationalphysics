import matplotlib.pyplot as plt
import numpy as np 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 7, 8, 9, 11, 13,]
plt.scatter(x, y, marker= "*", color = 'r')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("SCATTER PLOT")
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(min(y), max(y)+1, 1.0))
plt.show()