import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return 1/(1 + np.exp(-x))

x = np.linspace(-5, 5, 100)
y = sigmoid(x)
  
plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("Sigmoid(X)")

plt.ylim(0, 1)

plt.show()