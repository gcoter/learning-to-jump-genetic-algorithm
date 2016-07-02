"""
@author: Guillaume COTER
"""
#************************* MAIN CODE *********************************
from Game import Game
from GameDisplay import GameDisplay
from ArtificialPlayer import ArtificialPlayer
import numpy as np
import matplotlib.pyplot as plt
import pygame

#========================INITIALIZATIONS==============================
pygame.init()

# Constants
title = 'Jump' # window's title
display_width = 800 # window's width
display_height = 200 # window's height
maxHeight = 15 
image_path = '../img/player.png'
timeCoef = 2 # modifies the simulation's speed (ex: if 2, speed is doubled)

nbGenerations = 5 # number of generations
nbPlayersPerGeneration = 20 # number of players per generations
shape = [2,2,3] # defines the shape of the perceptron : each value is the number of nodes in the corresponding layer
probCrossover = 0.72 # probability that a crossover occurs
probMutation = 0.06 # probability that a mutation occurs
mutationImpact = 0.5 # how much will be added or substracted to a gene value when a mutation occurs

displayOn = True # when true, a window displays the simulation. Otherwise, it is not displayed

if displayOn:
    # Display object
    display = pygame.display.set_mode((display_width,display_height))
    gameDisplay = GameDisplay(pygame,display_width,display_height,display)
    pygame.display.set_caption(title)

clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT+1, 1000)#1 second is 1000 milliseconds

#============================FUNTIONS=================================
def runAGame(player,generationID=0,playerID=0):
    # Init
    currentGame = Game(pygame,maxHeight,display_width,display_height,timeCoef,player)
    
    while not currentGame.gameOver:
        # UPDATE MODEL
        currentGame.update(pygame,display_width)
            
        # RENDER
        if displayOn:
            gameDisplay.update(pygame,currentGame.getPlayer(),currentGame.getObstacle(),generationID,playerID,currentGame.fitnessFunction())
            
        # TICK
        clock.tick(60)
    
    return currentGame.fitnessFunction()

# return the total of scores obtained by the previous generation
def getSum(resultsFromPreviousGeneration):
    sum = 0
    for i in range(len(resultsFromPreviousGeneration)):
        sum += resultsFromPreviousGeneration[i][1]
        
    return sum
    
# return the probability that a player is chosen for reproduction
# p = (player performance) / (total of scores obtained by the previous generation)
def getProbs(resultsFromPreviousGeneration):
    probs = []
    sum = getSum(resultsFromPreviousGeneration)
        
    for i in range(len(resultsFromPreviousGeneration)):
        probs.append(resultsFromPreviousGeneration[i][1]/sum)
        
    return probs
    
# return a chromosome after a crossover with another chromosome
def crossover(chromosome1,chromosome2,probCrossover):
    if np.random.uniform() < probCrossover:
        #print '********************************'
        #print 'Crossover !'            
        #print '********************************'
        idxCrossover = np.random.randint(len(chromosome1))
        
        for i in range(idxCrossover,len(chromosome1)):
            chromosome1[i] = chromosome2[i]
            
    return chromosome1
    
# return a chromosome after mutations
def mutation(chromosome,probMutation):
    for i in range(len(chromosome)):    
        if np.random.uniform() < probMutation:
            #print '********************************'
            #print 'Mutation !'            
            #print '********************************'
            plus = (np.random.randint(2) == 0)
            
            if plus:
                chromosome[i] += mutationImpact
            else:
                chromosome[i] -= mutationImpact
                
    return chromosome 

# construct and return a new generation of players
def getNewGeneration(nbPlayersPerGeneration,resultsFromPreviousGeneration,shape,image_path):
    probs = getProbs(resultsFromPreviousGeneration)
    newGeneration = []
    
    for p in range(nbPlayersPerGeneration):
        idx = np.random.choice(nbPlayersPerGeneration,1,p=probs)[0]
        while idx == p:
            idx = np.random.choice(nbPlayersPerGeneration,1,p=probs)[0]
            
        newChromosome = crossover(resultsFromPreviousGeneration[p][0],resultsFromPreviousGeneration[idx][0],probCrossover)
        newChromosome = mutation(newChromosome,probMutation)
        
        newGeneration.append(ArtificialPlayer(pygame,image_path,(display_width * 0),(display_height * 0.8),shape,newChromosome))
        
    return newGeneration

# MAIN FUNCTION : it simulates an evolution process and returns all the scores
def evolution(nbGenerations,nbPlayersPerGeneration,shape,image_path):  
    allScores = []
    
    # res = [[chromosome,fitnessFunction],...]
    res = []
    generationScores = []
    for p in range(nbPlayersPerGeneration):
        print 'GENERATION 0 | PLAYER ' + str(p)
        ap = ArtificialPlayer(pygame,image_path,(display_width * 0),(display_height * 0.8),shape)
        score = runAGame(ap,0,p)
        print 'Score = ' + str(score)
        ap.printDecisions()
        generationScores.append(score)
        res.append([ap.getChromosome(),score])
        
    print '======================================'
    allScores.append(generationScores)
    generation = getNewGeneration(nbPlayersPerGeneration,res,shape,image_path)
    res = []
    generationScores = []
    
    for g in range(1,nbGenerations):
        #print '======================================'
        for p in range(nbPlayersPerGeneration):
            print 'GENERATION ' + str(g) + ' | PLAYER ' + str(p)
            ap = generation[p]
            score = runAGame(ap,g,p)
            res.append([ap.getChromosome(),score])
            print 'Score = ' + str(score)
            ap.printDecisions()
            generationScores.append(score)
        
        print '======================================'
        allScores.append(generationScores)
        generation = getNewGeneration(nbPlayersPerGeneration,res,shape,image_path)
        res = []
        generationScores = []
        
    return allScores
    
# return the average score
def getAvgScores(allScores):
    res = []
    for i in range(len(allScores)):
        total = 0
        for j in range(len(allScores[i])):
            total += allScores[i][j]
            
        res.append( (i, float(total)/len(allScores[i])) )
        
    return res

#=========================MAIN CODE===================================
allScores = evolution(nbGenerations,nbPlayersPerGeneration,shape,image_path)
avgScores = getAvgScores(allScores)
print "Avarage scores : " + str(avgScores)

pygame.quit()

# PLOT
plt.scatter(*zip(*avgScores))
plt.show()