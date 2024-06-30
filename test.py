WALK = 0
TURNLEFT = 1
TURNRIGHT = 2
GRAB = 3
SHOOT = 4
CLIMB = 5

NORTH =0
EAST =1
SOUTH = 2
WEST =3

class KnowledgeBase():
    def __init__(self):
        self.kb = ['-P13', '-P21', '-P32', '-G31', '-G21', '-W13', '-G01', '-W22', '-W00', '-W23', '-P30', '-P03', '-W33', '-W11', '-G00', '-P33', '-P01', '-G02', 'W10', '-W20', '-G13', '-W30', '-P31', '-P11', '-W32', '-P10', '-P02', '-W01', '-W02', '-W02', 'P12', '-W12', '-P23', '-P20', '-G03', '-G23', '-P00', '-G11', '-W21', '-W31', '-G22']
        self.reward = 0
        self.playerDirection = None
        self.hasArrow = True
        self.wumpusDead = False
        self.hasGold = False
        self.bumped = False
    
    def negate(self,literal: str) -> str:
        if literal.startswith('-'):
            return literal[1:]
        else:
            return '-' + literal    
        
    #doesn't work propely
    def ask(self,query:str,timestamp:int=0)-> bool:
        assumptionList:list[str] = query.split(' v ') # list with assumptions like 'W20 v W31 v W22 v W11'
        
        factList = [] # list with facts like '-W12', '-W11, W10'
        for e in self.kb:
            if(' v ' not in e): # check wheter assumption or fact
                factList.append(e)
        print(f"Fact list {factList}")
        print(f"Assumption list {assumptionList}")
        removedCounter = 0
        for e_splitted in assumptionList:
            e_splitted_neg = self.negate(e_splitted)
            print(f"Current Element of assumption {e_splitted} --> {e_splitted_neg}")
            for fact in factList: # find facts that have to do with the assumption element
                if(e_splitted_neg == fact): # check if there are facts that contradict assumption element
                    removedCounter+=1 # remove part of the assumption
                    print(assumptionList)
                    break
        print(f"Assumption that remains{assumptionList}")
        
        if(len(assumptionList) == removedCounter):
            return False
        return True
    
kb = KnowledgeBase()

print(kb.ask('P22'))