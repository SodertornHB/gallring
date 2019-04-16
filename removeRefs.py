import requests
import json
import time

auth_token = 'KCwR7Wix0QMSkv1BeAvIJb7cfqwrXc'
lyckadfil = open('modifieradeposter.txt', 'w')
misslyckadfil = open('misslyckadeposter.txt', 'w')
lyckadfil.writelines("Modifierade")
misslyckadfil.writelines("Misslyckade")

def removeRefs(postlista):
	url = 'https://libris.kb.se/'
	for post in postlista:
		headers = {'Accept': 'application/ld+json', 'Content-Type': 'application/ld+json', 'Authorization': 'Bearer ' + auth_token, 'XL-Active-Sigel': 'D'}
		url = url + post
		response = requests.get(url, headers=headers)
		print "Svar: " + str(response)
		json_body = response.json()
		etag = response.headers['etag'].strip('"').strip('gzip')
		etag = etag[0:len(etag)-1]
		#print etag 
		print json_body
		headers = {'Content-Type': 'application/ld+json', 'Authorization': 'Bearer ' + auth_token, 'If-Match': etag,  'XL-Active-Sigel': 'D'}
		try: 
			print "RefK kommer tas bort.."
			del json_body['@graph'][1]['physicalLocation'] 
			data = json.dumps(json_body)
			response = requests.put(url, data, headers = headers)
			print response
			lyckadfil.writelines("\n" + url)
		except: 
			print "Ingen Refk hos denna"
			misslyckadfil.writelines("\n" + url)
		url = 'https://libris.kb.se/'
		response = ""
