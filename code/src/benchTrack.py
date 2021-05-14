import os
import sys
import BenchTrack.structureBench as bt
# from BenchTrack.bench2site import bench2site
import BenchTrack.tools as tl


def exe(argv):
    """
    execution of the tool BenchTrack

    :param str argv: input in the terminal.

    """

    """
    Intégration 

    bench.getPathInf():
    infrastructures/PGM
    bench.getPathOutputFile():
    infrastructures/PGM/output.csv

    """

    if len(argv) < 2:
        print("Missing parameter,use --help to read the guide")
        return -1
    path_benchTrack = os.path.dirname(os.path.dirname(os.path.abspath( __file__ )))
    path_inf = argv[-1]
    if "--help" in argv:
        tl.help()
        return 0
    if "--check" in argv:
        tl.checkInfrastructure()
    bench = bt.BenchTrack(path_inf, path_benchTrack)

    if tl.manage_flag(argv,bench):
        bench.exe_bench()
        bench.ToCsv()
        # path_csvFile = bench.getPathOutputFile()
        # bench2site(path_inf, path_csvFile)

def mainFonction():
    exe(sys.argv)

if __name__ == '__main__':
    exe(sys.argv)
