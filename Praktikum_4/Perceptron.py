import random
import numpy as np
import math
import time
class Perceptron:
    
    
    def __init__(self):
        tmp = [0,0,0]
        for i in range(3):
            tmp[i] = random.random()
        self.synaptic_weights = np.array(tmp)
        
            
            
    def sigmoid(self,x):
        result = 1 / (1+np.exp(-x))
        # print(f"AFTER CONVERTION {result}")
        return result
    
    def sigmoid_derivative(self,x):
        return self.sigmoid(x) * (1-self.sigmoid(x))
    
    def think(self,inputs:str):
        arr = self.toNumpyArr(inputs)
        multiplied = np.dot(self.synaptic_weights,arr)
        result = self.sigmoid(multiplied)
        
        return result
    
    def toNumpyArr(self,arrStr:str)->np.ndarray:
        arr = np.array([],dtype=int)
        for e in arrStr:
            arr = np.append(arr,int(e))
        return arr
    
    def train(self,inputs:list[str],targets:list[str|int],iterations:int)->None:
        for iterations in range(iterations):
            for i in range(len(inputs)):
                input = inputs[i]
                target = int(targets[i])
                predicted = self.think(input)
                error = target - predicted
                correction = (error * self.sigmoid_derivative(predicted)) * self.toNumpyArr(input).T
                # print(f"TARGET -> {target}\t PREDICTED ->{predicted}\t CORRECTION->{correction}\n")
                self.synaptic_weights = np.add(self.synaptic_weights,correction)
                
            
    
if __name__ == "__main__":
    training_data = [["001","111","100","011"],["0","1","1","0"]]
    iterationNumber = 1000
    perceptron = Perceptron()
    print(perceptron.synaptic_weights)
    start = time.time()
    perceptron.train(training_data[0],training_data[1],iterationNumber)
    end = time.time()
    print(f"TIME NEEDED FOR TRAINING {(start-end)//60}:{(start-end)%60}")
    print(perceptron.synaptic_weights)
    unseen_data = ["000","010","101","010"]
    # for e in unseen_data:
    #     print(perceptron.think(e))
    while(True):
        example = str(input("Input your values xxx"))
        print(perceptron.think(example))
    #run the perceptron
    
    # perc = Perceptron()
    # perc.think("010")
    
