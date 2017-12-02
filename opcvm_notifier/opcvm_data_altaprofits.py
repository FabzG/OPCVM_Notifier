import urllib.request
import ssl
import json
import datetime
from bs4 import BeautifulSoup

class OpcvmDataAltaprofits():

    def __init__(self):
        self._base_url = "https://www.altaprofits.com/services/graphes/actifHistoData.jsp?isinList="

    def get_history(self, isin):
        historical_datas = {}
        #print(self._base_url + isin)
        req = urllib.request.urlopen(self._base_url + isin, context=ssl.SSLContext(ssl.PROTOCOL_SSLv23)).read()#.decode('iso-8859-1').encode('UTF-8')
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
'''
test = OpcvmDataAltaprofits()
test_ret = test.get_history("FR0007016068")

for key_elem in test_ret:
    print(str(key_elem) + " " + str(test_ret[key_elem]))
'''