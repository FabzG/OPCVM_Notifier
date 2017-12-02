import urllib.request
import ssl
import json
import datetime
from bs4 import BeautifulSoup

class OpcvmDataAltaprofits():

    def __init__(self):
        self._base_url_history = "https://www.altaprofits.com/services/graphes/actifHistoData.jsp?isinList="
        self._base_url_value = "https://www.altaprofits.com/support-opcvm/[NAME]-(eur)-r-isin-[ISIN]/cours"

    def get_history(self, isin):
        historical_datas = {}
        #print(self._base_url + isin)
        req = urllib.request.urlopen(self._base_url_history + isin, context=ssl.SSLContext(ssl.PROTOCOL_SSLv23)).read()#.decode('iso-8859-1').encode('UTF-8')
        #print(str(req)[2:-1].replace("\\", ""))
        json_data = json.loads(str(req)[2:-1].replace('\\', ''))
        #print(json_data)

        if json_data['datas']['series']:
            for elemtab in json_data['datas']['series']:
                if(elemtab['datas']):
                    for data_opcvm in elemtab['datas']:
                        date_value = datetime.date(int(data_opcvm['date'][:4]), int(data_opcvm['date'][5:7]), int(data_opcvm['date'][8:10]))
                        historical_datas[date_value] = data_opcvm['value']
        return historical_datas


    def get_value(self, isin, name):

        formatted_url = self._base_url_value.replace("[NAME]", name.replace(" ", "-").lower()).replace("[ISIN]", isin)
        formatted_url = OpcvmDataAltaprofits.remove_accents(formatted_url)
        print(formatted_url)
        req = urllib.request.urlopen(formatted_url, context=ssl.SSLContext(ssl.PROTOCOL_SSLv23)).read()
        #print(req)
        soup = BeautifulSoup(req, 'html.parser')
        all_th = soup.findAll("th")
        for th in all_th:
            #print(th)
            if(th.string == "Valeur liquidative"):
                return (th.find_next_sibling("td").string.replace(" ","").replace("€", ""))
        return None

    def remove_accents(input):
        return input.lower().replace("é", "e").replace("è", "e").replace("à", "a")
'''
test = OpcvmDataAltaprofits()
test_ret = test.get_value("FR0010547059", "TOCQUEVILLE VALUE AMÉRIQUE P")
print(test_ret)
'''
'''
test = OpcvmDataAltaprofits()
test_ret = test.get_history("FR0007016068")

for key_elem in test_ret:
    print(str(key_elem) + " " + str(test_ret[key_elem]))
'''