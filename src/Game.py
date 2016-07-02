from random import randint
from Player import Player
from Obstacle import Obstacle

# This class defines the game's logic and contains all the useful information
class Game(object):
    def __init__(self,pygame,maxHeight,display_width,display_height,timeCoef,player=None):
        self.timeCoef = timeCoef
        
        x0 = (display_width * 0)
        y0 = (display_height * 0.8)
        
        self.gameOver = False
        self.winner = False
        self.maxHeight = maxHeight
        self.x_speed = 5 * self.timeCoef
        self.y_speed = self.maxHeight
        
        self.y_max = self.maxHeight * (self.maxHeight - 1) - 1
        
        self.distance = 0
        
        self.artificial = (player != None)
        
        if self.artificial:
            self.player = player
        else:            
            self.player = Player(pygame,'../img/player.png',x0,y0)
            
        xObstacle = randint(0.2*display_width,0.8*display_width - 10)
        yObstacle = display_height * 0.8 - (maxHeight * (maxHeight - 1) - 1) * 0.3 + self.player.getImage().get_rect().size[1]
        obstacleWidth = 10
        obstacleHeight = self.y_max * 0.3        
        
        self.obstacle = Obstacle(xObstacle,yObstacle,obstacleWidth,obstacleHeight)
        
        self.time_max = 4 / float(self.timeCoef)
        self.time = self.time_max #time in seconds
        
    def getPlayer(self):
        return self.player
        
    def getObstacle(self):
        return self.obstacle
        
    def fitnessFunction(self):
        if self.winner:
            return 1 + float(self.distance)/(self.time_max * self.timeCoef - self.time + 1)
        else:
            return 1 + float(self.distance)/(self.time_max * self.timeCoef + 1)
            
    def manageEvents(self,pygame):
        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameOver = True
            if event.type == pygame.USEREVENT+1:
                self.time -= 1
                
        x_change = 0
        
        if self.artificial:
            decisions =  self.player.getDecisions(self.obstacle)
            
            if decisions[0] > 0.5: 
                x_change = -self.x_speed
            elif decisions[1] > 0.5:
                x_change = self.x_speed            
            if decisions[2] > 0.5:
                if not self.player.isJumping:
                    self.player.setIsJumping(True)
        else:
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]: 
                x_change = -self.x_speed
            elif key[pygame.K_RIGHT]:
                x_change = self.x_speed            
            if key[pygame.K_UP]:
                if not self.player.isJumping:
                    self.player.setIsJumping(True)
                    
        return x_change
        
    def update(self,pygame,display_width):
        
        x_change = self.manageEvents(pygame)
        y_change = 0
        
        if self.player.getX() > self.distance:
            self.distance = self.player.getX()                    
                
        if self.player.isJumping:
            y_change = -self.y_speed * self.timeCoef
            if self.y_speed <= -self.maxHeight:
                self.player.setIsJumping(False)
                self.y_speed = self.maxHeight
            else:
                self.y_speed -= self.timeCoef
                
        if self.obstacle.isTouched(self.player,self.player.getImage()):
            self.gameOver = True
            
        if self.player.getX() + self.player.getImage().get_rect().size[0] > display_width:
            self.gameOver = True
            self.winner = True
            
        if self.time == 0:
            self.gameOver = True
                
        self.player.move(x_change,y_change)