import numpy as np

# Defines a "brain"
# The implementation is based on neural network but only to forward input
# There is no training using back propagation
# Training is made by the genetic algorithm which selects the best parameters for this brain
# Parameters stand for genes here
class Brain(object):
    def __init__(self,dims,params=None):
        self.dims = dims
        
        # Parameters
        self.weights = []
        
        # Weights (parameters)
        for id in range(len(self.dims)-1):
            self.weights.append(np.random.randn(dims[id],dims[id+1]))
        
        if not params is None:
            self.setParameters(params)
        
    def forward(self, X):
        M = X
        
        # Transition between two layers :
        # newInput = oldInput . weights (matrix multiplication)
        for id in range(0,len(self.weights)):
            M = np.dot(M, self.weights[id])
            
        return self.sigmoid(M) # sigmoid returns a vector with values between 0 and 1
    
    def sigmoid(self, z):
        return 1/(1+np.exp(-z))
        
    def getDecisions(self, X):
        return self.forward(np.array((X), dtype=float))
    
    # Returns a single vector that contains all weights
    def getParameters(self):
        params = self.weights[0].ravel()
        
        for id in range(len(self.weights)-1):
            params = params = np.concatenate((params, self.weights[id+1].ravel()))
    
        return params
    
    # Set weights using single paramater vector
    def setParameters(self, parameters):
        start = 0
        end = 0        
        
        for id in range(len(self.dims)-1):
            end += self.dims[id] * self.dims[id+1]
            self.weights[id] = np.reshape(parameters[start:end], (self.dims[id] , self.dims[id+1]))
            start = end