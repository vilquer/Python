from class_tiavelha import *
class tiafofoqueira(TiaVelha):
    def __init__(self,nome,idade):
        TiaVelha.__init__(self,nome, idade)
        self.fofocas=[]
 
    def leva(self,fofoca):
        self.fofocas.append(fofoca)
 
    def traz(self):
        for fofoca in self.fofocas:
            print(fofoca)