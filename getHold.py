import requests
import time

headers = {'Accept': 'application/ld+json'}
xl_url = 'https://libris.kb.se/_findhold?id=https://libris.kb.se/'
old_url = 'https://libris.kb.se/_findhold?id=http://libris.kb.se/bib/'

def getHold(fil):

	holds = []

	with open(fil, 'r') as list: 
		lista = list.read().splitlines()
	list.closed
	True

	for bib in lista: 
		url = xl_url + bib + '&library=https://libris.kb.se/library/D'
		response = requests.get(url, headers = headers)
		if(response.status_code) != 200:
			url = old_url + bib + '&library=https://libris.kb.se/library/D'
			response = requests.get(url, headers=headers)
		stri = response.content.replace('[\"https://libris.kb.se/', "")
		stri = stri.replace('\"]', "")
		if(stri != "[]"):
			holds.append(stri)
			
	return holds
	
