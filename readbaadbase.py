# readbaadbase
# read csv file from baa database
# need to change x base to days (from start) not JD.

import csv
import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

vssdir='C:\\Users\\cjohn\\OneDrive\\Astronomy\\variablestars\\data_baa'
#vssfile='Z UMA_20210619_100143.csv'
#vssfile='AH DRA_20210621_221943.csv'
#vssfile='AH DRA_test.csv'
vssfile = 'Z UMA_20210626_235405.csv'
starname=vssfile.split('_')[0]
print(starname)
vssfullpath = vssdir + '\\' + vssfile

jd = []
mag = []

#using the (large) JD as x axis makes fitting unstable in period?
# use days relative to first measurement instead
jdmodifier = 2400000.0  #discard first N digits of jd here

with open(vssfullpath) as csvfile:
    baaread = csv.DictReader(csvfile, delimiter=',')
    for row in baaread:
#        print(row['Julian Date'], row['Magnitude'])
        jd.append(float(row['Julian Date'])-jdmodifier)
        mag.append(float(row['Magnitude']))


time_day = np.array(jd)
time_day = time_day - time_day[-1]

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_ylabel('Mag.')
ax1.set_xlabel('time (days)')
ax1.plot(time_day, mag, '.')
ax1.set_title(starname)
fig.show()

def sin_fit(x, amplitude, period, offset, phase):
    return offset + amplitude * np.sin(  2* np.pi * (x + phase) / period)

ub = (np.inf, np.inf, np.inf, 100)
lb = (0, 0, 0, 0)

#ub = (np.inf, np.inf, np.inf, 2*np.pi)
#lb = (-np.inf, -np.inf, -np.inf, 0)

#params, params_cov = optimize.curve_fit(sin_fit, jd, mag, p0=[1, 20, 8, 0])
params, params_cov = optimize.curve_fit(sin_fit, \
                                        time_day, \
                                        mag, \
                                        p0=[2, 200, 8, 50], \
                                        bounds=(lb,ub))
print(params)

ax1.plot(time_day, sin_fit(time_day, amplitude = params[0], period = params[1],
                     offset = params[2], phase = params[3]))
         
         
