import random
 
from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot, start, load
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
print("Kies wat je wilt doen \n 1 train de computer \n 2 speel tegen de computer \n 3 speel tegen een vriend \n 4 plot een validatie grafiek")
    choice = input
random.seed(1)
 
my_agent = MyAgent()
random_agent = RandomAgent()
 
train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=60,
    trainings=100,
    validations=1000)
my_agent = MyAgent(alpha=0.2, epsilon=0.6)

my_agent = MyAgent()
my_agent = load('MyAgent_3000')
 
my_agent.learning = False
 
start(player_x=my_agent)

#Je programma kan een Agent trainen
#Je kan tegen een Agent spelen
#Je kan tegen een ander persoon spelen
#Je programma kan een validatie grafiek plotten
