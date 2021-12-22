import random

from bke import MLAgent, is_winner, opponent, train, load, start, save, validate, RandomAgent, plot_validation, train_and_plot
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
   
print("1: train de computer \n 2: speel tegen een getrainde computer \n 3: je kan tegen ander persoon \n 4: train een AI en kijk hoe goed die het doet \n Kies wat je wilt spelen:")
choice = input()

if choice == '1':
    my_agent = MyAgent() #grafiekje weghalen
if choice == '2':
    my_agent = MyAgent()
if choice == '3':
    start()
if choice == '4':
  random_agent = RandomAgent() #weghalen dat je kan spelen
   
random.seed(1)
my_agent = MyAgent()
   
random_agent = RandomAgent()

my_agent = MyAgent(alpha=0.2, epsilon=0.6)

train(my_agent, 3000)
save(my_agent, 'MyAgent_3000')

train_and_plot(
agent=my_agent,
validation_agent=random_agent,
iterations=50,
trainings=100,
validations=1000)

if choice == '2':
    my_agent = load('MyAgent_3000')
    my_agent.learning = False
 

 
start(player_x=my_agent)

validation_agent = RandomAgent()

validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
 
plot_validation(validation_result)
 


# k
