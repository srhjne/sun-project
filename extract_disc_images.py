import requests
from sunpy.net import Fido, attrs as a
from astropy.units import cds
from astropy import units as u

result = Fido.search(a.Time('2014/7/1', '2014/12/31'), a.Instrument('AIA'), a.Wavelength(171*cds.AA), a.vso.Sample(1*u.day))

print result


downloaded_files = Fido.fetch(result, path='/media/sarah/SAMSUNG/ml_sun_images/{file}.fits')
