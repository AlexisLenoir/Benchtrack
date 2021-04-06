import sys
import pyAgrum as gum
for _ in range(2000):
    bn = gum.loadBN("data/"+sys.argv[1])
