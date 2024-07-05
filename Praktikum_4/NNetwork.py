import numpy as np
import math
import pandas as pd
class NeuralNetwork():

    #initialize the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        #random(rows,cols), return ndarray
        self.inputToHiddenWeights = np.random.random((inputnodes,hiddennodes))
        self.hiddenToOutputWeights = np.random.random((hiddennodes,outputnodes))
        self.learningRate = learningrate
        

    #sigmoid function
    def sigmoid(self, x:np.ndarray):
        # result = 1 / (1+pow(1/math.e,x))
        result = 1 / (1+np.exp(-x))
        # print(f"AFTER CONVERTION {result}")
        return result
        

    #derivative of sigmoid function
    def sigmoid_derivative(self, x):
        # return self.sigmoid(x) * (1-self.sigmoid(x))
        sig = self.sigmoid(x)
        return sig * (1 - sig)
    
    #train the neural network
    def train(self, inputs:np.ndarray, targets:np.ndarray,learningRate):
        # vectorized_sig_deriv = np.vectorize(self.sigmoid_derivative)
        for iterations in range(100): # remove later, because it must work with
                                    #learning rate, not iterations
            hiddenInputs = self.think(inputs,self.inputToHiddenWeights)
            predicted = self.think(hiddenInputs,self.hiddenToOutputWeights) # array
            absErrorVect = np.subtract(targets,predicted)
            hiddenErrorVect = np.dot(self.hiddenToOutputWeights.T,absErrorVect)
            deltaWHiddenOutpMatrix = np.dot(np.multiply(absErrorVect,self.sigmoid_derivative(predicted)),hiddenInputs.T) # check if calculations here correct
            self.hiddenToOutputWeights+= np.multiply(learningRate,deltaWHiddenOutpMatrix)#update weights after hidden layer
            deltaWInputHiddenMartix = np.dot(np.multiply(hiddenErrorVect,self.sigmoid_derivative(hiddenInputs)),inputs.T)
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
    TrainingData = pd.read_csv("D:/downloads/P4_Dataset/mnist_train_100.csv",header=None)
    TrainingTargets = TrainingData.iloc[:,0].values
    TrainingInputs = TrainingData.iloc[:,1:].values
    
    print(TrainingInputs)
    # print(training_data_list)
    
    # test_data_file = open("D:/downloads/P4_Dataset/mnist_test_10.csv")
    # data is looks like ['1,230,0,33,0\n', '2,93,0,0,232\n', '...']
    # first number is label, other ones are pixel values
   
    # test_data_list = test_data_file.readlines()
    # test_data_file.close()
    # TestingTargets = []
    # TestingInputs = []
   
    # print(test_data_list)
    
    
    
    # for line in training_data_list:
    #     TrainingTargets.append(line[0])
    #     for e in line[1:]:
    #         if(e == ','):
    #             continue
    #         TrainingInputs.append(e)
    # # print(TrainingTargets[0:30])
    # # print(TrainingInputs)
    # print(training_data_list[0][1:][20])
    
    # n = NeuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)
    
    # n.train(TrainingInputs,TrainingTargets,learning_rate)
       