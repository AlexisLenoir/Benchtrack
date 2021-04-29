"""
-----------------------------------------------bench2site---------------------------------------------------
Ce module permet de générer le site
"""

import os
import csv
import sys
import src.BenchTrack.structureBench
from generateRst import *



def load_csv_results(path_infra_csv, structure_run_time):
    
    with open(path_infra_csv) as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            
            structure_run_time[row[1]][row[2]][row[3]] = row[4]

    #print ("structure_run_time", structure_run_time)

    return structure_run_time



def bench2content(path_infra, path_benchTrack, file_csv):
    """
    Cette fonction prend en argument l'adresse de l'infrastructure et à l'aide du fichier csv results,
    genère un répertoire content pour l'affichage du site statique.
    """
    
    name_infra = os.path.basename(path_infra)

    # Chargement de l'objet de Benchtrack et de certains attributs
    my_bench = structureBench.BenchTrack(path_infra, path_benchTrack)

    list_targets = my_bench._BenchTrack__allTarget
    list_tasks = my_bench._BenchTrack__allTask

    # structure_task permet de savoir comment sont répartis les tasks et les targets
    structure_tasks = my_bench.get_structure_tasks()
    list_themes = list(structure_tasks.keys())

    """
    # Test sur les attributs de BenchTrack : 

    print("Liste des themes :",my_bench._BenchTrack__listThemes)
    print("Liste des targets :",list_targets)
    print("Liste des tasks :",list_tasks )
    print(" liste themes 2 :",list_themes)


    for th in list_themes:
    print( "Pour le theme", th)
    list_tasks = list(structure_tasks[th].keys())
    print (" list_tasks", list_tasks)
    for tk in list_tasks:
        print(" Pour la task", tk)
        list_target = structure_tasks[th][tk]
        print("liste des targets:", list_target)

    """

    # Initialisation de structure_run_time
    structure_run_time = {}
    for task in list_tasks:
        structure_run_time[task] = {}
        for target in list_targets:
            structure_run_time[task][target] = {}

    # Instanciation de structure_run_time à partir de results.csv 
    structure_run_time = load_csv_results(path_infra + "/" + file_csv, structure_run_time)

    #-----------Create path_content-----------

    #path_content = os.path.dirname(path_infra) + "/content"
    path_site = path_benchTrack + "/site"
    path_site_infra = path_benchTrack + "/site_" + name_infra
    os.system("cp -r " + path_site + " " + path_site_infra) #zip ?

    path_content = path_site_infra + "/content"
    os.mkdir(path_content)
    path_pages = path_content+"/pages"
    os.mkdir(path_pages)

    #------------ Page résumé ----------------
    create_infra_rst(name_infra,path_pages,path_infra+"/README.rst",structure_run_time,list_targets)

    # On génère les pages listes (sous-répertoire page)
    #create_pages_rst(path_pages,results)


    #------------ Page par target ------------

    # Créer un sous-répertoire targets
    path_targets = path_content+"/targets"
    os.mkdir(path_targets)

    for tg in list_targets:
        path_tg_rd= path_infra+"/targets/"+tg+"/README.rst" 
        create_target_rst(tg, path_tg_rd, path_targets, list_tasks,structure_run_time)


    #------------ Page par task/ Page par target x task ------------

    path_tasks = path_content+"/tasks"
    os.mkdir(path_tasks)
    path_targetsXtasks = path_content+"/targetsXtasks"
    os.mkdir(path_targetsXtasks)

    for theme in list_themes:
        list_tasks_in_theme = list(structure_tasks[theme].keys())

        for task in list_tasks_in_theme:
            path_readme_task = path_infra+"/tasks/"+theme+"/"+task+"/README.rst"
            # Génération de page par task 
            create_task_rst(task, path_readme_task, path_tasks, list_targets,structure_run_time)
            list_target_in_task = structure_tasks[theme][task]

            for target in list_target_in_task:
                # Génération de page par target x task 
                path_code = path_infra+"/tasks/"+theme+"/"+task+"/"+target
                name_target = os.path.splitext(os.path.basename(target))[0]
                create_targetXtask_rst(name_target, task, path_code, path_targetsXtasks,path_pages, structure_run_time)

    return path_site_infra, name_infra

    
def content2html(path_site_infra, path_benchTrack, name_infra):

    #print(" Test path interpreter: ",sys.executable)
    #print(" Test, lancer pelican")

    os.chdir(path_site_infra)
    os.system(sys.executable + " -m pelican content")

    # Modification de conf.py
    path_conf_py = path_site_infra + "/pelicanconf.py"
    new_file = ""
    line_name_site = "SITENAME = '"+ name_infra+"'\n"
    with open(path_conf_py) as f:
        for line in f:
            if line == "SITENAME = 'default'\n":
                new_file += line_name_site
                continue
            else:
                new_file += line

    with open(path_conf_py,'w') as f:
        f.write(new_file)








#--------------------------TEST-----------------------


if __name__ == '__main__':
    path_infra_PGM = "/Users/alexislenoir/python/Benchtrack/infrastructures/PGM"
    path_infra_ConfigFichier = "/Users/alexislenoir/python/Benchtrack/infrastructures/ConfigFichier"
    #path_infra_term = sys.argv[1]
    file_csv = "output.csv"

    path_benchTrack = os.path.dirname(os.path.dirname(os.path.abspath( __file__ )))

    path_site_infra, name_infra = bench2content(path_infra_ConfigFichier, path_benchTrack, file_csv)
    content2html(path_site_infra, path_benchTrack, name_infra)
    

