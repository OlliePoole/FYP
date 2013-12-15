'''
Created on 1 Dec 2012

@author: Ollie
'''
from Team import team

class league:
    
    def __init__(self, teamNames, teamClassNames):
        self._TeamTable = []
        self._StatTable = []
        self._noOfTeams = len(teamNames)
        self._teamClassNames = teamClassNames
        for x in range(self._noOfTeams):
            teamClassNames[x] = team() #Initalising each team with it's own team() class
            self._TeamTable.append(teamNames[x]) 
            #Appends the information to the list
        self.updateLists()
            
    def removeTeam(self, teamName):
        try:
            pos = self._TeamTable.index(teamName)
            #finds the position of the team to be removed
            self._TeamTable.remove(teamName)
            #removes the team
            self._noOfTeams -= 1
            #takes 1 from the number of teams
            del self._StatTable[pos]
            #deletes the stats on the team
            del self._teamClassNames[pos]
            #deletes the class name assosiated with the team
            return True
        except:
            return False
    
    def teamPosition(self, teamName):
        try:
            pos = self._TeamTable.index(teamName) +1
            #finds the position of the team
        except ValueError:
            pos = -1
        return pos
            
    def updateTeams(self, team1, score1, team2, score2):
        pos1 = self.teamPosition(team1)-1
        pos2 = self.teamPosition(team2)-1
        #finds the positions of the two teams
    
        if score1 > score2:
            self._teamClassNames[pos1].Win()
            self._teamClassNames[pos2].Loss()
        elif score1 < score2:
            self._teamClassNames[pos1].Loss()
            self._teamClassNames[pos2].Win()
        else:
            self._teamClassNames[pos1].Draw()
            self._teamClassNames[pos2].Draw()
        self.updateLists()
            
    def displayList(self):
        return self._TeamTable
    
    def displayStat(self):
        return self._StatTable
    
    def updateLists(self):
        self._StatTable = []
        try:
            for x in range(self._noOfTeams):
                teamStat = self._teamClassNames[x].getWins(), self._teamClassNames[x].getDraws(), self._teamClassNames[x].getLosses(), self._teamClassNames[x].getPlayed(), self._teamClassNames[x].getTotal()
                self._StatTable.append(teamStat)
                #gets the stats about each team from their team class, then appends that to a list
            return True
        except:
            return False 
    
    def updateTeam(self):
        wins = 0
        draws = 0
        losses = 0
        played = 0
        total = 0
        for z in range(self._noOfTeams):
            temp = str(self._StatTable[z])
            #temp = (0,0,0,0,0) or equiverlent
            for x in range(len(temp)):
                if temp[x] == ",":
                    #finds the ',' which indicates where the number are and accomidates for 2 digit numbers
                    if x-1==1:
                        wins = int(temp[1])
                    else:
                        wins = int(temp[1:x-1])
                    temp = temp[x+1:len(temp)]
                    #takes the number off the string so the next number can be accessed
                    self._teamClassNames[z].updateWins(wins)
                    #updates the win attribute for the team class
                    break
                
            for x in range(len(temp)):
                if temp[x] == ",":
                    if x-1==1:
                        draws = int(temp[1])
                    else:
                        draws = int(temp[1:x-1])
                    temp = temp[x+1:len(temp)]
                    self._teamClassNames[z].updateDraws(draws)
                    #updates the draws attribute for the team class
                    break
                
            for x in range(len(temp)):
                if temp[x] == ",":
                    if x-1==1:
                        losses = int(temp[1])
                    else:
                        losses = int(temp[1:x-1])
                    temp = temp[x+1:len(temp)]
                    self._teamClassNames[z].updateLosses(losses)
                    #updates the losses attribute for the team class
                    break
                
            for x in range(len(temp)):
                if temp[x] == ",":
                    if x-1==1:
                        played = int(temp[1])
                    else:
                        played = int(temp[1:x-1])
                    temp = temp[x+1:len(temp)]
                    self._teamClassNames[z].updatePlayed(played)
                    #updates the played attribute for the team class
                    break
            
            total = int(temp[1])
            self._teamClassNames[z].updateTotal(total)
            #updates the total attribute for the team class
        
    def loadFile(self):
        self._TeamTable = []
        self._StatTable = []
        with open("tableFile.txt") as f:
            line = f.readline()
        f.close()
        
        for x in range(len(line)):
            if line[x] == "]":
                #locates the ] character to split the string
                break
        teams = line[1:x]
        stats = line[x+1:len(line)]
        
        self._noOfTeams = 1
        for x in range(len(teams)):
            if teams[x] == ",":
                self._noOfTeams += 1
                #works out how many teams there are on the file
        
        for y in range(self._noOfTeams):
            for x in range(len(teams)):
                if teams[x] == ",":
                    self._TeamTable.append(teams[1:x-1])
                    teams = teams[x+2:len(teams)]
                    #searches for the ',' and appends the item to the list
                    break
                
            for z in range(len(stats)):
                if stats[z] == ")":
                    self._StatTable.append(stats[1:z])
                    stats = stats[z+2:len(stats)]
                    #searches for the ')' and appends the stats to a seperate list
                    break
                
        self._TeamTable.append(teams[1:len(teams)-1])
        self._StatTable.append(stats[1:len(stats)])
        
        self.updateTeam()
        
    def saveFile(self):
        try:
            with open("tableFile.txt", 'w') as f:
                f.write(str(self._TeamTable))
                f.write(str(self._StatTable))
            f.close()
            return True
        except:
            return False
        
    def updateTable(self):
        pointList= []
        for z in range(self._noOfTeams):
            pointList.append(self._teamClassNames[z].getTotal())
            #new list just for the teams total points
        upperBound = self._noOfTeams-1
        lowerBound = 0
        
        while lowerBound != self._noOfTeams-1:
            if pointList[lowerBound] < pointList[upperBound]:
                #checks if one total is bigger then the other and swaps them
                a, b = lowerBound, upperBound
                pointList[b], pointList[a] = pointList[a], pointList[b]
                self._TeamTable[b], self._TeamTable[a] = self._TeamTable[a], self._TeamTable[b]
                self._StatTable[b], self._StatTable[a] = self._StatTable[a], self._StatTable[b]
                self._teamClassNames[b], self._teamClassNames[a] = self._teamClassNames[a], self._teamClassNames[b]
                
                upperBound -= 1
            else:
                upperBound -= 1
            
            if upperBound == lowerBound:
                lowerBound += 1
                upperBound = self._noOfTeams-1
            
        





