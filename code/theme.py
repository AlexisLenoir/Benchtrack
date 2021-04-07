from tools import *
#theme

class Theme:
    def __init__(self,name):
        self.__themeName = name
        self.__listTasks = []

    def __str__(self):
        string = self.getName()
        string += "["+self.__listTasks[0].__str__()
        for i in range(1,len(self.__listTasks)):
            string += "," + self.__listTasks[i].__str__()
        string += "]"
        return string
    def addTask(self,task):
        self.__listTasks.append(task)
    def getName(self):
        return self.__themeName

    def exe_theme(self,listTask,listTarget,path):
        print("\nIn theme " + self.getName() + ":")
        for i in range(len(self.__listTasks)):
            # print(listTask)
            if self.__listTasks[i].getName() in listTask:
                self.__listTasks[i].exe_task(listTarget,self.__themeName,path)

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

    def get_structure_tasks(self,path):
        list_structure_task = {}
        for task in self.__listTasks:
            list_structure_task[task.getName()] =task.get_structure_tasks(path)
        return  list_structure_task

