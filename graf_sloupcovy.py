import matplotlib.pyplot as plt
import numpy as np

x = np.array(["8/21", "9/21", "10/21", "11/21", "12/21", "1/22", "2/22", "3/22", "4/22", "5/22", "6/22", "7/22"])
y = np.array([8783586, 9762615, 10785799, 11801999, 12820193, 1812809, 2814113, 3812873, 4844713, 5857793, 6823650, 7893379])

plt.bar(x,y)
plt.show()