import numpy as np
from Game import Game
from ArtificialPlayer import ArtificialPlayer

display_width = 800
display_height = 200

def getSum(resultsFromPreviousGeneration):
    sum = 0
    for i in range(len(resultsFromPreviousGeneration)):
        sum += resultsFromPreviousGeneration[i][1]
        
    return sum
    
def getProbs(resultsFromPreviousGeneration):
    probs = []
    sum = getSum(resultsFromPreviousGeneration)
        
    for i in range(len(resultsFromPreviousGeneration)):
        probs.append(resultsFromPreviousGeneration[i][1]/sum)
        
    return probs
    
def crossover(chromosome1,chromosome2,probCrossover):
    if np.random.uniform() < probCrossover:
        print '********************************'
        print 'Crossover !'            
        print '********************************'
        idxCrossover = np.random.randint(len(chromosome1))
        
        for i in range(idxCrossover,len(chromosome1)):
            chromosome1[i] = chromosome2[i]
            
    return chromosome1
    
def mutation(chromosome,probMutation):
    for i in range(len(chromosome)):    
        if np.random.uniform() < probMutation:
            print '********************************'
            print 'Mutation !'            
            print '********************************'
            plus = (np.random.randint(2) == 0)
            
            if plus:
                chromosome[i] += 0.5
            else:
                chromosome[i] -= 0.5
                
    return chromosome 

def getNewGeneration(nbPlayersPerGeneration,resultsFromPreviousGeneration,shape):
    probs = getProbs(resultsFromPreviousGeneration)
    newGeneration = []
    
    for p in range(nbPlayersPerGeneration):
        idx = np.random.choice(nbPlayersPerGeneration,1,p=probs)[0]
        while idx == p:
            idx = np.random.choice(nbPlayersPerGeneration,1,p=probs)[0]
            
        newChromosome = crossover(resultsFromPreviousGeneration[p][0],resultsFromPreviousGeneration[idx][0],0.7)
        newChromosome = mutation(newChromosome,0.01)
        
        newGeneration.append(ArtificialPlayer('../img/mario.png',(display_width * 0),(display_height * 0.8),shape,newChromosome))
        
    return newGeneration

def evolution(nbGenerations,nbPlayersPerGeneration,shape):  
    allScores = []
    
    # res = [[chromosome,fitnessFunction],...]
    res = []
    generationScores = []
    for p in range(nbPlayersPerGeneration):
        print 'GENERATION 0 | PLAYER ' + str(p)
        ap = ArtificialPlayer('../img/mario.png',(display_width * 0),(display_height * 0.8),shape)
        game = Game(display_width,display_height,ap)
        score = game.run()
        print 'Score = ' + str(score)
        generationScores.append(score)
        res.append([ap.getChromosome(),score])
        
    print '======================================'
    allScores.append(generationScores)
    generation = getNewGeneration(nbPlayersPerGeneration,res,shape)
    res = []
    generationScores = []
    
    for g in range(1,nbGenerations):
        print '======================================'
        for p in range(nbPlayersPerGeneration):
            print 'GENERATION ' + str(g) + ' | PLAYER ' + str(p)
            ap = generation[p]
            game = Game(display_width,display_height,ap)
            score = game.run()
            res.append([ap.getChromosome(),score])
            print 'Score = ' + str(score)
            generationScores.append(score)
        
        print '======================================'
        allScores.append(generationScores)
        generation = getNewGeneration(nbPlayersPerGeneration,res,shape)
        res = []
        generationScores = []
        
    return allScores
    
def getAvgScores(allScores):
    res = []
    for i in range(len(allScores)):
        total = 0
        for j in range(len(allScores[i])):
            total += allScores[i][j]
            
        res.append(float(total)/len(allScores[i]))
        
    return res
    
allScores = evolution(100,5,[2,2,3])
avgScores = getAvgScores(allScores)

print avgScores