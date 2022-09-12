import numpy as np
from astropy.time import Time
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def get_year_jd(year_span):
    year_val = []
    jd_val = []
    for yy in year_span:
        print(yy)
        t_dt = datetime(int(yy),1,1)
        t_astro = Time(t_dt)
        #print(t_astro.decimalyear, t_astro.jd)
        year_val.append(t_astro.decimalyear)
        jd_val.append(t_astro.jd)
    return (year_val, jd_val)

def plot_year_jd(year_val, jd_val, lo, hi, step):
    fig, ax = plt.subplots()
    plt.plot(year_val, jd_val)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.xticks(year_val)
    plt.yticks(np.arange(lo, hi, step))
    plt.grid(axis='both')
    ax.tick_params(axis='x', labelrotation=90)
    plt.ylabel('JD')
    plt.xlabel('year')    
    
yr_span = np.arange(1900, 2040, 10.0)
yr_span_short = np.arange(2000,2026,1.0)
print(yr_span)
print(yr_span_short)


(year_val_1, jd_val_1) = get_year_jd(yr_span)
print(year_val_1)
plot_year_jd(year_val_1, jd_val_1, 2410000, 2465000, 5000)
    
(year_val_2, jd_val_2) = get_year_jd(yr_span_short)
plot_year_jd(year_val_2, jd_val_2, 2451000, 2461000, 500)
print(year_val_2)
plt.show()


    
