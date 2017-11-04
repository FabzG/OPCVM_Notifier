import datetime

class TestOpcvm():

    def test_get_name(self):
        test_opcvm = Opcvm(self, "test", "FR00000000")
        assert test_opcvm.get_name() == "test"

    def test_get_isim(self):
        test_opcvm = Opcvm(self, "test", "FR00000000")
        assert test_opcvm.get_name() == "FR00000000"

    def test_get_value_list(self):
        test_opcvm = Opcvm(self, "test", "FR00000000")
        test_opcvm.add_value(datetime.date(2017,11,4), 112.2)
        test_date = datetime.date(2017,11,4)

        assert test_opcvm.get_value_list()[0].get_date() == test_date
        assert test_opcvm.get_value_list()[0].get_value() == 112.2

    def test_get_value_by_date(self):
        test_opcvm = Opcvm(self, "test", "FR00000000")
        test_opcvm.add_value(datetime.date(2017,11,4), 112.2)
        test_date = datetime.date(2017,11,4)

        assert test_opcvm.get_value_by_date(test_date)[0].get_date() == test_date
        assert test_opcvm.get_value_by_date(test_date)[0].get_value() == 112.2
