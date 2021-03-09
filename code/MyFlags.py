from absl import app
from absl import flags
import os
FLAGS = flags.FLAGS
def flagTasks(argv,bench):
    if FLAGS.task == '-i':
        if len(argv)< 3:
            print('Without'+ (3 - len(argv)).__init__()+'parameter')
            return - 1
        bench.showInfoTask(argv[1])
    if FLAGS.task == '-l':
        if len(argv) < 2:
            print('Without a parameter')
            return -1
        print("List of tasks:")
        bench.showListTasks()
    if FLAGS.task == '-include':
        list_Include = argv[1:len(argv)-1]
        bench.filter_task(list_Include,True)
        bench.exe_bench()
    if FLAGS.task == '-exclude':
        list_Include = argv[1:len(argv)-1]
        bench.filter_task(list_Include,False)
        bench.exe_bench()

def flagTargets(argv,bench):
    if FLAGS.target == '-i':
        if len(argv) < 3:
            print('Without'+ (3 - len(argv)).__init__()+'parameter')
            return -1
        bench.showInfoTarget(argv[1])
    if FLAGS.target == '-l':
        if len(argv) < 2:
            print('Without a parameter')
            return -1
        bench.show_list_target()
    if FLAGS.target == '-include':
        list_Include = argv[1:len(argv)-1]
        bench.filter_target(list_Include,True)
        bench.exe_bench()
    if FLAGS.target == '-exclude':
        list_Include = argv[1:len(argv)-1]
        bench.filter_target(list_Include,False)
        bench.exe_bench()
