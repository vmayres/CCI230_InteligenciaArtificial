class Node():

    def __init__(self, pai = None, posicao =  None):
        self.pai = pai
        self.posicao = posicao
        
        self.g = 0
        self.h = 0
        self.f = 0
            