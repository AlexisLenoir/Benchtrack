import sys
import pyAgrum as gum

# code to generate the random BN
#gen = gum.BNGenerator()
#for nbrnode in [10, 20, 30, 50, 70, 100]:
#  for arcrate in [0.1,0.3,0.5]:
#    bn=gen.generate(nbrnode, int(nbrnode * (1 + arcrate)), 3)
#    gum.saveBN(bn,f"data/bn{nbrnode}-{arcrate}.bif")

nbrnode = int(sys.argv[1])
arcrate = int(sys.argv[2])
filename = f"data/bn{nbrnode}-0.{arcrate}.bif"
bn = gum.loadBN(filename)

ie=gum.LazyPropagation(bn)
ie.makeInference()
for i in bn.nodes():
  print(ie.posterior(i))
