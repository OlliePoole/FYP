'''
Created on 14 Nov 2012

@author: Ollie
'''
  
import random

class NimGame():
    
    def __init__(self):
        print("")
        
    def randomStraws(self):
        straws = random.randint(10,20)
        if straws%4 == 1:
            straws += 1
        return straws
    #This generates a random number and checks if it one more than a multiple of four

    def computer(self, straws):
        remove = random.randint(1,3)
        while straws - remove < 0:
            remove = random.randint(1,3)
        return remove
    #This is responsible for the computer, it will generate a random number and perform a check
    #to avoid getting any negative numbers
    
    def computer2(self, straws):
        if straws%4 == 1:
            remove = 1
            return remove
        elif straws%4 == 2:
            remove = 1
            return remove
        elif straws%4 == 3:
            remove = 2
            return remove
        elif straws%4 == 0:
            remove = 3
            return remove
    #The second computer built on the specification given in the instructions

    def whosTurn(self, whosGo):
        if whosGo % 2 == 1:
            return "Computer1s"
        else : return "Computer2s"

winTracker = []
G = NimGame()
comp1Wins = 0
comp2Wins = 0
#Keeping track of how many each computer has won

for x in range(10):  
    print("Welcome to this game of NIM")
    straws = G.randomStraws()
    whosGo = 1
    print('The initial number of straws is: ', straws)

    while straws > 0:
        print("It is the", G.whosTurn(whosGo), "turn")
        if G.whosTurn(whosGo) == "Computer1s":
            straws -= G.computer(straws)
            print("The amount of straws remaining is now: ", straws)
            print("")
            whosGo += 1
        else:
            straws -= G.computer2(straws)
            print("The amount of straws remaining is now: ", straws)
            print("")
            whosGo += 1
        
    if G.whosTurn(whosGo) == "Computer1s":
        print("Computer1 has won!")
        winTracker.append("Computer1")
        comp1Wins += 1
        #Appends the result and adds one to the win counter for that computer
    else:
        print("Computer2 has one!")
        winTracker.append("Computer2")
        comp2Wins += 1
        #Appends the result and adds one to the win counter for that computer

print("After 10 games the results are:")
print(winTracker)
print("Computer 1 won: ", comp1Wins)
print("Computer 2 won: ", comp2Wins)
    
