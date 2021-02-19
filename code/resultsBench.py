#class pour enregister des resultat de Bench
class ResultsBench:
    def __init__(self,name):
        self.benchName = name
        self.listTargets = []
        self.listTemps = []
    def __str__(self):
        str = "BenchName:"+self.benchName+",Targets:\n"
        for i in range(len(self.listTargets)):
            str += "Num"+i.__str__() + ":"+self.listTargets[i]+":"+self.listTemps[i].__str__()+"\n"
        return str
    def add_target(self,name,temp):
        self.listTargets.append(name)
        self.listTemps.append(temp)