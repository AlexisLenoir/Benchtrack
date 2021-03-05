from absl import app
from absl import flags
import os

#show file's name of a folder
def file_name(file_dir,typeF):
    File_Name = []
    for files in os.listdir(file_dir):
        if files == typeF:
            file_dir = file_dir + "/" + files
            for files_sous in os.listdir(file_dir):
                print(files_sous)
    return File_Name
#show a file
def file_read(nomTest, nomTarget,typeF):
    for files in os.listdir(nomTest):
        if files == typeF:
            file_dir = nomTest + "/" + files
            for files_sous in os.listdir(file_dir):
                if files_sous == nomTarget:
                    filesRead = nomTest + "/" + typeF + "/" + nomTarget + "/" + "read.rst"
                    with open(filesRead, 'r') as f:
                        content = f.read()
                        print(content)

#show a list of all targets
def showListTargets(nomTest):
    file_name(nomTest,"targets")

#show the infomation of the target
def showInfoTarget(nomTarget,nomTest):
    print("Information of " + nomTarget + " in the test " + nomTest +":")
    file_read(nomTarget,nomTest,"targets")
#dispose flag --target
def flagTargets(argv):
    if FLAGS.target == '-i':
        if len(argv) < 3:
            print('Without'+ (3 - len(argv)).__init__()+'parameter')
            return -1
        showInfoTarget(argv[1],argv[2])
    if FLAGS.target == '-l':
        if len(argv) < 2:
            print('Without a parameter')
            return -1
        print("List of tagets:")
        showListTargets(argv[1])

#show the infomation of the task
def showInfoTask(nomTask,nomTest):
    print("Information of " + nomTask + "dans le test" + nomTest)
#show a list of all tasks
def showListTasks():
    pass
#dispose flag --tasks
def flagTasks(argv):
    if FLAGS.tasks == '-i':
        if len(argv)< 3:
            print('Without'+ (3 - len(argv)).__init__()+'parameter')
            return - 1
        showInfoTask(argv[1],argv[2])
    if FLAGS.tasks == '-l':
        if len(argv) < 2:
            print('Without a parameter')
            return -1
        print("List of tasks:")
        showListTasks(argv[1])

#modify the location of output file html
def modifyOutputLocation():
    pass

#define flags
FLAGS = flags.FLAGS
helpTarget = '\nFormat:--target <-l|-i> nameTest\n-l:list of target\n -i:infomation of target\n'
flags.DEFINE_enum('target', None, ['-l', '-i'], helpTarget)
helpTask = '\nFormat:--target <-l|-i> nameTest\n-l:list of target\n -i:infomation of task\n'
flags.DEFINE_enum('tasks', None,['-l', '-i'],helpTask)
flags.DEFINE_string('output',None,'Modife the folder of file output.html\n')

def flag(argv):
    # if FLAGS.debug:
    #     print('non-flag arguments:', argv)
    if FLAGS.target is not None:
        flagTargets(argv )
    if FLAGS.tasks is not None:
        flagTasks(argv)
    if FLAGS.output is not None:
        if len(argv) < 2:
            print("Without the parameter location")
            return -1
        modifyOutputLocation(argv[2])

if __name__ == '__main__':
    app.run(flag)