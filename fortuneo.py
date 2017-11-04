import urllib.request
import ssl
import json
from bs4 import BeautifulSoup

i = 1
'''
while True:
    url = "http://bourse.fortuneo.fr/api/sicav/search/?additionalParams=%7B%22ftnVie%22:%22true%22,%22view%22:%22VUE_PERF%22%7D&page=" + str(i)
    req = urllib.request.urlopen(url, context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
    jsonData = json.load(req)

    if jsonData['array']['data']:
        print("avec" + str(i))
        for elemtab in jsonData['array']['data']:
        #    for elem in elemtab:
        #        print("test" + elem)
            print("test" + elemtab[0])
        i = i+1
    else:
        break
'''
url = "http://bourse.fortuneo.fr/sicav-fonds/cours-aaa-actions-agro-alimentaire-c-FR0010058529-26"
req = urllib.request.urlopen(url, context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
soup = BeautifulSoup(req, 'html.parser')
print(soup.find('span', class_="header-devise").contents)
print(soup.find('div', class_="content-date").contents[3].contents)
