#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import time
from rpy2 import robjects

class Rrunning:
    def exeCmd(path,cmd):
        start=time.time()
        robjects.r.source('/Users/radar/Documents/m1_androide/PROJET/Benchtrack/ConfigFichier/tasks/default/charger_employe/Untitled.R')
        exeTime=time.time()-start
        print(exeTime)
