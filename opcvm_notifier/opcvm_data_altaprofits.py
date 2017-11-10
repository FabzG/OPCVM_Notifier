import urllib.request
import ssl
import json

class OpcvmDataAltaprofits():

    def __init__(self):
        self._base_url = "https://www.altaprofits.com/services/graphes/actifHistoData.jsp?isinList="

    def get_history(self, isin):
        print(self._base_url + isin)
        req = urllib.request.urlopen(self._base_url + isin, context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
        print(req)
        with urllib.urlopen("https://www.altaprofits.com/services/graphes/actifHistoData.jsp?isinList=FR0007016068") as response:
            print(response.read())
        json_data = json.load(req)

        if json_data['datas']['series']['datas']:
            for elemtab in json_data['datas']['series']['datas']:
                print(elemtab)

test = OpcvmDataAltaprofits()
test.get_history("FR0007016068")