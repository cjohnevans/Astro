# readbaadbase
# read csv file from baa database
# need to change x base to days (from start) not JD.

import csv
import matplotlib.pyplot as plt
import numpy as np

vssdir='/home/john/astro/variable_star_data'
#vssfile='Z UMA_20210619_100143.csv'
#vssfile='AH DRA_20210621_221943.csv'
#vssfile='AH DRA_test.csv'
#vssfile = 'Z UMA_20210626_235405.csv'
vssfile = 'Z UMA_20220912_201610.csv'
starname=vssfile.split('_')[0]
print(starname)
vssfullpath = vssdir + '/' + vssfile

jd = []
mag = []

#using the (large) JD as x axis makes fitting unstable in period?
# use days relative to first measurement instead
jdmodifier = 00000.0  #discard first N digits of jd here

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
ax1.plot(jd, mag, '.')
ax1.set_title(starname)

plt.show()
     
         
