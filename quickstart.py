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

eleanor.TargetData()# Chooses an aperture which optimizes the light curve for transit searches

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