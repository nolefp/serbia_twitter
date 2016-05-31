from pyquery import PyQuery as pq
import pandas as pd 
import requests

link = 'http://www.mc.rs/stampani-mediji---dnevne-novine-nedeljnici-magazini.16.html'
page_req = requests.get(link)

page_ = pq(page_req.text)

page_right = page_('div#contentRight')

i = 0
for par in page_right('table')('p').items():


	print i 
	i += 1
	print par
	if i == 1:
		break
