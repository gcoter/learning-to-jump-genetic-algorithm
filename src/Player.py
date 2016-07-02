# Defines a Player
class Player(object):
    def __init__(self,pygame,imagePath,x,y):
        self.x = x
        self.y = y
        self.isJumping = False
        
        self.image = pygame.image.load(imagePath)
        
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
        
    def isJumping(self):
        return self.isJumping
    
    def getImagePath(self):
        return self.imagePath
        
    def getImage(self):
        return self.image
        
    def setX(self,x):
        self.x = x
        
    def setY(self,y):
        self.y = y
        
    def setIsJumping(self,isJumping):
        self.isJumping = isJumping
        
    def move(self,x_change,y_change):
        newX = self.x + x_change
        
        if newX > 0:
            self.x += x_change  
        
        self.y += y_change
        