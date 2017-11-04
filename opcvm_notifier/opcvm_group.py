class OpcvmGroup():

    def __init__(self, group_name, opcvm=False):
        self._name = group_name
        self._opcvm_list = []

        if opcvm:
            self._opcvm_list.append(opcvm)

    def get_name(self):
        return self._name

    def get_opcvm_list(self):
        return self._opcvm_list