import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

class NeuralNetwork():

    #initialize the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inputToHiddenWeights = np.random.random((inputnodes,hiddennodes))
        self.hiddenToOutputWeights = np.random.random((hiddennodes,outputnodes))
        self.learningRate = learningrate

    
    # #sigmoid function
    def sigmoid(self, x: np.ndarray):
        # Clip the input values to a range that avoids overflow in the exp function (works also without it, but warning appears)
        # for exponent is same as infinity or zero
        x = np.clip(x, -709, 709)
        result = 1 / (1 + np.exp(-x))
        return result
        

    #derivative of sigmoid function
    def sigmoid_derivative(self, x):
        # return self.sigmoid(x) * (1-self.sigmoid(x))
        sig = self.sigmoid(x)
        return sig * (1 - sig)
    
    #train the neural network
    def train(self, inputs:np.ndarray, targets:np.ndarray,learningRate):
        for iterations in range(16000): 
            
            hiddenInputs = self.think(inputs,self.inputToHiddenWeights)
            # print(np.shape(hiddenInputs))
            predicted = self.think(hiddenInputs,self.hiddenToOutputWeights) # array
            # print(np.shape(predicted))
            absErrorVect = np.subtract(targets,predicted)
            hiddenErrorVect = np.dot(absErrorVect,self.hiddenToOutputWeights.T)
            deltaWHiddenOutpMatrix = np.dot(hiddenInputs.T,np.multiply(absErrorVect,self.sigmoid_derivative(predicted))) 
            #update weights after hidden layer
            self.hiddenToOutputWeights+= np.multiply(learningRate,deltaWHiddenOutpMatrix)
            deltaWInputHiddenMartix = np.dot(inputs.T,np.multiply(hiddenErrorVect,self.sigmoid_derivative(hiddenInputs)))
            #update weights after hidden layer
            self.inputToHiddenWeights+= np.multiply(learningRate,deltaWInputHiddenMartix)
            
            
    #one calculation step of the network
    def think(self, inputs,weights) ->np.ndarray:
        """Makes step one layer to another (I -> H, H -> O)

        Returns:
            np.ndarray: array of in-between/output assumptions [0;1]
        """
        multiplied = np.dot(inputs,weights) #array x array  = array
        result = self.sigmoid(multiplied) 
        return result
    
    def recognize(self,inputs:np.ndarray)-> np.ndarray:
        hiddenInputs = self.think(inputs,self.inputToHiddenWeights)
        predicted = self.think(hiddenInputs,self.hiddenToOutputWeights)
        
        return predicted
  
  
def normalizeInputs(inputs:np.ndarray):
    return (inputs / 254.0 * 0.99) + 0.01      
        
def oneHotEncode(labels, num_classes):
    one_hot = np.zeros((len(labels), num_classes)) + 0.01
    for i, label in enumerate(labels):
        one_hot[i][label] = 0.99
    return one_hot

def writeNetworkToFile(network:NeuralNetwork,filename:str="D:/downloads/P4_Dataset/TrainedNeuralNetwork.pkl")->None:
        with open(filename, 'wb') as file:
            pickle.dump(network, file)
            file.close()
            
def loadNetworkFromFile(filename:str="D:/downloads/P4_Dataset/TrainedNeuralNetwork.pkl")->NeuralNetwork:
    with open(filename, 'rb') as file:
        loadedNeuralNetwork = pickle.load(file)
        file.close()
    return loadedNeuralNetwork
        
if __name__ == "__main__":

    input_nodes = 784 #28*28 pixel
    hidden_nodes = 200 #voodoo magic number
    output_nodes = 10 #numbers from [0:9]

    learning_rate = 0.03 #feel free to play around with

    # first number is label, other ones are pixel values
    TrainingData = pd.read_csv("D:/downloads/P4_Dataset/mnist_train_full.csv",header=None)
    TrainingTargets = TrainingData.iloc[:,0].values
    TrainingInputs = TrainingData.iloc[:,1:].values
    TrainingInputs = normalizeInputs(TrainingInputs)
    TrainingTargets = oneHotEncode(TrainingTargets,10)
    
    TestData = pd.read_csv("D:/downloads/P4_Dataset/mnist_test_full.csv",header=None)
    TestTargetsRaw = TestData.iloc[:,0].values
    TestInputsRaw = TestData.iloc[:,1:].values
    TestInputs = normalizeInputs(TestInputsRaw)
    TestTargets = oneHotEncode(TestTargetsRaw,10)
   
    n = NeuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)
    start = time.time()
    n.train(TrainingInputs,TrainingTargets,learning_rate)
    end = time.time()
    print(f"TIME NEEDED FOR TRAINING {(end-start)//60}:{(end-start)%60:.2f}")
    
    
    results = n.recognize(TestInputs)
    totalRecognitions = len(TestInputs)
    
    whatPredicted = np.argmax(results,axis=1) # returns index of max value from each example in ndarray
    whatCorrect = np.argmax(TestTargets,axis=1) # returns index of max value from each example in ndarray
    # print(f"{whatPredicted}"+'\n'+f"{whatCorrect}")
    correctRecognitions = np.sum((whatPredicted == whatCorrect)) #compare indexes and sum up matches
    accuracyPercentage = correctRecognitions/totalRecognitions*100
    print(f" The accuracy of prediction is {accuracyPercentage}%")
    writeNetworkToFile(n)
    
    # image_array = np.reshape(TestInputsRaw[1],(28,28)) # print 2nd example
    # plt.imshow(image_array,cmap='Greys', interpolation='None')
    # plt.show()
    