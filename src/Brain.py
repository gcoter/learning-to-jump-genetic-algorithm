import numpy as np

# Defines a MultiLayerPerceptron
class Brain(object):
    def __init__(self,dims,params=None):
        self.dims = dims
        
        # Parameters
        self.weights = []
        
        # Weights (parameters)
        for id in range(len(self.dims)-1):
            self.weights.append(np.random.randn(dims[id],dims[id+1]))
        
        if not params is None:
            self.setParams(params)
        
    def forward(self, X):
        M = X
        
        for id in range(0,len(self.weights)):
            M = np.dot(M, self.weights[id])
            
        return self.sigmoid(M)
    
    def sigmoid(self, z):
        return 1/(1+np.exp(-z))
        
    def getDecisions(self, X):
        return self.forward(np.array((X), dtype=float))
    
    # Returns a single vector that contains all weights
    def getParams(self):
        params = self.weights[0].ravel()
        
        for id in range(len(self.weights)-1):
            params = params = np.concatenate((params, self.weights[id+1].ravel()))
    
        return params
    
    # Set weights using single paramater vector
    def setParams(self, params):
        start = 0
        end = 0        
        
        for id in range(len(self.dims)-1):
            end += self.dims[id] * self.dims[id+1]
            self.weights[id] = np.reshape(params[start:end], (self.dims[id] , self.dims[id+1]))
            start = end