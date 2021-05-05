import sys
import pyAgrum as gum
print("argv2:",sys.argv[2])
bn = gum.loadBN("data/"+sys.argv[1])
