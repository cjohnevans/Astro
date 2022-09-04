# astroquery - remote query if astronomy data from online repositories
#  e.g https://vizier.u-strasbg.fr/viz-bin/Vizier
#  requires 'astro' conda environment (on deneb)

from astroquery.vizier import Vizier
from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import astropy.units as  u
import matplotlib.pyplot as plt

Vizier.ROW_LIMIT = -1  # gaia has a limit on the number of rows returned.  This turns it off


catalog_id = "I/355/gaiadr3"

result = Simbad.query_object("NGC 7789")
print(result)
target_coord = SkyCoord(result['RA'], result['DEC'], unit=(u.hourangle, u.deg))

# can probably query vizier with object name too
gaia_result = Vizier.query_region(target_coord, radius=0.2*u.deg, catalog=catalog_id)
gaia_data = gaia_result[0]

print(gaia_data.colnames)

plt.scatter(gaia_data['BP-RP'], gaia_data['Gmag'])
plt.show()
