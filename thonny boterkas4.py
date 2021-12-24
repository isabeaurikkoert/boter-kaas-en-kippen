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
    
 
my_agent = MyAgent(alpha=0.02, epsilon=0.3)
 

 
   
print(" 1: train de computer \n 2: speel tegen een getrainde computer \n 3: je kan tegen ander persoon \n 4: train een AI en kijk hoe goed die het doet \n 5: Wat zijn hyperparameters? \n Kies wat je wilt spelen:")
choice = input()

if choice == '1':
    train(my_agent, 3000)
    save(my_agent, 'MyAgent_3000')
    
if choice == '2':
    train(my_agent, 3000)
    save(my_agent, 'MyAgent_3000')
    my_agent = load('MyAgent_3000')
    my_agent.learning = False
    start(player_x=my_agent)
    
if choice == '3':
    start()
    
    
if choice == '4':
    train(my_agent, 10000)
    save(my_agent, 'MyAgent_noBeat')
    my_agent = load('MyAgent_noBeat')
    my_agent.learning = False
     
    validation_agent = RandomAgent()
     
    validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=10000)
     
    plot_validation(validation_result)
    
if choice == '5':
    print("Hyperparameters zijn grenzen die je kan aanpassen. In deze code heb je 2 hyperparameters, alpha en epsilon. De alpha is de leerfactor van de computer. Deze bepaalt hoe snel de computer nieuwe kennis adopteert. Hoe hoger dit getal, hoe sneller de computer geneigd zal zijn om oude kennis te vervangen door nieuwe kennis. De epsilon  is de verkenningsfactor van de computer. Deze bepaalt hoe vaak de computer nieuwe dingen probeert. Hoe hoger dit getal, hoe vaker de computer een willekeurige actie probeert in plaats van de best bekende zet. Door te spelen met deze twee parameters kan je dus een beetje controleren hoe 'slim' de computer is.")
    
