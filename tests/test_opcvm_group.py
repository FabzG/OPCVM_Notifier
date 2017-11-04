import opcvm_notifier.opcvm_group as opcvm_group
import opcvm_notifier.opcvm as opcvm

class TestOpcvmGroup():

    def test_get_opcvm_groups(self):
        test_opcvm_group = opcvm_group.OpcvmGroup("test group")

        assert test_opcvm_group.get_name() == "test group"

    def test_get_opcvm_by_groups(self):
        test = False
        test_opcvm = opcvm.Opcvm("test", "FR00000000")
        test_opcvm_group = opcvm_group.OpcvmGroup("test group", test_opcvm)

        for current_opcvm in test_opcvm_group.get_opcvm_list():
            if current_opcvm == test_opcvm:
                test = True

        assert test
