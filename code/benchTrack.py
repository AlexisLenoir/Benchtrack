import os
import sys
# from absl import app
# from absl import flags

from tools import *
from MyFlags import *
from structureBench import BenchTrack

# FLAGS = flags.FLAGS
# helpTarget = '\nFormat:--target nameTest\n-l:list of target\n -i:infomation of target\n'
# flags.DEFINE_enum('target', None,['--liste', '-info','--include','--exclude'],helpTarget)
# helpTask = '\nFormat:--task nameTest\n-l:list of task\n -i:infomation of task\n'
# flags.DEFINE_enum('task', None,['--liste', '--info','--include','--exclude'],helpTask)
# flags.DEFINE_string('output',None,'Modife the folder of file output.html\n')

#function for manage flags
def manage_flag(argv,bench):
    # if FLAGS.target is not None:
    #     flagTargets(argv,bench)
    #     return 1
    #
    # if FLAGS.task is not None:
    #     flagTasks(argv,bench)
    #     return 1
    #
    # if FLAGS.output is not None:
    #     if len(argv) < 2:
    #         print("Without the parameter location")
    #         return -1
    #     # modifyOutputLocation(argv[1])
    #     return 1
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
    bench = BenchTrack(argv[len(argv) - 1])
    if manage_flag(argv,bench):
        bench.exe_bench()
        bench.ToCsv()


if __name__ == '__main__':
    exe(sys.argv)
