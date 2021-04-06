from tools import *
class Task:
    def __init__(self, name, args, sample_size=20):
        self.__Name = name
        self.__dictTargets = {}
        self.__sample_size = int(sample_size)
        self.__args = args
    def __str__(self):
        string = self.getName() + "["
        for i in self.__dictTargets:
            string += i + " "
        return string + "]"

    def addTarget(self, name_Target):
        self.__dictTargets[name_Target] = [-1] * len(self.__args)

    def modifyTarget(self, name_Target, res_Target):
        self.__dictTargets[name_Target] = res_Target

    def exe_task(self, lis, themeName, path):
        print("-In Task " + self.__Name + ":")
        for i in self.__dictTargets:
            if i in lis:
                list_times = []
                for j in range(len(self.__args)):
                    # time to execute before_test
                    times_before = time.time()
                    self.exe_before_test(themeName, i, path,self.__args[j])
                    times_before = time.time() - times_before

                    # time to execute test
                    start = time.time()
                    self.exe_target(themeName, i, path,self.__args[j])
                    list_times.append((time.time() - start - times_before) / self.__sample_size)

                    print("--execute target " + i + ' ' + self.__sample_size.__str__() + ' times avec parameter:' + self.__args[j])
                    print("Execution time:" + list_times[-1].__str__())
                self.__dictTargets[i] = list_times

    def exe_before_test(self, themeName, targets, path,args):
        path_File = path  + "/tasks/" + themeName + "/" + self.getName() + "/" + "before_" + targets
        path_ConfigFile = path  + "/targets/" + targets + "/config.ini"
        self.exe_file(path_ConfigFile, path_File,args)

    def exe_target(self, themeName, targets,path,args):
        path_ConfigFile = path  + "/targets/" + targets + "/config.ini"
        path_File = path  + "/tasks/" + themeName + "/" + self.getName() + "/" +targets
        self.exe_file(path_ConfigFile, path_File,args)

    def exe_file(self, path_configFile, path_file, args):
        if os.path.exists(path_configFile):
            command, language = ConfigFileTarget(path_configFile)
            for n in range(self.__sample_size):
                if os.path.exists(path_file):
                    exeCmd(path_file, args, command, language)
        else:
            print("Can't find the file config:" + path_configFile)

    def getName(self):
        return self.__Name

    def ToCsv(self, writer, theme):
        targetNames = []
        targetNames = dict.keys(self.__dictTargets)
        for target in targetNames:
            for i in range(len(self.__args)):
                run_time = self.__dictTargets[target][i]
                writer.writerow([theme, self.__Name, target,self.__args[i], run_time])