class TestOpcvmGroup():

    def test_get_opcvm_groups(self):
        test_opcvm = opcvm.Opcvm("test", "FR00000000")
        test_opcvm_group = opcvm_group.OpcvmGroup("test group", test_opcvm)

        assert test_opcvm_group.get_groups() == "test group"

    def test_get_opcvm_by_groups(self):
        test = False
        test_opcvm = opcvm.Opcvm("test", "FR00000000")
        test_opcvm_group = opcvm_group.OpcvmGroup("test group", test_opcvm)

        for opcvm in test_opcvm_group.get_opcvm("test group"):
            if(opcvm == test_opcvm):
                test = True

        assert test
