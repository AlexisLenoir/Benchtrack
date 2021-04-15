from tools import *
class Task:
    def __init__(self, name, args, sample_size=20):
        '''
        Constructor of class Task

        Parameters
        ----------
        name : string
            name of the task.
        args : string
            parameters of the task.
        sample_size : int, optional
            the times of execution. The default is 20.

        Returns
        -------
        None.

        '''
        self.__Name = name
        self.__dictTargets = {}
        self.__sample_size = int(sample_size)
        self.__args = args
    def __str__(self):
        '''
        Return a string of all the targets from the task

        Returns
        -------
        stirng
            all the targets from the task.

        '''
        string = self.getName() + "["
        for i in self.__dictTargets:
            string += i + " "
        return string + "]"

    def addTarget(self, name_Target):
        '''
        Add targets to targets dictionary of the task

        Parameters
        ----------
        name_Target : string
            name of target.

        Returns
        -------
        None.

        '''
        self.__dictTargets[name_Target] = [-1] * len(self.__args)

    def modifyTarget(self, name_Target, res_Target):
        '''
        Add execution time of targets of the task

        Parameters
        ----------
        name_Target : string
            the target.
        res_Target : flaot
            execution time.

        Returns
        -------
        None.

        '''
        self.__dictTargets[name_Target] = res_Target

    def exe_task(self, lis, themeName, path):
        '''
        Execution of the tasks 

        Parameters
        ----------
        lis : list of string
            list of targets.
        themeName : string
            name of theme of the task.
        path : stirng
            the path contains the theme

        Returns
        -------
        None.

        '''
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
        '''
        execute some before-task file like imports

        Returns
        -------
        None.

        '''
        path_File = path  + "/tasks/" + themeName + "/" + self.getName() 
        path_ConfigFile = path  + "/targets/" + targets + "/config.ini"
        self.exe_file(path_ConfigFile, path_File,args,"before_"+targets)

    def exe_target(self, themeName, targets,path,args):
        '''
        drive infos from configure file of target and transforme these infos

        Returns
        -------
        None.

        '''
        path_ConfigFile = path  + "/targets/" + targets + "/config.ini"
        path_File = path  + "/tasks/" + themeName + "/" + self.getName() 
        self.exe_file(path_ConfigFile, path_File,args,targets)

    def exe_file(self, path_configFile, path_file, args,target):
        '''
        execution of target

        Returns
        -------
        None.

        '''
        
        #path_file+=".py"
        if os.path.exists(path_configFile):
            command, language = ConfigFileTarget(path_configFile)
            for n in range(1):
                
                #if os.path.exists(path_file):
                    
                    exeCmd(path_file, args, command, language,target)
        else:
            print("Can't find the file config:" + path_configFile)

    def getName(self):
        '''
        return name of the task

        Returns
        -------
        string
            name of the task.

        '''
        return self.__Name

    def ToCsv(self, writer, theme):
        '''
        generetor the csv file which contains some
        infos about results of execution

        Returns
        -------
        None.

        '''
        targetNames = []
        targetNames = dict.keys(self.__dictTargets)
        for target in targetNames:
            for i in range(len(self.__args)):
                run_time = self.__dictTargets[target][i]
                writer.writerow([theme, self.__Name, target,self.__args[i], run_time])

    def get_structure_tasks(self,path):
        '''
        get targets of tasks

        Returns
        -------
        list_target : TYPE
            DESCRIPTION.

        '''
        list_target=[]
        for target in list(self.__dictTargets.keys()):
            path_configFile = path + "/targets/" + target + "/config.ini"
            if os.path.exists(path_configFile):
                command, language = ConfigFileTarget(path_configFile)
                target += get_suffixe(language)
                list_target.append(target)
        return list_target