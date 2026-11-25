import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(0.1, 8.1, 81)
y = np.zeros(81)

for i in range(0, 81, 1):
    y[i] = 1 / x[i] + 2.4 * math.exp(x[i])

plt.plot(x, y, 'g--', label='y=1/x+2,4e^x')

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('Графік функції')
plt.legend()

plt.savefig('image.png', dpi=400)
plt.show()