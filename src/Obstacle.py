"""
@author: Guillaume COTER
"""
# Defines an obstacle
class Obstacle(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
        
    def getHeight(self):
        return self.height
        
    def getWidth(self):
        return self.width
        
    def isTouched(self,player,playerImg):
        if player.getX() + playerImg.get_rect().size[0] > self.x and player.getX() < self.x + self.width:
            if player.getY() + playerImg.get_rect().size[1] > self.y:
                return True
            else:
                return False
        else:
            return False