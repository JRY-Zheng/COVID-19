import numpy as np
import matplotlib.pyplot as plt

R0 = np.linspace(1,3,101)
n0 = 1-(1+np.log(R0))/R0

plt.plot(R0, n0)
plt.xlabel('Basic reproduction number')
plt.ylabel('Beds in need per person')
plt.grid()
plt.savefig('R0-n0.png')
plt.close()