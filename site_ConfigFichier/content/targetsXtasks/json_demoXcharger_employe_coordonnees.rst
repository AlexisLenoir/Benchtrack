charger_employe_coordonnees/json_demo
#####################################

:authors: Benchtrack
:date: 2010-10-03 10:20

La target `json_demo <{filename}/targets/json_demo.rst>`_ de la task `charger_employe_coordonnees <{filename}/tasks/charger_employe_coordonnees.rst>`_ 


.. list-table:: Results
   :widths: auto

   * - Run_time
     - 2.8043


Code source: 

.. code-block:: python 
   :linenos: table
   :linenostart: 1

   import json
   
   with open('data/employe_coordonnees.json', 'r') as fichier:
       data = json.load(fichier)