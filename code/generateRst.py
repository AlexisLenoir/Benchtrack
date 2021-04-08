"""
-----------------------------------------------generateRst---------------------------------------------------
Ce module contient toutes les fonctions permettant de générer les fichiers rst pour le répertoire content

"""


def create_title_rst(readme,name_title):
    """
    Pour gérer les cas où il y a déjà un titre
    readme est une chaîne de carac d'un fichier readme
    """
    title = ""
    for i in range(len(readme)):
        if readme[i] == '\n':
            if readme[i+1] == '#' or readme[i+1] == '=':
                return title
            else:
                break
    title = name_title + " [Error]\n"
    nb_carac = len(title)
    for i in range(nb_carac):
        title += "="
    title += "\n"
    return title

def create_rst_base():
    pass
  
def create_infra_rst(name_infra, path_content, path_readme, structure_run_time, list_targets):
    readme = ''
    with open(path_readme,'r') as f:
        readme = f.read()

    path_file = path_content+ "/" +name_infra+ ".rst"

    with open(path_file,'w') as f:
        f.write(create_title_rst(readme,name_infra))
        """
        f.write(name_infra+"\n")
        for i in range(len(name_infra)):
            f.write("#")
        f.write("\n")
        """
        f.write("\n")
        f.write(":authors: Benchtrack\n")
        f.write(":date: 2010-10-03 10:20\n")
        f.write("\n")
        f.write(readme)
        f.write("\n")
        f.write("\n")
        f.write(".. list-table:: Results\n")
        f.write("   :widths: auto\n")
        f.write("   :header-rows: 1\n")
        f.write("   :stub-columns: 1\n")
        f.write("\n")
        f.write("   * - Tasks/Targets\n")
        for target in list_targets:
            f.write("     - "+target+"\n")

        problem_exec = False

        for task in list(structure_run_time.keys()):
            f.write("   * - "+task+"\n")
            for target in list(structure_run_time[task].keys()):
                if len(list(structure_run_time[task][target].keys())) == 0:
                    f.write("     -  \n")
                else:
                    for arg in list(structure_run_time[task][target].keys()):
                        if structure_run_time[task][target][arg] == -2:
                            problem_exec = True
                            f.write("     - X\n")
                            break
                    if not problem_exec:
                        f.write("     - OK\n")

        
def create_target_rst(name_target, path_readme, path_targets, list_tasks, structure_run_time):
    readme = ''
    with open(path_readme,'r') as f:
        readme = f.read()

    path_file = path_targets+ "/" +name_target+ ".rst"

    with open(path_file,'w') as f:
        f.write(name_target+"\n")
        for i in range(len(name_target)):
            f.write("#")
        f.write("\n")
        f.write("\n")
        f.write(":authors: Benchtrack\n")
        f.write(":date: 2010-10-03 10:20\n")
        f.write("\n")
        f.write(readme)
        f.write("\n")
        f.write("\n")
        f.write(".. list-table:: Results\n")
        f.write("   :widths: auto\n")
        #f.write("   :header-rows: 1\n")
        #f.write("   :stub-columns: 1\n")
        f.write("\n")
        f.write("   * - Arg/Tasks\n")
        list_args = []
        for task in list_tasks:
            f.write("     - "+task+"\n")
            for arg in list(structure_run_time[task][name_target].keys()):
                if arg not in list_args:
                    list_args.append(arg)

        for arg in list_args:
            f.write("   * - "+arg+"\n")
            for task in list_tasks:
                if arg in list(structure_run_time[task][name_target].keys()):
                    f.write("     - "+structure_run_time[task][name_target][arg]+"\n")
                else:
                    f.write("     -  \n")


