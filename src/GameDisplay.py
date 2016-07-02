# This class handles the display
class GameDisplay(object):
    def __init__(self,pygame,display_width,display_height,display):  
        self.display_width = display_width
        self.display_height = display_height
		
        self.black = (0,0,0)
        self.white = (255,255,255)
        
        self.displayText = False
        
        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        self.font = pygame.font.SysFont("monospace", 15)
        self.mainTextX = 0
        self.mainTextY = 0
        self.scoreTextX = self.mainTextX
        self.scoreTextY = self.mainTextY + 10
        
        self.display = display
        
    def displayPlayer(self,player):
        self.display.blit(player.getImage(),(player.getX(),player.getY()))
        
    def displayTexts(self,generationID,playerID,score):
        mainString = 'GENERATION ' + str(generationID) + ' | PLAYER ' + str(playerID)
        scoreString = 'SCORE = ' + str(score)
        
        mainLabel = self.font.render(mainString, 1, self.black)
        scoreLabel = self.font.render(scoreString, 1, self.black)
        
        if self.displayText:
            self.display.blit(mainLabel, (self.mainTextX, self.mainTextY))
            self.display.blit(scoreLabel, (self.scoreTextX, self.scoreTextY))
        
    def update(self,pygame,player,obstacle,generationID,playerID,score):
        # RENDER
        self.display.fill(self.white)
        self.displayPlayer(player)
        pygame.draw.rect(self.display,self.black,(obstacle.getX(),obstacle.getY(),obstacle.getWidth(),obstacle.getHeight()))

        # render text
        self.displayTexts(generationID,playerID,score)
        		
        # UPDATE DISPLAY
        pygame.display.update()