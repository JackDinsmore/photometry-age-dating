# Code obtained from https://adina.feinste.in/eleanor/getting_started/tutorial.html

from IPython.display import Image

import warnings
warnings.filterwarnings('ignore')


import eleanor
import numpy as np
from astropy import units as u
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord

STAR_TIC = 38846515
STAR_SECTOR = 1
# TIC stands for Tycho Input Catalog.
# (STAR_TIC, STAR_SECTOR) = (38846515, 1) stands for WASP-100.


'''star = eleanor.Source(tic=STAR_TIC, sector=STAR_SECTOR)# Removing the sector argument will use the sector most recently observed.

print('Found TIC {0} (Gaia {1}), with TESS magnitude {2}, RA {3}, and Dec {4}'
     .format(star.tic, star.gaia, star.tess_mag, star.coords[0], star.coords[1]))'''

star = eleanor.Source(name='WASP-100', sector=1)

print('Found TIC {0} (Gaia {1}), with TESS magnitude {2}, RA {3}, and Dec {4}'
    .format(star.tic, star.gaia, star.tess_mag, star.coords[0], star.coords[1]))



'''
All equivalent:
star = eleanor.Source(name='WASP-100', sector=1)

print('Found TIC {0} (Gaia {1}), with TESS magnitude {2}, RA {3}, and Dec {4}'
    .format(star.tic, star.gaia, star.tess_mag, star.coords[0], star.coords[1]))

coords = (68.959732, -64.02704)
# or
coords = SkyCoord(ra=68.959732, dec=-64.02704, unit=(u.deg, u.deg))

star = eleanor.Source(coords=coords, sector=1)

print('Found TIC {0} (Gaia {1}), with TESS magnitude {2}, RA {3}, and Dec {4}'
    .format(star.tic, star.gaia, star.tess_mag, star.coords[0], star.coords[1]))

star = eleanor.Source(gaia=4675352109658261376, sector=1)

print('Found TIC {0} (Gaia {1}), with TESS magnitude {2}, RA {3}, and Dec {4}'
    .format(star.tic, star.gaia, star.tess_mag, star.coords[0], star.coords[1]))
'''


# Target the data to one star by removing systematic errors. 
data = eleanor.TargetData(star, height=15, width=15, bkg_size=31, do_psf=True, do_pca=True)


# Plot data.
plt.figure(figsize=(15,5))

q = data.quality == 0

plt.plot(data.time[q], data.raw_flux[q]/np.nanmedian(data.raw_flux[q])+0.06, 'k')# Black: Raw data
plt.plot(data.time[q], data.corr_flux[q]/np.nanmedian(data.corr_flux[q]) + 0.03, 'r')# Red: corrected
plt.plot(data.time[q], data.pca_flux[q]/np.nanmedian(data.pca_flux[q]), 'g')# Green: PCA light curve (Principal Components Analysis)
plt.plot(data.time[q], data.psf_flux[q]/np.nanmedian(data.psf_flux[q]) - 0.02, 'b')# PSF modeled light curve (Point Spread Function). Burring / spreading of the image due to brightness.
plt.ylabel('Normalized Flux')
plt.xlabel('Time [BJD - 2457000]')
plt.title('WASP-100')
plt.show()


print("Background model:" + str(data.bkg_type))


# Plot background as a function of time to see what was removed. I think the spikes are orientation changes.
plt.figure(figsize=(15,5))

plt.plot(data.time, data.flux_bkg, 'k', label='1D postcard', linewidth=3)
plt.plot(data.time, data.tpf_flux_bkg, 'r--', label='1D TPF', linewidth=2)
plt.ylabel('Normalized Flux')
plt.xlabel('Time [BJD - 2457000]')
plt.legend()
plt.show()



# Plot 2D background; other stars.
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,4))
ax1.imshow(data.tpf[0])
ax1.set_title('Target Pixel File')
ax2.imshow(data.bkg_tpf[0])
ax2.set_title('2D interpolated background')
plt.show()



# Plot automatically chosen aperture
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,4))
ax1.imshow(data.tpf[0])
ax1.set_title('Target Pixel File')
ax2.imshow(data.aperture)
ax2.set_title('Aperture')
plt.show()


data.save()



# Plot the light curve.
lk = data.to_lightkurve()
lk.plot()