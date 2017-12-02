import urllib.request
import ssl
import json
import datetime
import datetime
from datetime import date
from bs4 import BeautifulSoup

class OpcvmDataMorningStar():

    def __init__(self):
        self._base_url_find_id = "http://www.morningstar.fr/fr/funds/SecuritySearchResults.aspx?type=FUND&search=[ISIN]"
        self._base_url_fund = "http://www.morningstar.fr/fr/funds/snapshot/snapshot.aspx?id="
        self._base_url_histo = "http://tools.morningstar.fr/api/rest.svc/timeseries_price/ok91jeenoo?id=[IDMORNING]%5D2%5D1%5D&currencyId=EUR&idtype=Morningstar&priceType=&frequency=daily&startDate=1900-01-01&endDate=[TODAY]&outputType=COMPACTJSON"

    def get_id(self, isin):
        formatted_url = self._base_url_find_id.replace("[ISIN]", isin)
        req = urllib.request.urlopen(formatted_url, context=ssl.SSLContext(ssl.PROTOCOL_SSLv23)).read()
        soup = BeautifulSoup(req, 'html.parser')
        a_id = soup.select('a[href^="/fr/funds/snapshot/snapshot.aspx?id="]')
        id = str(a_id[0])[45:55]
        return id

    def get_history(self, isin):
        id_morning_star = self.get_id(isin)
        formatted_url = self._base_url_histo.replace("[IDMORNING]", id_morning_star).replace("[TODAY]", str(date.today()))
        print(formatted_url)
        req = urllib.request.urlopen(formatted_url, context=ssl.SSLContext(ssl.PROTOCOL_SSLv23)).read()

        history = {}

        for elem in str(req)[4:-3].split("],["):
            date_millisec = elem.split(", ")[0]
            value = elem.split(", ")[1]
            delta = datetime.timedelta(milliseconds=int(date_millisec))
            date_formatted = date(1970,1,1)+delta
            history[date_formatted] = float(value)

        return history

    def get_historical_value(self, isin, value_date):
        return self.get_history(isin)[value_date]
