#class Task
import os
import re
from tools import *
class Task:
    def __init__(self,name):
        self.__Name = name
        self.__dictTargets = {}
        self.__dictTargetTimes = {}
        self.__times_default = 20

    def addTarget(self, name_Target, res_Target):
        self.__dictTargets [name_Target] = res_Target

    def addTargetTimes(self, name_Target, times):
        self.__dictTargetTimes [name_Target] = times

    def modifyTarget(self, name_Target, res_Target):
        self.__dictTargets [name_Target] = res_Target

    def exe_task(self,lis,benchName,themeName):
        print("-In Task "+self.__Name+":")
        for i in self.__dictTargets:
            # print(i,lis)
            if i in lis:
                path_ConfigFile = "../"+benchName +"/targets/"+i
                command,language = ConfigFile(path_ConfigFile)
                path = "../"+benchName +"/tasks/"+themeName+"/"+self.__Name
                start = time.time()
                times = self.__times_default
                if i in self.__dictTargetTimes:
                    times = self.__dictTargetTimes[i]
                for n in range(times):
                    exeCmd(path,command,language)
                self.__dictTargets[i] = (time.time() - start)/times
                print("--execute target " + i +' '+times.__str__()+' times')
                print("Execution time:"+self.__dictTargets[i].__str__())

    def getName(self):
        return self.__Name
    def ToCsv(self,writer,theme):
        targetNames = []
        targetNames = dict.keys(self.__dictTargets)
        for target in targetNames:
            run_time = self.__dictTargets[target]
            writer.writerow([theme, self.__Name, target, run_time])

#theme
class Theme:
    def __init__(self,name):
        self.__themeName = name
        self.__listTasks = []

    def addTask(self,task):
        self.__listTasks.append(task)
    def getName(self):
        return self.__themeName

    def exe_theme(self,listTask,listTarget,benchName):
        print("\nIn theme " + self.getName() + ":")
        for i in range(len(self.__listTasks)):
            # print(listTask)
            if self.__listTasks[i].getName() in listTask:
                self.__listTasks[i].exe_task(listTarget,benchName,self.__themeName)

    def showlistTasks(self):
        print("In the theme " + self.getName() + ",there are tasks:")
        for i in self.__listTasks:
            print(i.getName())
    def showInfoTask(self,nameTask,nameTest):
        for i in self.__listTasks:
            if i.getName() == nameTask:
                file_read("../"+nameTest,nameTask,'tasks')
                return 1
    def ToCsv(self,writer):
        for task in self.__listTasks:
            task.ToCsv(writer,self.__themeName)
#class BenchTrack,
class BenchTrack:
    def __init__(self,name_test):
        self.__name = name_test
        #dictionaire of targets,<key = nameTarget> = objetTarget
        self.__dictTargets={}
        #list of
        self.__listThemes=[]
        self.__allTarget=[]
        self.__allTask = []
        self.__construct()
        self.__outputFile = "../"+self.__name+"/output.csv"
    def __construct(self):
        """
        construct all theme,target,task
        """
        path = '../'
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
                #for every target in the folder task
                for i in os.listdir(pathTs):
                    if re.match("times",i):
                        with open(pathTs+i, newline='') as csvfile:
                            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                            next(spamreader)
                            for row in spamreader:
                                aux = re.split(',|\[|\]|\'',row.__str__())
                                aux = [x for x in aux if x != '']
                                task.addTargetTimes(aux[0],int(aux[1]))
                        continue
                    ret = re.match("README|data", i)
                    if not ret:
                        ret = re.match("[A-Z,a-z,_,-]*", i)
                        # print(ret.group())
                        pathF = pathTs + '/' + i
                        task.addTarget(ret.group(),-1)
                        task.addTarget(ret.group(),-1)
                theme.addTask(task)
            self.__listThemes.append(theme)

        #construt list of targets
        path = "../"+self.__name+"/targets"
        for targetName in os.listdir(path):
            self.__allTarget.append(targetName)

    def getName(self):
        return self.__name

    def ToCsv(self):
        with open(self.__outputFile, "w",newline="") as csvfile:
            writer = csv.writer(csvfile)
            # name of columns
            writer.writerow(["theme", "task", "target", "run_time"])
            # values of columns
            for theme in self.__listThemes:
                theme.ToCsv(writer)

    def addTargets(self,name_target,lang_target):
        self.__dictTargets[name_target] = lang_target

    def __addThemes(self,theme):
        self.__listThemes.append(theme)

    # execution of bench
    def exe_bench(self):
        print("Execution de "+self.__name)
        for i in range(len(self.__listThemes)):
            self.__listThemes[i].exe_theme(self.__allTask,self.__allTarget,self.__name)

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

    def show_list_target(self):
        print("List of targets:")
        for i in range(len(self.__allTarget)):
            print(self.__allTarget[i])

    def showInfoTarget(self,nomTarget):
        print("Information of " + nomTarget + " in the test " + self.__name +":")
        file_read("../"+self.__name,nomTarget,"targets")

    def showListTasks(self):
        print("List of tasks:")
        for i in range(len(self.__listThemes)):
            self.__listThemes[i].showlistTasks()

    def showInfoTask(self,nameTask):
        for i in self.__listThemes:
            if i.showInfoTask(nameTask,self.__name):
                return 1
        print("Task "+nameTask+" doesn't exite")
        return -1
