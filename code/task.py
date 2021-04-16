from tools import *
import os
class Task:
    """
    This class contains the structure of the Task

    :cvar str __Name :name of the task.
    :cvar str __args :parameters of the task.
    :cvar int __sample_size :optional,the times of execution. The default is 20.
    :cvar dict __dictTargets:a dictionnaire contains keys of target's name and values of object Target
    """
    def __init__(self, name, args, sample_size=20):
        """
        Constructor of class Task

        :param str name :name of the task.
        :param str args :parameters of the task.
        :param int sample_size :optional,the times of execution. The default is 20.

        :return: no return

        """
        self.__Name = name
        self.__dictTargets = {}
        self.__sample_size = int(sample_size)
        self.__args = args
    def __str__(self):
        """
        Return a string of all the targets from the task

        :return: stirng:all the targets from the task.

        """
        string = self.getName() + "["
        for i in self.__dictTargets:
            string += i + " "
        return string + "]"

    def addTarget(self, name_Target):
        '''
        Add targets to targets dictionary of the task

        param str name_Target :name of target.

        :return: no return

        '''
        self.__dictTargets[name_Target] = [-1] * len(self.__args)

    def modifyTarget(self, name_Target, res_Target):
        """
        Add execution time of targets of the task

        :param str name_Target :the target.
        :param float res_Target : execution time.

        :return: no return

        """
        self.__dictTargets[name_Target] = res_Target

    def exe_task(self, lis, themeName, path):
        """
        Execution of the tasks

        :param list lis :list of targets.
        :param str themeName : name of theme of the task.
        :param str path :the path contains the theme

        :return: no return

        """
        print("-In Task " + self.__Name + ":")
        for target in self.__dictTargets:
            if target in lis:
                try :
                    self.exe_target(themeName, target, path, self.__args[0])
                except ModuleNotFoundError:
                    self.upgrade_for_target(path,target)
                list_times = []
                for j in range(len(self.__args)):
                    # time to execute before_test
                    times_before = time.time()
                    for _ in range(self.__sample_size):
                        self.exe_before_test(themeName, target, path,self.__args[j])
                    times_before = time.time() - times_before

                    # time to execute test
                    start = time.time()
                    for _ in range(self.__sample_size):
                        self.exe_target(themeName, target, path,self.__args[j])
                    list_times.append((time.time() - start - times_before) / self.__sample_size)

                    print("--execute target " + target + ' ' + self.__sample_size.__str__() + ' times with arg:' + self.__args[j])
                    print("Execution time:" + list_times[-1].__str__())
                self.__dictTargets[target] = list_times

    def exe_before_test(self, themeName, targets, path,args):
        """
        execute some before-task file like imports

        :param str themeName:name of theme
        :param str targets:name of target
        :param str path :path of the infrastructure
        :param str args:args of execution

        :return: no return

        """
        path_File = path  + "/tasks/" + themeName + "/" + self.getName() 
        path_ConfigFile = path  + "/targets/" + targets + "/config.ini"
        self.exe_file(path_ConfigFile, path_File,args,"before_"+targets)

    def exe_target(self, themeName, targets,path,args):
        '''
        drive infos from configure file of target and transforme these infos

        :param str themeName:name of theme
        :param str targets:name of target
        :param str path :path of the infrastructure
        :param str args:args of execution

        :return: no return

        '''
        path_ConfigFile = path  + "/targets/" + targets + "/config.ini"
        path_File = path  + "/tasks/" + themeName + "/" + self.getName()
        self.exe_file(path_ConfigFile, path_File,args,targets)

    def exe_file(self, path_configFile, path_file, args,target):
        '''
        execution of a target

        :param str path_configFile:path of file config of target
        :param str path_file:file to execute
        :param str args:args of execution
        :param str target :name of target

        :return: no return

        '''
        command, language = ConfigFileTarget(path_configFile)
        exeCmd(path_file, args, command, language,target)


    def getName(self):
        '''
        get name of the task

        :return:name of the task.

        '''
        return self.__Name

    def ToCsv(self, writer, theme):
        '''
        generetor the csv file which contains some
        infos about results of execution

        :return: no return

        '''
        targetNames = dict.keys(self.__dictTargets)
        for target in targetNames:
            for i in range(len(self.__args)):
                run_time = self.__dictTargets[target][i]
                writer.writerow([theme, self.__Name, target,self.__args[i], run_time])

    def get_structure_tasks(self,path):
        """
        get targets of tasks

        :return: list_target : TYPE DESCRIPTION.

        """
        list_target=[]
        for target in list(self.__dictTargets.keys()):
            path_configFile = path + "/targets/" + target + "/config.ini"
            if os.path.exists(path_configFile):
                command, language = ConfigFileTarget(path_configFile)
                target += get_suffixe(language)
                list_target.append(target)
        return list_target

    def upgrade_for_target(self,path,target):
        """

        :return: no return
        """
        path_ConfigFile = path  + "/targets/" + target + "/config.ini"
        config = ConfigParser()
        config.read(path_ConfigFile)
        upgrade = config.get('execution', 'upgrading')
        os.system(upgrade)