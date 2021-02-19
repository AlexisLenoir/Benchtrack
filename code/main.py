import os
import os
import time
import datetime
#Pour trouver tous les fichers de repertoire de BASE.
def find_all_file(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f

#Pour calculer temps d'execution
def exe_python(target_name):
    start = datetime.datetime.now()
    print("Test "+target_name+" start")
    os.system("python " + target_name)
    timeUsed = (datetime.datetime.now() - start).microseconds * 1e-6
    print("Test " + target_name +" finished using time:" + timeUsed.__str__())
    return timeUsed

# #execute test of bench
# def exe_bench(bench_name):
#     for i in find_all_file(bench_name):
#         exe_python(i)
#test
base = 'PGM/bench1/'
for i in find_all_file(base):
    t = exe_python(base + i)
