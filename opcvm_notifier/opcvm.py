class Opcvm:

    def __init__(self, name, isim, values={}):
        self._name = name
        self._isim = isim
        self._values = values

    def get_name(self):
        return self._name

    def get_isim(self):
        return self._isim

    def get_value_list(self):
        return self._values

    def get_value_list(self):
        return self._values

    def set_value_list(self, values_list):
        self._values = values_list

    def add_value(self, date, value):
        self._values[date] = value
