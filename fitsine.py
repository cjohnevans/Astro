# fitsine
# 26/6/20.  got doublesin fn working with tuples.  need to implement fitting with double sines.

import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

def sin_fit(x, amplitude, period, offset, phase):
    return offset + amplitude * np.sin(  2* np.pi * (x + phase) / period)

def doublesinfit(x, amplitude, period, offset, phase):
    sin1= sin_fit(x,  amplitude[0], period[0], offset[0], phase[0])
    sin2= sin_fit(x,  amplitude[1], period[1], offset[1], phase[1])
    return sin1+sin2

x0 = np.arange(0.0, 100, 0.5)

sinx0 = sin_fit(x0, 2, 20, 0, 0)
doublesin=doublesinfit(x0, (1.0,2.0), (10.0, 100.0), (0,0), (0,0))

ub = (np.inf, np.inf, np.inf, 2*np.pi)
lb = (-np.inf, -np.inf, -np.inf, 0)

params, params_cov = optimize.curve_fit(sin_fit, \
                                        x0, \
                                        sinx0, \
                                        p0=[0.1, 20, 0, 0], \
                                        bounds=(lb,ub))
print(params)

sinx0fit = sin_fit(x0, params[0], params[1], params[2], params[3])

#plt.plot(x0, sinx0, 'bo', x0, sinx0fit, 'r')
plt.plot(x0, doublesin)
plt.show()
