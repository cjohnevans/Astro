#plotlightcurve
# original version - based on BAA database
# paths will need to be updated

import os
import csv

inpath = 'C:\\Users\\cjohn\\OneDrive\\Astronomy\\variablestars\\data'
os.chdir(inpath)
os.listdir(os.getcwd())
infile = 'V1405_Cas_20210610_195550.csv'

print(inpath + '\\' + infile)

row = 0
csvdata = ''

with open(inpath + '\\' + infile) as csvfile:
    csvdata[row] = csv.reader(csvfile, delimiter=',')

print(csvdata[0])

#for row in csvdata:
#    print(row)


