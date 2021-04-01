import time
import datetime
from configparser import ConfigParser
import csv
import os
from rpy2 import robjects

def exeCmdPython(path, cmd):
    CurrentPath = os.getcwd()
    PathAbsolu = CurrentPath + "/" + path
    os.fchdir(os.open(PathAbsolu, os.O_RDONLY))
    #res = os.system("cd"+path+"&&"+cmd)
    res=os.system(cmd)
    if res != 0:
        if os.path.exists('errorInfo.txt'):
            with open('errorInfo.txt', mode='w', encoding='utf-8') as ff:
                print(ff.read())
        else:
            with open("errorInfo.txt", mode='w+', encoding='utf-8') as ff:
                print(ff.read())

    os.fchdir(os.open(CurrentPath, os.O_RDONLY))


def exeCmdR(path,cmd):
        robjects.r.source(path+"/"+cmd)


def exeCmd(path, cmd,language):
    if language == "python":
        exeCmdPython(path, cmd)
    if language == "r":
        exeCmdR(path,cmd)


def ConfigFile(targetName):
    config = ConfigParser()
    config.read(targetName + "/config.ini")
    language = config.get('execution', 'language')
    run = config.get('execution', 'run')
    return run,language


# pour trouver tous les fichers de repertoire de BASE.
def find_all_file(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f


def exitFile(fileName, Path):
    for files in os.listdir(Path):
        if files == fileName:
            return True
    return False


# Pour calculer temps d'execution en python
# @param target_name:path et nom pour target
# @return temp d'execution
def exe_python(target_name):
    start = datetime.datetime.now()
    print("Test " + target_name + " start")
    os.system("python " + target_name)
    timeUsed = (datetime.datetime.now() - start).microseconds * 1e-6
    print("Test " + target_name + " finished using time:" + timeUsed.__str__())
    return timeUsed


# return the commande for run the target
def run_text(target_name):
    pass


def to_txt(list_res):
    with  open('PGM/result.txt', 'w') as f:
        for i in list_res:
            f.write(i.benchName + '\n')
            for target in i.listTargets:
                f.write(target)
            f.write('\n')
            for targetTime in i.listTemps:
                f.write(targetTime.__str__() + '\n')
            f.write('|' + '\n')
        f.close()


# print a file
def file_read(nomTest, nomTarget, typeF):
    for files in os.listdir(nomTest):
        if files == typeF:
            file_dir = nomTest + "/" + files
            for files_sous in os.listdir(file_dir):
                if files_sous == nomTarget:
                    filesRead = nomTest + "/" + typeF + "/" + nomTarget + "/" + "README.rst"
                    with open(filesRead, 'r') as f:
                        content = f.read()
                        print(content)
                        print("Fin\n")
                        return 1
                if exitFile(files_sous, file_dir):
                    dir = file_dir + "/" + files_sous
                    for file_task in os.listdir(dir):
                        if file_task == nomTarget:
                            filesRead = nomTest + "/" + typeF + "/" + files_sous + "/" + file_task + "/" + "README.rst"
                            with open(filesRead, 'r') as f:
                                content = f.read()
                                print(content)
                                print("Fin\n")
                                return 1