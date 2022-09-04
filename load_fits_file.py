# based on AAVSO webinar on Python for astronomy (3/9/2022)
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits  
#import astroquery

print('hello')

#fitsfile = fits.open('WFPC2u5780205r_c0fx.fits') # need to take the zeroth version of hdu.data for this to work
fitsfile = fits.open('502nmos.fits')

# doesn't echo anything to screen
# fits files are collections of headers and datasets
# fitsfile is a list of "HDU" objects = Header Data Unit

print(type(fitsfile))

#need to pull out HDU object
hdu = fitsfile[0]
for key, value in hdu.header.items():
    print(key, value)
#print(hdu.header['OBJECT']) #doesn't work for this example
#print(hdu.header['TELESCOP'])

print(hdu.data)
print(hdu.data.shape) #work out data size
average_value = np.mean(hdu.data[0])
#set the contrase
black_point = 10.0 * average_value
white_point = 1000.0 * average_value

plt.imshow(hdu.data) 
#plt.imshow(hdu.data, vmin = black_point, vmax=white_point, cmap='Greys') #its got >1 image, plot the fist 
plt.title(hdu.header['ORIGIN']) 
plt.show()


print("done")
