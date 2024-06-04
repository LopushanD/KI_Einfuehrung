from board import *
class BacktrackingAlgorithm():
    def __init__(self,population:list[str]):
        self.listQueensScores:list[list[str,int]] = self.initQueensScores(population)
        
        
        