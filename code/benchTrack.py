import os
import sys
from MyFlags import *
from structureBench import BenchTrack

#function for manage flags
def manage_flag(argv,bench):
    '''
    This function manage all flags,
    with a flag for show a list or the information,this function call a function to show that
    with a flag include or exclude,this function modifie the object bench
    without flag,return 1
    Parameter:
        Argv:args
        Bench:l'object benchTrack
    '''
    for i in range(len(argv)):
        if "--target-include" == argv[i]:
            flagTargets(argv[i:],bench,"include")
        if "--target-exclude" == argv[i]:
            flagTargets(argv,bench,"exclude")
        if "--target-list" == argv[i]:
            flagTargets(argv[i:],bench,"list")
            return 0
        if "--target-info" == argv[i]:
            flagTargets(argv[i:],bench,"info")
            return 0

        if "--task-include" == argv[i]:
            flagTasks(argv[i:],bench,"include")
        if "--task-exclude" == argv[i]:
            flagTasks(argv[i:],bench,"exclude")
        if "--task-liste" == argv[i]:
            flagTasks(argv[i:],bench,"list")
            return 0
        if "--task-info" == argv[i]:
            flagTasks(argv[i:],bench,"info")
            return 0
    return 1

def exe(argv):
    if len(argv) < 2:
        print("Missing parameter")
        return -1
    bench = BenchTrack(argv[-1])
    if manage_flag(argv,bench):
        bench.exe_bench()
        bench.ToCsv()
    # print(bench.__str__())
    # print(bench.get_structure_tasks())
if __name__ == '__main__':
    exe(sys.argv)
