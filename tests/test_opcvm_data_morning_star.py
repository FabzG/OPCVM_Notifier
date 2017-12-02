from datetime import date
import opcvm_notifier.opcvm_data_morning_star as opcvm_data_morning_star
import pytest

class TestOpcvmDataMorningStar():

    def test_get_mornings_star_id(self):
        # for "AXA Or et Matières Premières C", ISIN FR0010011171
        test_morning_star = opcvm_data_morning_star.OpcvmDataMorningStar()
        id_morning_star = test_morning_star.get_id("FR0010011171")
        assert id_morning_star == "F0GBR04GA7"

    def test_get_mornings_star_id(self):
        # for "AXA Or et Matières Premières C", ISIN FR0010011171, hist value = 1341273600000,84.58
        test_morning_star = opcvm_data_morning_star.OpcvmDataMorningStar()
        historical_value = test_morning_star.get_historical_value("FR0010011171", date(2011,3,7))
        assert historical_value == 47.080
