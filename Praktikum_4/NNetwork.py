import time
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

class NeuralNetwork():

    #initialize the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        #random(rows,cols), return ndarray
        self.inputToHiddenWeights = np.random.random((inputnodes,hiddennodes))
        self.hiddenToOutputWeights = np.random.random((hiddennodes,outputnodes))
        self.learningRate = learningrate
        

    # def sigmoid(self, x:np.ndarray):
    #     # result = 1 / (1+pow(1/math.e,x))
    #     result = 1 / (1+np.exp(-x))
    #     # print(f"AFTER CONVERTION {result}")
    #     return result
    
    # #sigmoid function
    def sigmoid(self, x: np.ndarray):
        # Clip the input values to a range that avoids overflow in the exp function (works also without it, but warning appears)
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
        # vectorized_sig_deriv = np.vectorize(self.sigmoid_derivative)
        for iterations in range(10**3): 
                                    #learning rate, not iterations
            hiddenInputs = self.think(inputs,self.inputToHiddenWeights)
            # print(np.shape(hiddenInputs))
            predicted = self.think(hiddenInputs,self.hiddenToOutputWeights) # array
            # print(np.shape(predicted))
            absErrorVect = np.subtract(targets,predicted)
            hiddenErrorVect = np.dot(absErrorVect,self.hiddenToOutputWeights.T)
            deltaWHiddenOutpMatrix = np.dot(hiddenInputs.T,np.multiply(absErrorVect,self.sigmoid_derivative(predicted))) # check if calculations here correct
            self.hiddenToOutputWeights+= np.multiply(learningRate,deltaWHiddenOutpMatrix)#update weights after hidden layer
            deltaWInputHiddenMartix = np.dot(inputs.T,np.multiply(hiddenErrorVect,self.sigmoid_derivative(hiddenInputs)))
            self.inputToHiddenWeights+= np.multiply(learningRate,deltaWInputHiddenMartix) # update weights after input layer
            
            
    #one calculation step of the network
    def think(self, inputs,weights) ->np.ndarray:
        """Makes step one layer to another (I -> H, H -> O)

        Returns:
            np.ndarray: array of in-between/output assumptions [0;1]
        """
        multiplied = np.dot(inputs,weights) #array x array  = array
        # vectorizedSigmoid = np.vectorize(self.sigmoid) # Makes scalar function to a vectorized one . upd not needed, vectorized by default
        result = self.sigmoid(multiplied) 
        return result
    
    def recognize(self,inputs:np.ndarray)-> np.ndarray:
        hiddenInputs = self.think(inputs,self.inputToHiddenWeights)
        predicted = self.think(hiddenInputs,self.hiddenToOutputWeights) # array
        
        return predicted
  
  
def normalizeInputs(inputs:np.ndarray):
    return (inputs / 254.0 * 0.99) + 0.01      
        
def oneHotEncode(labels, num_classes):
    one_hot = np.zeros((len(labels), num_classes)) + 0.01
    for i, label in enumerate(labels):
        one_hot[i][label] = 0.99
    return one_hot
        
if __name__ == "__main__":

    input_nodes = 784 #28*28 pixel
    hidden_nodes = 200 #voodoo magic number
    output_nodes = 10 #numbers from [0:9]

    learning_rate = 0.1 #feel free to play around with

    # training_data_file = open("D:/downloads/P4_Dataset/mnist_train_100.csv")
    # data is looks like ['1,230,0,33,0\n', '2,93,0,0,232\n', '...']
    # first number is label, other ones are pixel values
    # training_data_list = training_data_file.readlines()
    # training_data_file.close()
    
    # data is looks like ['1,230,0,33,0\n', '2,93,0,0,232\n', '...']
    # first number is label, other ones are pixel values
    TrainingData = pd.read_csv("D:/downloads/P4_Dataset/mnist_train_100.csv",header=None)
    TrainingTargets = TrainingData.iloc[:,0].values
    TrainingInputs = TrainingData.iloc[:,1:].values
    TrainingInputs = normalizeInputs(TrainingInputs)
    TrainingTargets = oneHotEncode(TrainingTargets,10)
    
    
    TestData = pd.read_csv("D:/downloads/P4_Dataset/mnist_test_10.csv",header=None)
    TestTargetsRaw = TestData.iloc[:,0].values
    TestInputsRaw = TestData.iloc[:,1:].values
    TestInputs = normalizeInputs(TestInputsRaw)
    TestTargets = oneHotEncode(TestTargetsRaw,10)
    # print(TestTargets.tolist()[0])
    # print(f"TEST INPUTS {np.shape(TestInputs)}\nTEST TARGETS {np.shape(TestTargets)}\n TRAINING INPUTS {np.shape(TrainingInputs)}\nTRAINING TARGETS {np.shape(TrainingTargets)}\n")  
    n = NeuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)
    start = time.time()
    n.train(TrainingInputs,TrainingTargets,learning_rate)
    end = time.time()
    print(f"TIME NEEDED FOR TRAINING {(end-start)//60}:{(end-start)%60:.2f}")
    
    
    results = n.recognize(TestInputs)
    # print(TestTargets.tolist())
    totalRecognitions = len(TestInputs)
    correctRecognitions = 0
    # print(results.__len__())
    whatPredicted = results.max(0)
    whatCorrect = TestTargets.max(0) # returns max value from each example in ndarray
    #Now need to find index of this value (index = number that is correct)
    #do same for predicted number and compare those indexes. if same -> predicted correctly, otherwise incorrectly
        
    image_array = np.reshape(TestInputsRaw[1],(28,28)) # print 2nd example
    plt.imshow(image_array,cmap='Greys', interpolation='None')
    plt.show()
    