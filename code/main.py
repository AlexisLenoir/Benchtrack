import os

from benchTrack import *
from resultsBench import ResultsBench

#test
List_Result_Benchs = []
bench_name = 'bench1'
res = exe_bench(bench_name)
List_Result_Benchs.append(res)
print(res.__str__())

to_txt(List_Result_Benchs)

