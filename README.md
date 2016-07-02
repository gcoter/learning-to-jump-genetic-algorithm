# learning-to-jump-genetic-algorithm
A small man learns how to jump over an obstacle thanks to a simple genetic algorithm.

# Requirements
* Python 2.7
* pygame
* numpy
* matplotlib

## Description
### Genetic Algorithm
The first generation is composed of artificial players whose *brain*'s parameters are randomly initialized. Then the following steps are executed :

1. **For each player, run a game and calculate its score** (players that go further and are faster get higher score)
2. **Create a new generation** : each player selects a partner (players with higher score have more chance to be selected). Their genes (= their brain's parameters) are combined by crossover and mutations can occur.
3. **Repeat**

### Making decisions
A player has two **sensors** : one on its left and one on its right. A sensor returns 1 if the obstacle or the left screen border is close enough, otherwise it returns 0.
Those sensors create a vector which is given as input to a simple neural network.
A brain returns *decisions* which is a vector with 3 components : 

1. Going left
2. Going right
3. Jump

During a game, if one component is greater than 0.5, the associated action is executed.

## Run
Simply run the Main.py file. You can change parameters directly in Main.py.

## Known Issues
I noticed that some issues appear randomly when trying to display the simulation. Most of the time, restarting a new console solves the problems.
However, if you still have problems, you can turn off the display by setting the boolean *displayOn* to **False** in Main.py.
