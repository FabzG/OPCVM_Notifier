class Opcvm:

    def __init__(self, name, isim):
        self._name = name
        self._isim = isim
        self._values = []

    def __init__(self, name, values):
        self._name = name
        self._isim = isim
        self._values = values

    def get_name(self):
        return self._name

    def get_isim(self):
        return self._isim

