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
    
    def player(self, straws):
        remove = int(input("How many straws do you want to remove: "))
        while remove < 1 or remove > 3:
            print("Number must be between 1 and 3, please try again")
            remove = int(input("How many straws do you want to remove: "))
        while straws - remove < 0:
            print("Error, insufficient straws")
            remove = int(input("How many straws do you want to remove: "))
        return remove
    #Responsible for the player, validating for numbers outside 1 and 3 and avoiding negative numbers

    def whosTurn(self, whosGo):
        if whosGo % 2 == 1:
            return "Computers"
        else : return "Players"
    #Works out who's go it is by working out if the number is even or odd
        
G = NimGame()

repeat = "Y"
while repeat == "Y":    
    print("Welcome to this game of NIM")
    straws = G.randomStraws() #Gets value from function
    whosGo = 1
    print('The initial number of straws is: ', straws)

    while straws > 0: #loop while the number of straws is greater than 0
        print("It is the", G.whosTurn(whosGo), "turn")
        if G.whosTurn(whosGo) == "Computers":
            straws -= G.computer(straws)
            print("The amount of straws remaining is now: ", straws)
            print("")
            whosGo += 1
        else:
            straws -= G.player(straws)
            print("The amount of straws remaining is now: ", straws)
            print("")
            whosGo += 1
        
    if G.whosTurn(whosGo) == "Computers": #Works out the last person to play and displays the winner
        print("The computer has won!")
    else:
        print("The player has one!")
        
    repeat = raw_input("Do you want to play again: (Y or N)") #Asking the user if they want to play again
    while repeat != "Y" and repeat != "N":
        print("Please enter either 'Y' or 'N'")
        repeat = raw_input("Do you want to play again: (Y or N)")
exit()
