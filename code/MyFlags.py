# from absl import app
# from absl import flags
import os

def flagTasks(argv,bench,flag):
    '''
    gestion of flags of the tasks

    Parameters
    ----------
    argv : string
        name of the benchmark.
    bench : string
        name of bench for testing.
    flag : string
        type of flags.


    '''
    if flag == 'info':
        if len(argv)< 3:
            print('Without'+ (3 - len(argv)).__init__()+'parameter')
            return - 1
        bench.showInfoTask(argv[1])
    if flag == 'list':
        if len(argv) < 2:
            print('Without a parameter')
            return -1
        bench.showListTasks()
    if flag == 'include':
        list_Include = argv[1:len(argv)-1]
        bench.filter_task(list_Include,True)

    if flag == 'exclude':
        list_Include = argv[1:len(argv)-1]
        bench.filter_task(list_Include,False)


def flagTargets(argv,bench,flag):
    '''
    gestion of flags of the targets

    Parameters
    ----------
    argv : string
        name of the benchmark.
    bench : string
        name of bench for testing.
    flag : string
        type of flags.


    '''
    
    if flag == 'info':
        if len(argv) < 3:
            print('Without'+ (3 - len(argv)).__init__()+'parameter')
            return -1
        bench.showInfoTarget(argv[1])
    if flag == 'list':
        if len(argv) < 2:
            print('Without a parameter')
            return -1
        bench.show_list_target()
    if flag == 'include':
        list_Include = argv[1:len(argv)-1]
        bench.filter_target(list_Include,True)

    if flag == 'exclude':
        list_Include = argv[1:len(argv)-1]
        bench.filter_target(list_Include,False)
