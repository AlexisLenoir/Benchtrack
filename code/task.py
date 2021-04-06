from tools import *
class Task:
    def __init__(self, name, args, sample_size=20):
        self.__Name = name
        self.__dictTargets = {}
        self.__sample_size = sample_size
        self.args = args

    def __str__(self):
        string = self.getName() + "["
        for i in self.__dictTargets:
            string += i + " "
        return string + "]"

    def addTarget(self, name_Target, res_Target=-1):
        self.__dictTargets[name_Target] = res_Target

    def modifyTarget(self, name_Target, res_Target):
        self.__dictTargets[name_Target] = res_Target

    def exe_task(self, lis, benchName, themeName, path):
        print("-In Task " + self.__Name + ":")
        for i in self.__dictTargets:
            if i in lis:
                # time to execute before_test
                times_before = time.time()
                self.exe_before_test(benchName, themeName, i, path)
                times_before = time.time() - times_before

                # time to execute test
                start = time.time()
                self.exe_target(benchName, themeName, i, path)
                self.__dictTargets[i] = (time.time() - start - times_before) / self.__sample_size
                print("--execute target " + i + ' ' + self.__sample_size.__str__() + ' times')
                print("Execution time:" + self.__dictTargets[i].__str__())

    def exe_before_test(self, benchName, themeName, targets, path):
        path_File = path + benchName + "/tasks/" + themeName + "/" + self.getName() + "/" + "before_" + targets
        path_ConfigFile = path + benchName + "/targets/" + targets
        self.exe_file(path_ConfigFile, path_File)

    def exe_target(self, benchName, themeName, targets, path):
        path_ConfigFile = path + benchName + "/targets/" + targets
        path_File = path + benchName + "/tasks/" + themeName + "/" + self.getName() + targets
        self.exe_file(path_ConfigFile, path_File)

    def exe_file(self, path_configFile, args, path_file):
        if os.path.exists(path_configFile):
            command, language = ConfigFileTask(path_configFile)
            for n in range(self.__sample_size):
                if os.path.exists(path_file):
                    exeCmd(path_file, args, command, language)
        else:
            print("Can't find the file config:" + path_file)

    def getName(self):
        return self.__Name

    def ToCsv(self, writer, theme):
        targetNames = []
        targetNames = dict.keys(self.__dictTargets)
        for target in targetNames:
            run_time = self.__dictTargets[target]
            writer.writerow([theme, self.__Name, target, run_time])