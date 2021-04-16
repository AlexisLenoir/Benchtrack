import unittest
from benchTrack import *
from tools import *

class TestMathFunc(unittest.TestCase):
    """Test benchTrack.py"""
    def test_construct(self):
        bench = BenchTrack("../infrastructures/PGM","")
        self.assertEqual("PGM",bench.getName())
        string = "PGM:list Themes[inference[BIFreading[pyAgrumTest ]]]"
        self.assertEqual(string,bench.__str__())

    def test_structure(self):
        bench = BenchTrack("../infrastructures/PGM","")
        structure = bench.get_structure_tasks()
        theme = structure['inference']
        task = theme['BIFreading']
        self.assertEqual(task[0],'pyAgrumTest.py')

    def test_filter_target(self):
        bench = BenchTrack("../infrastructures/PGM","")
        number = bench.filter_target(['pyAgrumTest'],False)
        self.assertEqual(number,0)
        number = bench.filter_target(['pyAgrumTest'], True)
        self.assertEqual(number,1)

    def test_filter_task(self):
        bench = BenchTrack("../infrastructures/PGM","")
        number = bench.filter_task(['BIFreading'],False)
        self.assertEqual(number,0)
        number = bench.filter_task(['BIFreading'], True)
        self.assertEqual(number,1)

    def test_filter_task(self):
        bench = BenchTrack("../infrastructures/PGM","")
        number = bench.filter_task(['BIFreading'],False)
        self.assertEqual(number,0)
        number = bench.filter_task(['BIFreading'], True)
        self.assertEqual(number,1)

    def test_execute(self):
        self.assertTrue(exeCmd("../infrastructures/PGM/tasks/inference/BIFreading","asia.bif","python {script} {arg}","python","pyAgrumTest"))

    def text_To_Csv(self):
        bench = BenchTrack("../infrastructures/PGM","")
        bench.ToCsv()


if __name__ == '__main__':
    unittest.main()
