import datetime
import opcvm_notifier.opcvm_data_altaprofits as opcvm_data_altaprofits
import pytest

class TestOpcvmDataAltaprofits():

    def test_get_history(self):
        # for "UBS EUROPEAN OPPORTUNITY UNCONSTRAINED PEA (EUR) R", 2000-01-10 -> 277,2
        test_altaprofits = opcvm_data_altaprofits.OpcvmDataAltaprofits()
        history_tab = test_altaprofits.get_history("FR0007016068")
        assert history_tab[datetime.date(2000, 1, 10)] == 277.2

    @pytest.mark.skip
    def test_get_actual_value(self):
        # for "UBS EUROPEAN OPPORTUNITY UNCONSTRAINED PEA (EUR) R"
        test_altaprofits = opcvm_data_altaprofits.OpcvmDataAltaprofits()
        actual_value = test_altaprofits.get_value("FR0007016068")
        assert actual_value == 630.39
