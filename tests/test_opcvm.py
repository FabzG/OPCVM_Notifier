import datetime
import opcvm_notifier.opcvm as opcvm


class TestOpcvm():

    def test_get_name(self):
        test_opcvm = opcvm.Opcvm("test", "FR00000000")
        assert test_opcvm.get_name() == "test"

    def test_get_isim(self):
        test_opcvm = opcvm.Opcvm("test", "FR00000000")
        assert test_opcvm.get_isim() == "FR00000000"

    def test_get_value_dict(self):
        test_opcvm = opcvm.Opcvm("test", "FR00000000")
        test_opcvm.add_value(datetime.date(2017, 11, 4), 112.2)
        test_date = datetime.date(2017, 11, 4)

        assert test_opcvm.get_value_list()[test_date] == 112.2
