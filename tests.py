import requests
from sunpy.net import Fido, attrs as a

result = Fido.search(a.Time('2012/3/4', '2012/3/6'), a.Instrument('HMI'))

some_results=result[0,0:12]
downloaded_files = Fido.fetch(some_results, path='/home/sarah/sun-stuff/data/{file}.fits')
