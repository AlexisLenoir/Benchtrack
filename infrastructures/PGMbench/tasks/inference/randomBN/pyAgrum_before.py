import sys
import pyAgrum as gum

nbrnode = int(sys.argv[1])
arcrate = int(sys.argv[2])
filename = f"data/bn{nbrnode}-0.{arcrate}.bif"
bn = gum.loadBN(filename)
