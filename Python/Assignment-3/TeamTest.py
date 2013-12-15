'''
Created on 1 Dec 2012

@author: Ollie
'''
from Team import team

Test = team()

#Displaying the initial values
print("Wins: ", Test.getWins())
print("Draws: ", Test.getDraws())
print("Losses: ", Test.getLosses())
print("Games Played: ", Test.getPlayed())
print("Total: ", Test.getTotal())

#Inputting the test data
Test.Win()
Test.Draw()
Test.Loss()

#Printing the values again
print("Wins: ", Test.getWins())
print("Draws: ", Test.getDraws())
print("Losses: ", Test.getLosses())
print("Games Played: ", Test.getPlayed())
print("Total: ", Test.getTotal())
