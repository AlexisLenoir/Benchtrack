"""
-----------------------------------------bench2content-------------------------------------------

Cette fonction prend en argument l'adresse de l'infrastructure et à l'aide du fichier csv results,
genère un répertoire content pour l'affichage du site statique.

"""

import os
import csv
import shutil
import numpy as np
import sys
from os import getcwd, chdir, mkdir
import pathlib as pl


# Créer une fonction pour charger le csv
def load_csv_results(path_infra_csv):
    list_tasks = {}
    nb_tasks = 0
    list_targets = {}
    nb_targets = 0

    with open(path_infra_csv) as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue

            if not row[1] in list_tasks:
                list_tasks[row[1]] = nb_tasks
                nb_tasks +=1

            if not row[2] in list_targets:
                list_targets[row[2]] = nb_targets
                nb_targets +=1
    
        run_times = [["" for j in range(nb_targets)] for i in range(nb_tasks)]
        line_count = 0 

        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            indice_task = list_tasks[row[1]]
            indice_target = list_targets[row[2]]
            run_times[indice_task][indice_target] = row[3]


    #print (" Les tasks sont ",list_tasks)
    #print (" Les targets ",list_targets)
    #print(" Les temps d'éxécution sont ",run_times)

    return [list_tasks,list_targets,run_times]


def create_infra_rst(name_infra, path_content, path_readme, results):
    path_file = path_content+ "/" +name_infra+ ".rst"
    shutil.copy(path_readme,path_file)
    list_tasks = results[0]
    list_targets = results[1]
    run_times = results[2]

    with open(path_file,'a') as f:
        f.write("\n")
        f.write("\n")
        f.write(".. list-table:: Results\n")
        f.write("   :widths: auto\n")
        f.write("   :header-rows: 1\n")
        f.write("   :stub-columns: 1\n")
        f.write("\n")
        f.write("   * - Tasks/Targets\n")
        for tg in list(list_targets.keys()):
            f.write("     - "+tg+"\n")
        for tk in list(list_tasks.keys()):
            f.write("   * - "+tk+"\n")
            for tg in list(list_targets.keys()):
                f.write("     - "+run_times[list_tasks[tk]][list_targets[tg]]+"\n")

        

def create_target_rst(name_target,path_readme,path_targets,results):
    path_file = path_targets+ "/" +name_target+ ".rst"
    shutil.copy(path_readme,path_file)
    list_tasks = results[0]
    list_targets = results[1]
    run_times = results[2]

    with open(path_file,'a') as f:
        f.write("\n")
        f.write("\n")
        f.write(".. list-table:: Results\n")
        f.write("   :widths: auto\n")
        f.write("   :header-rows: 1\n")
        f.write("   :stub-columns: 1\n")
        f.write("\n")
        f.write("   * - Tasks\n")
        f.write("     - Run_time\n")
        for tk in list(list_tasks.keys()):
            f.write("   * - "+tk+"\n")
            f.write("     - "+run_times[list_tasks[tk]][list_targets[name_target]]+"\n")


def create_task_rst(name_task,path_readme,path_tasks,results):
    path_file = path_tasks+ "/" +name_task+ ".rst"
    shutil.copy(path_readme,path_file)
    list_tasks = results[0]
    list_targets = results[1]
    run_times = results[2]

    with open(path_file,'a') as f:
        f.write("\n")
        f.write("\n")
        f.write(".. list-table:: Results\n")
        f.write("   :widths: auto\n")
        f.write("   :header-rows: 1\n")
        f.write("   :stub-columns: 1\n")
        f.write("\n")
        f.write("   * - Targets\n")
        f.write("     - Run_time\n")
        for tg in list(list_targets.keys()):
            f.write("   * - "+tg+"\n")
            f.write("     - "+run_times[list_tasks[name_task]][list_targets[tg]]+"\n")

def create_targetXtask_rst(name_target,name_task,path_code,path_targetsXtasks,results):
    path_file = path_targetsXtasks + "/" + name_target + "X" + name_task + ".rst"
    list_tasks = results[0]
    list_targets = results[1]
    run_times = results[2]

    with open(path_code,'r') as f:
        code = f.read()
    
    with open(path_file,'w') as f:
        f.write ("La target "+name_target+" de la task "+name_task+": \n")
        f.write("\n")
        f.write("\n")
        f.write(".. list-table:: Results\n")
        f.write("   :widths: auto\n")
        f.write("   :header-rows: 1\n")
        f.write("   :stub-columns: 1\n")
        f.write("\n")
        f.write("   * - Run_time\n")
        f.write("     - "+run_times[list_tasks[name_task]][list_targets[name_target]])
        f.write("\n")
        f.write("\n")
        f.write("Code source: \n")
        f.write(code)






# On récupère le chemin du répertoire
path_infra = sys.argv[1]
#path_infra = "/Users/alexislenoir/python/bench2html/ConfigFichier"
name_infra = os.path.basename(path_infra)

# On crée le repertoire content 
path_content = os.path.dirname(path_infra) + "/content"
os.mkdir(path_content)


# Chargement du fichier .cvs 
results = load_csv_results(path_infra + "/" + name_infra + ".csv")


# On génère le fichier name_of_infrastructure.rst (page résumé)
create_infra_rst(name_infra ,path_content,path_infra+"/README.rst",results)



# On génère les pages par target

# Créer un sous-répertoire targets
path_targets = path_content+"/targets"
os.mkdir(path_targets)

list_targets = results[1]
list_tasks = results[0]

for tg in list(list_targets.keys()):
    path_tg_rd= path_infra+"/targets/"+tg+"/README.rst" 
    create_target_rst(tg, path_tg_rd, path_targets, results)

# On génère les pages par task et par target x task
os.mkdir(path_content+"/tasks")
path_targetsXtasks = path_content+"/targetsXtasks"
os.mkdir(path_targetsXtasks)

#chdir('essais')
list_themes = [file_name for file_name in os.listdir(path_infra+"/tasks") if file_name[0] != '.']
#print(list_themes)
for th in list_themes:
    list_tks = [file_name for file_name in os.listdir(path_infra+"/tasks/"+th) if file_name[0] != '.']
    #print(list_tks)
    for tk in list_tks:
        create_task_rst(tk,path_infra+"/tasks/"+th+"/"+tk+"/README.rst",path_content+"/tasks",results)
        list_tgs = [pl.PurePosixPath(file_name).stem  for file_name in os.listdir(path_infra+"/tasks/"+th+"/"+tk) if file_name[0] != '.']
        #print(list_tgs)
        for tg in list(list_targets.keys()):
            if tg in list_tgs:
                create_targetXtask_rst(tg,tk,path_infra+"/tasks/"+th+"/"+tk+"/"+tg+".py",path_targetsXtasks,results)