def create_task_rst(name_task, path_readme, path_tasks, list_targets, structure_run_time):
    readme = ''
    with open(path_readme,'r') as f:
        readme = f.read()

    path_file = path_tasks+ "/" +name_task+ ".rst"

    with open(path_file,'w') as f:
        f.write(name_task+"\n")
        for i in range(len(name_task)):
            f.write("#")
        f.write("\n")
        f.write("\n")
        f.write(":authors: Benchtrack\n")
        f.write(":date: 2010-10-03 10:20\n")
        f.write("\n")
        f.write(readme)
        f.write("\n")
        f.write("\n")
        f.write(".. list-table:: Results\n")
        f.write("   :widths: auto\n")
        #f.write("   :header-rows: 1\n")
        #f.write("   :stub-columns: 1\n")
        f.write("\n")
        f.write("   * - Arg/Targets\n")
        list_args = []
        for target in list_targets:
            f.write("     - "+target+"\n")
            for arg in list(structure_run_time[name_task][target].keys()):
                if arg not in list_args:
                    list_args.append(arg)

        for arg in list_args:
            f.write("   * - "+arg+"\n")
            for target in list_targets:
                if arg in list(structure_run_time[name_task][target].keys()):
                    f.write("     - "+structure_run_time[name_task][target][arg]+"\n")
                else:
                    f.write("     -  \n")

def create_targetXtask_rst(name_target, name_task,path_code, path_targetsXtasks, path_pages, structure_run_time):
    path_file = path_targetsXtasks + "/" + name_target + "X" + name_task + ".rst"

    with open(path_code,'r') as f:
        code = f.read()
    
    with open(path_file,'w') as f:
        f.write(name_task+"/"+name_target+"\n")
        for i in range(len(name_task+name_target)+1):
            f.write("#")
        f.write("\n")
        f.write("\n")
        f.write(":authors: Benchtrack\n")
        f.write(":date: 2010-10-03 10:20\n")
        f.write("\n")
        #f.write ("La target "+name_target+" de la task "+name_task+": \n")
        f.write ("La target ")
        f.write("`"+name_target+" <{filename}/targets/"+name_target+".rst>`_")
        f.write(" de la task ")
        f.write("`"+name_task+" <{filename}/tasks/"+name_task+".rst>`_ \n")
        f.write("\n")
        f.write("\n")
        f.write(".. list-table:: Results\n")
        f.write("   :widths: auto\n")
        f.write("\n")
        list_args = list(structure_run_time[name_task][name_target].keys())
        if len(list_args) > 1:
            f.write("   * - Arg \n")
            for arg in list_args:
                f.write("     - "+arg+"\n")
            f.write("   * - Run_time\n")
            for arg in list_args:
                f.write("     - "+structure_run_time[name_task][name_target][arg]+"\n")    
        else:
            f.write("   * - Run_time\n")
            if len(list_args) == 0:
                f.write("     -  X\n")
            else:
                f.write("     - "+structure_run_time[name_task][name_target][list_args[0]]+"\n")
        f.write("\n")
        f.write("\n")
        f.write("Code source: \n")
        f.write("\n")
        f.write(".. code-block:: python \n")
        f.write("   :linenos: table\n")
        f.write("   :linenostart: 1\n")
        f.write("\n")
        f.write("   ")
        for i in range (len(code)-1):
            if code[i] == '\n':
                f.write('\n')
                f.write("   ")
            else:
                f.write(code[i])
    """
    #deprecated
    with open(path_pages+"/targetsXtasks.rst",'a') as f:
        f.write("- `"+name_target+" for "+name_task+" <{filename}/targetsXtasks/"+name_target + "X" + name_task + ".rst>`_\n")
        f.write("\n"
    """

def create_pages_rst(path_pages,results):
    # Deprecated
    list_tasks = results[0]
    list_targets = results[1]
    run_times = results[2]

    with open(path_pages+"/targets.rst",'w') as f:
        f.write("Targets\n")
        f.write("#######\n")
        f.write("\n")
        f.write(":authors: Benchtrack\n")
        f.write(":date: 2010-10-03 10:20\n")
        f.write("\n")
        for tg in list(list_targets.keys()):
            f.write("- `"+tg+" <{filename}/targets/"+tg+".rst>`_\n")

    with open(path_pages+"/tasks.rst",'w') as f:
        f.write("Tasks\n")
        f.write("#####\n")
        f.write("\n")
        f.write(":authors: Benchtrack\n")
        f.write(":date: 2010-10-03 10:20\n")
        f.write("\n")
        for tk in list(list_tasks.keys()):
            f.write("- `"+tk+" <{filename}/tasks/"+tk+".rst>`_\n")

    with open(path_pages+"/targetsXtasks.rst",'w') as f:
        f.write("Targets per task\n")
        f.write("################\n")
        f.write("\n")
        f.write(":authors: Benchtrack\n")
        f.write(":date: 2010-10-03 10:20\n")
        f.write("\n")
