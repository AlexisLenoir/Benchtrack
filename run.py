"""
Script qui prend un fichier configuration json en argument
"""
import json
import sys

name_file = sys.argv[1]

with open(name_file) as json_data:
    data_dict = json.load(json_data)
    print(data_dict)
