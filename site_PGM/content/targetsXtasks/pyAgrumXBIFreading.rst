BIFreading/pyAgrum
##################

:authors: Benchtrack
:date: 2010-10-03 10:20

La target `pyAgrum <{filename}/targets/pyAgrum.rst>`_ de la task `BIFreading <{filename}/tasks/BIFreading.rst>`_ 


.. list-table:: Results
   :widths: auto

   * - Arg 
     - asia.bif
     - alarm.bif
     - Mildew.bif
     - Diabetes.bif
   * - Run_time
     - 4.76837158203125e-08
     - -5.7220458984375e-07
     - 4.76837158203125e-08
     - -6.556510925292969e-07


Code source: 

.. code-block:: python 
   :linenos: table
   :linenostart: 1

   import sys
   import pyAgrum as gum
   for _ in range(2000):
       bn = gum.loadBN("data/"+sys.argv[1])