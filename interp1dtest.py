#interp1d test
from scipy.interpolate import interp1d
import  numpy as np

x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')

xnew = np.linspace(0, 10, num=41, endpoint=True)
import matplotlib.pyplot as plt

print(type (f(xnew)))
y_interp = f2(xnew)

plt.plot(x, y, 'o', xnew, y_interp, 'x')
plt.legend(['data', 'linear'])
plt.show()

