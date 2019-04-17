import numpy as np
import pandas as pd



class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x  #Input to network

        #(What do I initialize these with?)
        self.weights1 =[] #Weights of First Layer 
        self.weights2 =[] #Weights of Second Layer



        self.y = y      #Estimate of y
        self.output = np.zeros(y.shape)

    def feedforward(self)

        # Activation function applied to layer and feeding it forward to the next layer

        self.firstlayer = sigmoid()
        self.output = sigmoid()
