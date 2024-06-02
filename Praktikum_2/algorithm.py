from board import *
import random
import math
class Algorithm():
    def __init__(self,population:list[str],isModelGenetic:bool=True,iterationsNumber:int=100):
        self.listQueensScores:list[list[str,int]] = self.initQueensScores(population)
        self.iterationsNumber = iterationsNumber
        self.isModelGenetic = isModelGenetic
        
        
        
    def start(self):
        if(self.isModelGenetic):
            self.geneticAlgorithm()
        else:
            self.backtrackingAlgorithm()
            
    
    #not tested  
    def geneticAlgorithm(self) -> list:
        """looks for best positioning of queens on chessboard

        Returns:
            list: list with data to visualize best score in each generation
        """
        stopFlag:bool = False
        board = Board()
        iterationCounter=0
        dataToVisualize=[]
        
        for _ in range(self.iterationsNumber):

            #initialize tmp variables
            newPopulation:list[list[str,int]] = []
            idx:int = 0
            generationBestFitVal:int = 0
            
            #check how fit every instance of population is
            for i in range(len(self.listQueensScores)):
                fitVal:int = self.checkAttacks(self.listQueensScores[i][0])
                self.listQueensScores[i][1] = fitVal
                if(generationBestFitVal < fitVal):
                    generationBestFitVal = fitVal
                    idx = i
                if(generationBestFitVal == 28):
                    stopFlag = True
            
            #display best individuum in current generation
            board.updateBoard(self.listQueensScores[idx][0])
            board.printBoard()
            print(f"Fit value of the best individuum in current generation is: {generationBestFitVal}")
            dataToVisualize.append(generationBestFitVal)
            
            #if positioning is good enough, break
            if(stopFlag):
                #print(f"NUMBER OF NEEDED GENERATIONS TO REACH 28 POINTS IS {iterationCounter}")
                break
            
            #create new generation
            for _ in range(len(self.listQueensScores)):
                x:str = self.selectRandom(self.listQueensScores)
                y:str = self.selectRandom(self.listQueensScores)
                child:str = self.reproduce(x,y)
                child = self.mutateByChance(child)
                newPopulation.append([child,0])
            self.listQueensScores = newPopulation
            iterationCounter+=1
        return dataToVisualize
            
    #not tested   
    def backtrackingAlgorithm(self):
        pass   
     
    # Done  
    def checkAttacks(self,queens:str)->int:
        """Checks who attacks who

        Args:
            queens (str): set of queens on board

        Returns:
            int: fitness value based on number of non-attacking queens
        """
        counter:int =0
        for i in range(len(queens)-1):
            for j in range(i+1,len(queens)):
                #vertical attack is impossible since 1 column can have only 1 queen
                
                #for horizontal attack values in string must be equal
                if(queens[i] == queens[j]):
                    counter+=1
                #for diagonal attack distance between indexes(columns) must be equal values(rows)
                if(abs(i-j)-abs(int(queens[i])-int(queens[j]))==0):
                    counter+=1
        #ideal score for 8 Queens is 28
        # result:int = math.comb(28-counter,2)
        result:int = 28-counter
        return result
    
    # Done
    def selectRandom(self,populationScore:list[list[str,int]])-> str:
        #remove element with worst fitness value
        sortedPopulationScore:list[list[str,int]] = sorted(populationScore,key=lambda x :x[1],reverse=True)[0:-1]
        #determine max value of random generated number
        maxValue:int = 0
        for _,val in sortedPopulationScore:
            maxValue+=val
        randomNumber:int = random.randint(0,maxValue)
        
        #determite what instance will be returned
        # the bigger fit value is, the better return chances instance have
        # example: [(EL1,17),(EL2,15),(EL3,10)]
        # random number is between 0 and sum of EL1,El2,El3. If number is {0;17} EL1 returned, if number is {18;33} EL2 returned
        idx:int =0
        while (randomNumber>0):
            randomNumber -= sortedPopulationScore[idx][1]
            if(randomNumber > 0):
                idx+=1
            
        return sortedPopulationScore[idx][0]
        
            
        
    # Done
    def reproduce(self,x:str,y:str)-> str:
        xList = []
        xList.append(x[0:int(len(x)/2)])
        xList.append(x[int(len(x)/2):len(x)])
        yList =[]
        yList.append(y[0:int(len(y)/2)])
        yList.append(y[int(len(y)/2):len(y)])
        
        newStr=''
        numb:int = random.randint(0,1)
        if(numb==1):
            newStr =xList[0]+yList[1]
        else:
            newStr = yList[0]+xList[1]
        return newStr
    
    # done
    def mutateByChance(self,x:str,mutationChance:float=0.05)->str:
        newStr=''
        for i in range(len(x)):
            number = random.random()
            if(number <= mutationChance):
                newStr+= str(random.randint(1,8))
            else:
                newStr+=x[i]
                # idx = random.randint(0,8)
                # val = random.randint(1,8)
                # x[idx] = str(val)
        return newStr
    
    
    def initQueensScores(self,population:list[str])-> list[list[str,int]]:
        newList =[]
        for i in population:
            tmp = [i,0]
            newList.append(tmp)
        
        
        return newList
    
        