import requests
import time

auth_token = ''#din token
headers = {'Authorization': 'Bearer ' + auth_token, 'XL-Active-Sigel': 'D'}
fil = open('raderadeposter.txt', 'w')
fil.writelines("Raderat")

def testaPost(post):
	print "Denna hade raderats..: " + post
	url = 'https://libris.kb.se/' + post
	print "..med ett DELETE-anrop mot denna URL:" + url

def raderaPoster(postlista):
	url = 'https://libris.kb.se/'
	for post in postlista:
		url = url + post
		print "Raderar.. " + url
		fil.writelines("\n" + url)
		time.sleep(1)
		response = requests.delete(url, headers=headers)
		url = 'https://libris.kb.se/'
	fil.close()