import matplotlib.pyplot as plt
import numpy as np
from astropy.table import Table  
#import astroquery

#loading a light curve from the aavso from the database
# recommend - no discrepant data (judged to be outliners), no diff and step data and csv files.

lightcurve_file = 'aavsodata_v1405.csv'

data = Table.read(lightcurve_file, encoding='UTF-8')
print(data.colnames)

#watch out - Magnitude gets interpreted as TEXT due to the 'fainter thans'
rows_to_remove = []
for observation in data:
    if '<' in observation['Magnitude']:
        rows_to_remove.append(observation.index)
# remove rows with text
print(rows_to_remove)
data.remove_rows(rows_to_remove)

data['Magnitude'] = [float(mag) for mag in data['Magnitude']]
#    else:
#        observation['Magnitude'] = float(observation['Magnitude'])
#    print(type(observation['Magnitude']))

plt.scatter(data['JD'], data['Magnitude'])
plt.gca().invert_yaxis()
plt.title('V1405 Cas')
plt.show()
