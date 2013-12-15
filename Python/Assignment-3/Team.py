'''
Created on 1 Dec 2012

@author: Ollie
'''

class team():
    
    def __init__(self):
        self._Wins = 0
        self._Draws = 0
        self._Losses = 0
        self._Played = 0
        self._Total = 0
        
    def getWins(self):
        return self._Wins
    
    def getDraws(self):
        return self._Draws
    
    def getLosses(self):
        return self._Losses
    
    def getPlayed(self):
        return self._Played
        
    def getTotal(self):
        return self._Total
    
    def updateWins(self, wins):
        self._Wins = wins
        #updates after loading from the file
    
    def updateDraws(self, draws):
        self._Draws = draws
        #updates after loading from the file
    
    def updateLosses(self, losses):
        self._Losses = losses
        #updates after loading from the file
    
    def updatePlayed(self, played):
        self._Played = played
        #updates after loading from the file
    
    def updateTotal(self, total):
        self._Total = total
        #updates after loading from the file
        
    def Win(self):
        self._Wins += 1
        self._Played += 1
        self._Total += 2
    
    def Draw(self):
        self._Draws += 1
        self._Played += 1
        self._Total += 1
    
    def Loss(self):
        self._Losses += 1
        self._Played += 1
