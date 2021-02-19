import os
import time
import datetime

#Pour trouver tous les fichers de repertoire de BASE.
from resultsBench import ResultsBench

def find_all_file(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f

#Pour calculer temps d'execution en python
#@param target_name:path et nom pour target
#@return temp d'execution
def exe_python(target_name):
    start = datetime.datetime.now()
    print("Test "+target_name+" start")
    os.system("python " + target_name)
    timeUsed = (datetime.datetime.now() - start).microseconds * 1e-6
    print("Test " + target_name +" finished using time:" + timeUsed.__str__())
    return timeUsed

#execute test of bench
def exe_bench(bench_name):
    base = 'PGM/' + bench_name + '/'
    res = ResultsBench(base)
    for i in find_all_file(base):
        t = exe_python(base + i)
        res.add_target(i,t)
    return res

def to_txt(list_res):
    with  open('PGM/result.txt','w') as f:
        for i in list_res:
            f.write(i.benchName+'\n')
            for target in i.listTargets:
                f.write(target)
            f.write('\n')
            for targetTime in i.listTemps:
                f.write(targetTime.__str__()+'\n')
            f.write('|'+'\n')
        f.close()