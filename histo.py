import matplotlib.pyplot as plt 
import numpy as np
ages = [2, 5, 70, 30, 45, 50, 45, 43, 40, 44, 60, 7, 13, 57, 18, 90, 77, 32, 21, 20, 40,81,92]
range = (0, 100)
bins = 10
plt.hist(ages, bins, range, edgecolor = "Black", )
plt.xlabel("Age")
plt.ylabel("No. of people")
plt.title("My Histogram")
plt.xticks(np.arange(1, 100, 5))
plt.show() 