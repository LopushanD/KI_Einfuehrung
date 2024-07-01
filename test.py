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
        self.kb = ['-P10', '-W20', 'W10', '-W01', '-P00', '-G00', '-G13', '-P02', 'P12', '-G11', '-W03', 'P32 v P12 v P01', '-G23', '-P01', '-G03', '-W13', '-P20', '-P33', '-G21', '-W22', '-G22', '-W31', '-P21', '-P23', '-G01', '-P03', '-W23', '-P13', '-W32', '-P11', '-W21', '-W12', '-W00', '-W02', '-W11', '-W33', '-P22', '-G02', '-P31']

        self.reward = 0
        self.playerDirection = None
        self.hasArrow = True
        self.wumpusDead = False
        self.hasGold = False
        self.bumped = False
        self.wumpusFound = False
    
    def tell(self,newKnowledge:dict,reward:float,timestamp:int=0):
        
        self.playerDirection = newKnowledge["direction"].value
        self.hasArrow = newKnowledge["arrow"]
        self.hasGold = newKnowledge["gold"]
        self.wumpusDead = newKnowledge['scream']
        self.bumped = newKnowledge['bump']
        x = newKnowledge["x"]
        y = newKnowledge["y"]
        isstench = newKnowledge["stench"]
        isbreeze = newKnowledge["breeze"]
        isglitter = newKnowledge["glitter"]
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
        #makes logical resolution (what implies what)
        derivedKnowledge.append(gold)
        
        # checks if our current tile is safe and adds this info to the knowledge base
        if(not reward == -1000):
            self.kb.extend([f"-P{str(x)+str(y)}",f"-W{str(x)+str(y)}"])
        derivedKnowledge = self.derive(x,y,result[0:2])
        
        self.kb.extend(derivedKnowledge)
        self.kb=list(set(self.kb)) # needed to delete duplicates
        # self.resolve()
        # self.kb=list(set(self.kb)) # needed to delete duplicates
        
        
    def derive(self,xPos:int,Ypos:int,newKnowledge:list[str])->list:
        result:list[str] = []
        for e in newKnowledge:
            tmp:list =[]
                            
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
            
        # give wumpus/pits their proper names in knowledge base
        for i in range(len(result)):
            result[i] = result[i].replace('S','W')
            result[i] = result[i].replace('B','P')
            
        # if we already have facts about added assumption
        before = []
        before.extend(result)
        for e in self.kb:
            if(" v " not in e):
                ###print(f"e -->{e}")
                
                for i in range(len(result)):
                    tmp:list[str] = result[i].split(" v ")
                    for e2 in result[i].split(" v "):
                            if("-"+e == e2):
                                tmp.remove(e2)
                    if(len(tmp)>0):
                        result[i] = ' v '.join(tmp)
        print(result)
        after = []
        after.extend(result)
        if(len(before) > len(after)):
            print(f"IN DERIVE() THE FOR LOOP HAS DONE SOMETHING\n{before}\n{after}")                
        #print(f"result --> {result}")
            
        return result
    
    def askNew(self, querry:list[str]=[]) -> bool:
        assumptionList = querry
        factList = [] # list with facts like '-W12', '-W11, W10'
        if(len(querry)==0):#automatic querry for agent's assumptions   
            for e in self.kb[:]:
                if(' v 'in e): # check wheter assumption or fact
                    assumptionList.extend(e.split(' v ')) # assumption 'W20 v W31 v W22 v W11' splitted into W20, W31, W22, W11
                    self.kb.remove(e) # remove from knowledge base to return it later after resolving the assumption
                else:
                    factList.append(e) 
        else: # manual querry by user
            
            for e in self.kb[:]:
                if(not ' v 'in e): # check wheter assumption or fact
                    factList.append(e) 
        assumptionList = list(set(assumptionList)) # remove duplicates

        for e_splitted in assumptionList: 
            # print(f"Current Element of assumption {e_splitted}")
            for fact in factList: # find facts that have to do with the assumption element
                if("-"+e_splitted == fact): # check if there are facts that contradict assumption element
                    # print(self.kb)
                    assumptionList.remove(e_splitted) # remove part of the assumption
        #print(f"Assumption that remains{assumptionList}")
        
        if(len(assumptionList)>0):
            wumpusAssumptionList = []
            pitAssumptionList = []
            for assumption in assumptionList:
                if(assumption[0] == "W"):
                    wumpusAssumptionList.append(assumption)
                else:
                    pitAssumptionList.append(assumption)
            
            if(len(wumpusAssumptionList)>0):
                tmp = " v ".join(wumpusAssumptionList)
                if(not self.wumpusFound):
                    if(" v "not in tmp):
                        self.wumpusFound = True
                    self.kb.append(tmp) # add assumption that was completely or partially resolved
            if(len(pitAssumptionList)>0):
                self.kb.append(" v ".join(pitAssumptionList)) # add assumption that was completely or partially resolved
            self.kb=list(set(self.kb)) # needed to delete duplicates
            
            return True
        self.kb=list(set(self.kb)) # needed to delete duplicates
        return False
    
    # has same function as ask method (but suits task description better)
    def askOld(self) -> None:
        assumptionList:list[str] =[] # list with assumptions like 'W20 v W31 v W22 v W11'
        factList = [] # list with facts like '-W12', '-W11, W10'
        
        for e in self.kb[:]:
            if(' v 'in e): # check wheter assumption or fact
                assumptionList.extend(e.split(' v ')) # assumption 'W20 v W31 v W22 v W11' splitted into W20, W31, W22, W11
                self.kb.remove(e) # remove from knowledge base to return it later after resolving the assumption
            else:
                factList.append(e) 
        assumptionList = list(set(assumptionList)) # remove duplicates
        #print(f"Fact list {factList}")
        #print(f"Assumption list {assumptionList}")

        for e_splitted in assumptionList: 
            # print(f"Current Element of assumption {e_splitted}")
            for fact in factList: # find facts that have to do with the assumption element
                if("-"+e_splitted == fact): # check if there are facts that contradict assumption element
                    # print(self.kb)
                    assumptionList.remove(e_splitted) # remove part of the assumption
        #print(f"Assumption that remains{assumptionList}")
        
        if(len(assumptionList)>0):
            wumpusAssumptionList = []
            pitAssumptionList = []
            for assumption in assumptionList:
                if(assumption[0] == "W"):
                    wumpusAssumptionList.append(assumption)
                else:
                    pitAssumptionList.append(assumption)
            if(len(wumpusAssumptionList)>0):
                tmp = " v ".join(wumpusAssumptionList)
                if(not self.wumpusFound):
                    if(" v "not in tmp):
                        self.wumpusFound = True
                    self.kb.append(tmp) # add assumption that was completely or partially resolved
            if(len(pitAssumptionList)>0):
                self.kb.append(" v ".join(pitAssumptionList)) # add assumption that was completely or partially resolved
                
        
    # def ask(self,query:str,timestamp:int=0)-> bool:
    #     pass
    
    # def turn(self,side:str)->None:
    #     if(side=='R'):
    #         self.playerDirection = (self.playerDirection+1)%4
    #     elif(side=='L'):
    #         self.playerDirection = (self.playerDirection-1)%4



kb = KnowledgeBase()
# [ St: True, Br: True, G: False, Bu: False, Sc: False ]
kb.derive(1,1,["-S",'-B'])
