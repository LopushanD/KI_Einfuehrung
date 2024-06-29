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
        self.kb = ["-P00","-G00"]
        self.reward = 0
        self.playerDirection = None
        self.hasArrow = True
        self.wumpusDead = False
        self.hasGold = False
    
    def tell(self,newKnowledge:dict,reward:float,timestamp:int):
        self.playerDirection = newKnowledge["direction"].value
        # self.hasArrow = newKnowledge["arrow"]
        # self.hasGold = newKnowledge["gold"]
        # self.wumpusDead = newKnowledge['scream']
        x = newKnowledge["x"]
        y = newKnowledge["y"]
        
        isstench = newKnowledge["stench"]
        isbreeze = newKnowledge["breeze"]
        isglitter = newKnowledge["glitter"]
        # gold, direction, arrow,bump, scream not interesting for now
        result = ["","",""]
        
        # if not isgold:
        #     result[0]+='-'
        if not isstench:
            result[0]+='-'
        if not isbreeze:
            result[1]+='-'
        if not isglitter:
            result[2]+='-'
        
        result[0]+="S"
        result[1]+="B"
        result[2]+="G"
        
        gold = result[2]+str(x)+str(y)
        
        derivedKnowledge = self.derive(x,y,result[0:2])
        derivedKnowledge.append(gold)
        
        self.kb.extend(derivedKnowledge)
        self.kb=list(set(self.kb)) # needed to delete duplicates
        self.resolve()
        self.kb=list(set(self.kb)) # needed to delete duplicates
        
        if(not reward == -1000):
            self.kb.extend([f"-P{str(x)+str(y)}",f"-W{str(x)+str(y)}"])
        
    def derive(self,xPos:int,Ypos:int,newKnowledge:list[str])->list:
        result:list[str] = []
        # print(newKnowledge)
        for e in newKnowledge:
            tmp:list =[]
            # prefix=""
            
            
            # if(e[0] =='-'):
                # prefix='-'
                # e = e.removeprefix('-')
            #positions of possible pit/wumpus(x,y)

                
            if(xPos == 0):
                if(Ypos == 0):
                    if(e[0] =='-'):
                        tmp.extend([f"{e}01",f"{e}10"])
                    else:
                        tmp.extend([f"{e}01 v {e}10"])
                elif(Ypos == 3):
                    if(e[0] =='-'):
                        tmp.extend([f"{e}02",f"{e}13"])
                    else:
                        tmp.extend([f"{e}02 v {e}13"])
                else:
                    if(e[0] == '-'):
                        tmp.extend([f"{e}0{str(Ypos+1)}",f"{e}0{str(Ypos-1)}",f"{e}{str(xPos+1)}{str(Ypos)}"])
                        
                    else:
                        tmp.extend([f"{e}0{str(Ypos+1)} v {e}{str(xPos+1)}{str(Ypos)} v {e}0{str(Ypos-1)}"])
            elif(xPos == 3):
                if(Ypos == 0):
                    if(e[0] == '-'):
                        tmp.extend([f"{e}31",f"{e}20"])
                    else:
                        tmp.extend([f"{e}31 v {e}20"])
                        
                elif(Ypos == 3):
                    if(e[0] == '-'):
                        tmp.extend([f"{e}23",f"{e}32"])
                    else:
                        tmp.extend([f"{e}23 v {e}32"])                        
                else:
                    if(e[0] == '-'):
                        tmp.extend([f"{e}3{str(Ypos+1)}",f"{e}3{str(Ypos-1)}",f"{e}{str(xPos-1)}{str(Ypos)}"])

                    else:
                        tmp.extend([f"{e}3{str(Ypos-1)} v {e}{str(xPos-1)}{str(Ypos)} v {e}3{str(Ypos+1)}"])
                        
                        
            else:
                if(Ypos == 0):
                    if(e[0] == '-'):
                        tmp.extend([f"{e}{str(xPos+1)}0",f"{e}{str(xPos-1)}0",f"{e}{str(xPos)}1"])
                        
                    else:
                        tmp.extend([f"{e}{str(xPos-1)}0 v {e}{str(xPos)}1 v {e}{str(xPos+1)}0"])
                        
                elif(Ypos == 3):
                    if(e[0] == '-'):
                        tmp.extend([f"{e}{str(xPos+1)}3",f"{e}{str(xPos-1)}3",f"{e}{str(xPos)}2"])
                        
                    else:
                        tmp.extend([f"{e}{str(xPos-1)}3 v {e}{str(xPos)}2 v {e}{str(xPos+1)}3"])
                else:
                    if(e[0] == '-'):
                        tmp.extend([f"{e}{str(xPos)}{str(Ypos+1)}",f"{e}{str(xPos)}{str(Ypos-1)}",f"{e}{str(xPos-1)}{str(Ypos)}",f"{e}{str(xPos+1)}{str(Ypos)}"])
                        
                    else:
                        tmp.extend([f"{e}{str(xPos)}{str(Ypos-1)} v {e}{str(xPos+1)}{str(Ypos)} v {e}{str(xPos)}{str(Ypos+1)} v {e}{str(xPos-1)}{str(Ypos)}"])
                        
            result.extend(tmp)
            
        for i in range(len(result)):
            result[i] = result[i].replace('S','W')
            result[i] = result[i].replace('B','P')
            
        # print(f"result --> {result}")
            
        return result
    
    def resolve(self) -> None:
        assumptionList:list[str] =[] # list with assumptions like 'W20 v W31 v W22 v W11'
        factList = [] # list with facts like '-W12', '-W11, W10'
        for e in self.kb:
            if(' v 'in e): # check wheter assumption or fact
                assumptionList.extend(e.split(' v ')) # assumption 'W20 v W31 v W22 v W11' splitted into W20, W31, W22, W11
                self.kb.remove(e) # remove from knowledge base to return it later after resolving the assumption
            else:
                factList.append(e) 
        assumptionList = list(set(assumptionList)) # remove duplicates
        print(f"Fact list {factList}")
        print(f"Assumption list {assumptionList}")

        for e_splitted in assumptionList: 
            print(f"Current Element of assumption{e_splitted}")
            for fact in factList: # find facts that have to do with the assumption element
                if("-"+e_splitted == fact): # check if there are facts that contradict assumption element
                    # print(self.kb)
                    assumptionList.remove(e_splitted) # remove part of the assumption
        print(f"Assumption that remains{assumptionList}")
        self.kb.append(" v ".join(assumptionList)) # return assumption that was completely or partially resolved
        
    def ask(self,timestamp:int)-> int:
        pass
    
    def turn(self,side:str)->None:
        if(side=='R'):
            self.playerDirection = (self.playerDirection+1)%4
        elif(side=='L'):
            self.playerDirection = (self.playerDirection-1)%4