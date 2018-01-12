import opcvm_notifier.opcvm_fortuneo
import pytest


class TestOpcvmFortuneo:

    '''@pytest.mark.skip'''
    def test_get_url(self):
        fortuneo_test = opcvm_notifier.opcvm_fortuneo.OpcvmFortuneo()
        assert fortuneo_test.get_base_url() == "https://bourse.fortuneo.fr/api/sicav/search/?additionalParams=%7B%22ftnVie%22:%22true%22,%22view%22:%22VUE_PERF%22%7D&page="

    '''@pytest.mark.skip'''
    def test_get_list_first_opcvm(self):
        fortuneo_test = opcvm_notifier.opcvm_fortuneo.OpcvmFortuneo()
        assert fortuneo_test.get_list_opcvm()[0].get_name() == "AAA Actions Agro Alimentaire RC"