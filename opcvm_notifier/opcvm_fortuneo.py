import urllib.request
import ssl
import json
import opcvm_notifier.opcvm
from bs4 import BeautifulSoup

class OpcvmFortuneo:

    def __init__(self):
        self._BASE_URL = "http://bourse.fortuneo.fr/api/sicav/search/?additionalParams=%7B%22ftnVie%22:%22true%22,%22view%22:%22VUE_PERF%22%7D&page="

    def get_base_url(self):
        return self._BASE_URL

    def get_list_opcvm(self):
        list_opcvm_fortuneo = []
        page = 1

        while True:
            req = urllib.request.urlopen(self.get_base_url() + str(page), context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
            json_data = json.load(req)

            if json_data['array']['data']:
                for elemtab in json_data['array']['data']:
                    soup = BeautifulSoup(elemtab[0], 'html.parser')
                    a_tag = soup.find("a")
                    list_opcvm_fortuneo.append(opcvm_notifier.opcvm.Opcvm(str(a_tag.get('title')), str(a_tag.get('href'))))

                page = page+1
            else:
                break

        return list_opcvm_fortuneo


req = urllib.request.urlopen("https://services.opcvm360.com/api-v1/fundshares?fundshares=63420340,16560,19440,2423,63424605,3621,5018,3748,7571,12631,20521,3357,16589,19955,7939,19846,26219,63422586,63408909,16357,16618,8172&fields=isin,idFund,srri,name,varPYTD,varP1Y,varP3Y,varP5Y&apiKey=b0b645dc2b704ae3ec14", context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
json_data = json.load(req)
if json_data['data']:
    for elemtab2 in json_data['data']:
        print(elemtab2)

'''
test = OpcvmFortuneo()
opcvmlist = test.get_list_opcvm()
#for opcvm in opcvmlist:
#    print(opcvm.get_name())
'''
'''
i = 1

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

url = "http://bourse.fortuneo.fr/sicav-fonds/cours-aaa-actions-agro-alimentaire-c-FR0010058529-26"
req = urllib.request.urlopen(url, context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
soup = BeautifulSoup(req, 'html.parser')
print(soup.find('span', class_="header-devise").contents)
print(soup.find('div', class_="content-date").contents[3].contents)
'''
