import matplotlib.pyplot as plt
import numpy as np
y1 = [1, 2, 3, 4]
y2 = [1, 2, 3, 4]
tick_label = ["one", "two", "three", "four"]
plt.bar(np.arange(len(y1))-0.2, y1, tick_label = tick_label, width=0.4)
plt.bar(np.arange(len(y2))+0.2, y2, tick_label = tick_label, width=0.4)
plt.title("My bar chart")
plt.legend(labels = ['a', 'b'])
plt.show()