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

if choice == '1':
    start ()
if choice == '2':
if choice == '3':
if choice == '4':

k