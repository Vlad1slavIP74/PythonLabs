import numpy as np
import matplotlib.pyplot as plt
import math
v = 0, 1

print(v)


M = [
    [math.cos(math.pi), -math.sin(math.pi)],
    [math.sin(math.pi), math.cos(math.pi)]
]

vs = [v]

for i in range(100):
    v = np.matmul(vs[i], M) * 0.99
    vs.append(v)
    
vs = np.array(vs)
plt.figure(figsize=(6, 6))
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.plot(*vs.T)
plt.show()