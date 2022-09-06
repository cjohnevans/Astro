import numpy as np
from astropy.time import Time
from datetime import datetime

t_dt = datetime(2021,10,11)
print(t_dt)
t2 = Time(t_dt)
print(t2)
print(t2.jd)
