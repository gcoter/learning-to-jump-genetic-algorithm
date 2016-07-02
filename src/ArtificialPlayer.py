"""
@author: Guillaume COTER
"""
from Brain import Brain
from Player import Player

# Defines an Artificial Player (AP), which is a Player
class ArtificialPlayer(Player):
    def __init__(self,pygame,imagePath,x,y,dims,chromosome=None):
        Player.__init__(self,pygame,imagePath,x,y)
        
        self.brain = Brain(dims,chromosome)
        
    # an AP has one sensor to his left and one to his right
    # they are able to detect the obstacle and the left screen side
    def detect(self,obstacle):
        sensorLeft = 0
        sensorRight = 0
        
        distance = obstacle.getX() - (self.x + self.image.get_rect().size[0])
        
        if (-distance > 0 and -distance < 50) or self.x < 50:
            sensorLeft = 1
        
        if distance > 0 and distance < 50:
            sensorRight = 1
        
        return [sensorLeft,sensorRight]
        
    def getDecisions(self,obstacle):
        return self.brain.getDecisions(self.detect(obstacle))
        
    def getChromosome(self):
        return self.brain.getParams()
        