charger_employe/ini_demo
########################

:authors: Benchtrack
:date: 2010-10-03 10:20

La target `ini_demo <{filename}/targets/ini_demo.rst>`_ de la task `charger_employe <{filename}/tasks/charger_employe.rst>`_ 


.. list-table:: Results
   :widths: auto

   * - Run_time
     - 3.5924


Code source: 

.. code-block:: python 
   :linenos: table
   :linenostart: 1

   import configparser
   
   mon_conteneur = configparser.ConfigParser()
   mon_conteneur.read('data/employe.ini'