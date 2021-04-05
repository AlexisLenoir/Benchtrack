#class Task
import os
import re
from tools import *
class Task:
    def __init__(self,name,args,sample_size=20):
        self.__Name = name
        self.__dictTargets = {}
        self.__sample_size = sample_size
        self.args = args

    def __str__(self):
        string = self.getName() + "["
        for i in self.__dictTargets:
            string += i + " "
        return string

    def addTarget(self, name_Target, res_Target = -1):
        self.__dictTargets [name_Target] = res_Target

    def modifyTarget(self, name_Target, res_Target):
        self.__dictTargets [name_Target] = res_Target

    def exe_task(self,lis,benchName,themeName,path):
        print("-In Task "+self.__Name+":")
        for i in self.__dictTargets:
            if i in lis:
                #time to execute before_test
                times_before = time.time()
                self.exe_before_test(benchName,themeName,i,path)
                times_before = time.time() - times_before

                #time to execute test
                start = time.time()
                self.exe_target(benchName,themeName,i,path)
                self.__dictTargets[i] = (time.time() - start - times_before)/self.__sample_size
                print("--execute target " + i +' '+self.__sample_size.__str__()+' times')
                print("Execution time:"+self.__dictTargets[i].__str__())


    def exe_before_test(self,benchName,themeName,targets,path):
        path_File = path + benchName + "/tasks/" + themeName + "/" + self.getName() + "/" + "before_" + targets
        path_ConfigFile = path + benchName + "/targets/" + targets
        self.exe_file(path_ConfigFile, path_File)

    def exe_target(self,benchName,themeName,targets,path):
        path_ConfigFile = path + benchName + "/targets/" + targets
        path_File =path + benchName + "/tasks/" + themeName + "/" + self.getName() + targets
        self.exe_file(path_ConfigFile,path_File)

    def exe_file(self,path_configFile,args,path_file):
        if os.path.exists(path_configFile):
            command, language = ConfigFile(path_configFile)
            for n in range(self.__sample_size):
                if os.path.exists(path_file):
                    exeCmd(path_file,args, command, language)
        else:
            print("Can't find the file config:"+path_file)

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

    def __str__(self):
        string = self.getName()
        string += self.__listTasks[0].__str__()
        for i in range(1,len(self.__listTasks)):
            string += "," + self.__listTasks[i].__str__()
        string += "]"

    def addTask(self,task):
        self.__listTasks.append(task)
    def getName(self):
        return self.__themeName

    def exe_theme(self,listTask,listTarget,benchName,path):
        print("\nIn theme " + self.getName() + ":")
        for i in range(len(self.__listTasks)):
            # print(listTask)
            if self.__listTasks[i].getName() in listTask:
                self.__listTasks[i].exe_task(listTarget,benchName,self.__themeName,path)

    def showlistTasks(self):
        print("In the theme " + self.getName() + ",there are tasks:")
        for i in self.__listTasks:
            print(i.getName())
    def showInfoTask(self,nameTask,nameTest,path):
        for i in self.__listTasks:
            if i.getName() == nameTask:
                file_read(path+nameTest,nameTask,'tasks')
                return 1
    def ToCsv(self,writer):
        for task in self.__listTasks:
            task.ToCsv(writer,self.__themeName)
#class BenchTrack,
class BenchTrack:
    def __init__(self,path,name):
        self.__path = path.replace('benchtrack.py',' ')
        self.__name = name
        #dictionaire of targets,<key = nameTarget> = objetTarget
        self.__dictTargets={}
        #list of
        self.__listThemes=[]
        self.__allTarget=[]
        self.__allTask = []
        self.__construct()
        self.__outputFile = self.__path+self.__name+"/output.csv"
    def __str__(self):
        string = self.getName()
        string += ":list Themes["
        string += self.__listThemes[0].__str__()
        for i in range(1,len(self.__listThemes)):
            string += "," + self.__listThemes[i].__str__()
        string += "]"
        return string

    def __construct(self):
        """
        construct all theme,target,task
        """
        path = self.__path
        if not exitFile(self.__name,path):
            print("Error:Test name")
            return -2
        path += self.__name
        #for every theme in the folder test
        path += '/tasks'

        #construt list of targets
        path = self.__path+self.__name+"/targets"
        for targetName in os.listdir(path):
            self.__allTarget.append(targetName)

        for themeName in os.listdir(path):
            theme = Theme(themeName)
            #for every task in the folder theme
            pathT = path + '/' + themeName
            for taskName in os.listdir(pathT):
                #set in the list alltask
                if taskName not in self.__allTask:
                    self.__allTask.append(taskName)
                pathTs = pathT+'/'+taskName +'/'
                path_config = pathTs + 'config.ini'
                #resd config.ini and construct task
                sample_size = 20
                args = ''
                if os.path.exists(path_config):
                    sample_size,args = ConfigFileTask(path_config)
                task = Task(taskName,args.split(' '),sample_size)
                # set all target
                for targetName in self.__allTarget:
                    path_target = pathTs + targetName
                    if os.path.exists(path_target):
                        task.addTarget(targetName)
                theme.addTask(task)
                #for every target in the folder task
                # for i in os.listdir(pathTs):
                #     if re.match("times",i):
                #         with open(pathTs+i, newline='') as csvfile:
                #             spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                #             next(spamreader)
                #             for row in spamreader:
                #                 aux = re.split(',|\[|\]|\'',row.__str__())
                #                 aux = [x for x in aux if x != '']
                #                 task.addTargetTimes(aux[0],int(aux[1]))
                #         continue
                #     ret = re.match("README|data", i)
                #     if not ret:
                #         ret = re.match("[A-Z,a-z,_,-]*", i)
                #         # print(ret.group())
                #         pathF = pathTs + '/' + i
                #         task.addTarget(ret.group(),-1)
                #         task.addTarget(ret.group(),-1)

            self.__listThemes.append(theme)

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
            self.__listThemes[i].exe_theme(self.__allTask,self.__allTarget,self.__name,self.__path)

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
        file_read(self.__path+self.__name,nomTarget,"targets")

    def showListTasks(self):
        print("List of tasks:")
        for i in range(len(self.__listThemes)):
            self.__listThemes[i].showlistTasks()

    def showInfoTask(self,nameTask):
        for i in self.__listThemes:
            if i.showInfoTask(nameTask,self.__name,self.__path):
                return 1
        print("Task "+nameTask+" doesn't exite")
        return -1
