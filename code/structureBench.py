#class Task
import os
import re
from tools import *


class Task:
    def __init__(self,name):
        self.__Name = name
        self.__dictTargets = {}
    # def __str__(self):
    #     str = "BenchMark:" + self.__Name + ",Targets:\n"
    #     for i in self.__dictTargets.keys():
    #         str += "Target " + i.__str__() + ":" + self.__dictTargets[i].__str__() + "\n"
    #     return str + '\n'

    def addTarget(self, name_Target, res_Target):
        self.__dictTargets [name_Target] = res_Target

    def modifyTarget(self, name_Target, res_Target):
        self.__dictTargets [name_Target] = res_Target

    def exe_task(self,lis):
        print("-In Task "+self.__Name+":")
        for i in self.__dictTargets:
            # print(i,lis)
            if i in lis:
                print("--execute target "+i)

    def getName(self):
        return self.__Name

#theme
class Theme:
    def __init__(self,name):
        self.__themeName = name
        self.__listTasks = []
    # def __str__(self):
    #     str = "BenchName:"+self.__themeName+'BenchMark:\n'
    #     for i in range(len(self.__listTasks)):
    #         str += self.__listTasks[i].__str__()
    #     return str
    def addTask(self,task):
        self.__listTasks.append(task)
    def getName(self):
        return self.__themeName

    def exe_theme(self,listTask,listTarget):
        print("\nIn theme " + self.__themeName + ":")
        for i in range(len(self.__listTasks)):
            # print(listTask)
            if self.__listTasks[i].getName() in listTask:
                self.__listTasks[i].exe_task(listTarget)

    def showlistTasks(self):
        print("\nIn the theme " + self.getName() + ",there are tasks:")
        for i in self.__listTasks:
            print(i.getName())
    def showInfoTask(self,nameTask,nameTest):
        for i in self.__listTasks:
            if i.getName() == nameTask:
                file_read(nameTest,nameTask,'tasks')
                return 1

class BenchTrack:
    def __init__(self,name_test):
        self.__name = name_test
        #dictionaire[Name_Target]=langauge
        self.__dictTargets={}
        #list of objet task
        self.__listThemes=[]
        self.__allTarget=[]
        self.__allTask = []
        self.__construct()

    def __construct(self):
        path = './'
        if not exitFile(self.__name,path):
            print("Error:Test name")
            return -2
        path += self.__name
        #for every theme in the folder test
        path += '/tasks'
        for themeName in os.listdir(path):
            theme = Theme(themeName)
            #for every task in the folder theme
            pathT = path + '/' + themeName
            for taskName in os.listdir(pathT):
                task = Task(taskName)
                if taskName not in self.__allTask:
                    self.__allTask.append(taskName)
                pathTs = pathT+'/'+taskName +'/'
                for i in find_all_file(pathTs):
                    ret = re.match("read", i)
                    if not ret:
                        ret = re.match("[A-Z,a-z]*", i)
                        # print(ret.group())
                        pathF = pathTs + '/' + i
                        task.addTarget(ret.group(),-1)
                        task.addTarget(ret.group(),-1)
                theme.addTask(task)
            self.__listThemes.append(theme)
        #construt list of targets
        path = "./"+self.__name+"/targets"
        for targetName in os.listdir(path):
            self.__allTarget.append(targetName)

    def addTargets(self,name_target,lang_target):
        self.__dictTargets[name_target] = lang_target

    def __addThemes(self,theme):
        self.__listThemes.append(theme)

    # execution of bench
    def exe_bench(self):
        print("Execution de "+self.__name)
        for i in range(len(self.__listThemes)):
            self.__listThemes[i].exe_theme(self.__allTask,self.__allTarget)

    def filter_target(self,lis,model):
        if model:
            self.__allTarget = lis
            # print(self.__allTarget)
        else:
            self.__allTarget = [x for x in self.__allTarget if x not in lis]
            # print('List:')
            # print(self.__allTarget)

    def filter_task(self,lis,model):
        if model:
            self.__allTask = lis
            print(self.__allTask)
        else:
            self.__allTask = [x for x in self.__allTask if x not in lis]
            print(self.__allTask)

    # def exe_bench_Task(self):
    #     print("Execution de "+self.__name)
    #     for i in range(len(self.__listThemes)):
    #         self.__listThemes[i].exe_theme()
    #
    # def exe_bench_Target(self,listTarget,mode):
    #     print("Execution de "+self.__name)
    #     for i in range(len(self.__listThemes)):
    #         self.__listThemes[i].exe_theme()

    def show_list_target(self):
        print("List of targets:")
        for i in range(len(self.__allTarget)):
            print(self.__allTarget[i])

    def showInfoTarget(self,nomTarget):
        print("Information of " + nomTarget + " in the test " + self.__name +":")
        file_read(self.__name,nomTarget,"targets")

    def showListTasks(self):
        for i in range(len(self.__listThemes)):
            print("List of tasks:")
            self.__listThemes[i].showlistTasks()

    def showInfoTask(self,nameTask):
        for i in self.__listThemes:
            if i.showInfoTask(nameTask,self.__name):
                return 1
        print("Task "+nameTask+" doesn't exite")
        return -1
