#  requires 'astro' conda environment (on deneb)
#loading a light curve from the aavso from the database
# recommend - no discrepant data (judged to be outliners), no diff and step data and csv files.

import matplotlib.pyplot as plt
import numpy as np
from astropy.table import Table
import os

data_dir = '/home/john/astro/variable_star_data'
#lightcurve_file = 'aavsodata_v1405cas_20220903.csv'
lightcurve_file = 'aavsodata_txdra_20220904.csv'
lightcurve_path = os.path.join(data_dir, lightcurve_file)
#chart_title = 'V1405 Cas'
chart_title = 'TX Dra'

data = Table.read(lightcurve_path, encoding='UTF-8')
print(data.colnames)

#watch out - Magnitude gets interpreted as TEXT due to the 'fainter thans'
rows_to_remove = []
for observation in data:
    #print(observation['Star Name'])
    if '<' in observation['Magnitude']:
        rows_to_remove.append(observation.index)
# remove rows with text
print(rows_to_remove)
data.remove_rows(rows_to_remove)

data['Magnitude'] = [float(mag) for mag in data['Magnitude']]
#    else:
#        observation['Magnitude'] = float(observation['Magnitude'])
#    print(type(observation['Magnitude']))

plt.scatter(data['JD'], data['Magnitude'], marker='.')
plt.gca().invert_yaxis()
plt.title(chart_title)
plt.show()
