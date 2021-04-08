import unittest
from benchTrack import *
from unittest.mock import patch

class TestMathFunc(unittest.TestCase):
    """Test benchTrack.py"""
    def test_construct(self):
        bench = BenchTrack("../PGM")
        self.assertEqual("PGM",bench.getName())
        string = "PGM:list Themes[inference[BIFreading[pyAgrum ]]]"
        self.assertEqual(string,bench.__str__())

    def test_structure(self):
        bench = BenchTrack("../PGM")
        string = "{'inference': {'BIFreading': ['pyAgrum.py']}}"
        self.assertEqual(string,bench.get_structure_tasks().__str__())

    # def test_InfoTarget(self):
    #     bench = BenchTrack("ConfigFichier")
    #     with patch('builtins.print') as mocked_print:
    #         bench.showInfoTarget("xml_demo")
    #         # print(mocked_print)
    #         mocked_print.assert_called_with('Fin\n')
    #
    # def test_ListTarget(self):
    #     bench = BenchTrack("ConfigFichier")
    #     with patch('builtins.print') as mocked_print:
    #         bench.show_list_target()
    #         # print(mocked_print)
    #         mocked_print.assert_called_with("xml_demo")
    #
    # def test_InfoTask(self):
    #     bench = BenchTrack("ConfigFichier")
    #     with patch('builtins.print') as mocked_print:
    #         bench.showInfoTask("charger_employe")
    #         # print(mocked_print)
    #         mocked_print.assert_called_with('Fin\n')
    #
    # def test_ListTask(self):
    #     bench = BenchTrack("ConfigFichier")
    #     with patch('builtins.print') as mocked_print:
    #         bench.showListTasks()
    #         # print(mocked_print)
    #         mocked_print.assert_called_with("charger_employe_coordonnees")

    # def test_filter_target(self):
    #     bench = BenchTrack("ConfigFichier")
    #     bench.filter_target("xml_demo",True)
    #     bench.exe_bench()
    #     bench.ToCsv()






if __name__ == '__main__':
    unittest.main()
