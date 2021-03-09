import os
import sys
from absl import app
from absl import flags

from MyFlags import *
from structureBench import BenchTrack

FLAGS = flags.FLAGS
helpTarget = '\nFormat:--target <-l|-i> nameTest\n-l:list of target\n -i:infomation of target\n'
flags.DEFINE_enum('target', None, ['-l', '-i','-include','-exclude'], helpTarget)
helpTask = '\nFormat:--task <-l|-i> nameTest\n-l:list of task\n -i:infomation of task\n'
flags.DEFINE_enum('task', None,['-l', '-i','-include','-exclude'],helpTask)
flags.DEFINE_string('output',None,'Modife the folder of file output.html\n')

def manage_flag(argv,bench):
    if FLAGS.target is not None:
        flagTargets(argv,bench)
        return 0

    if FLAGS.task is not None:
        flagTasks(argv,bench)
        return 0

    if FLAGS.output is not None:
        if len(argv) < 2:
            print("Without the parameter location")
            return -1
        # modifyOutputLocation(argv[1])
        return 0
    return 1

def exe(argv):
    # if FLAGS.debug:
    #     print('non-flag arguments:', argv)
    if len(argv) < 2:
        print("Missing parameter")
        return -1
    bench = BenchTrack(argv[len(argv) - 1])
    if manage_flag(argv,bench):
        bench.exe_bench()


if __name__ == '__main__':
    app.run(exe)

