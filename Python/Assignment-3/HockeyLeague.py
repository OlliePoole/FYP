'''
Created on 4 Dec 2012

@author: Ollie
'''

from League import league

def DisplayMenu():
    print("""Menu:
            Press 1 to remove a team
            Press 2 to find a team position
            Press 3 to input a score
            Press 4 to display the league
            Press 5 to load the table
            Press 6 to save the table
            Press 0 to exit""")

def getMenuChoice():
    choice = int(input("Enter your choice: "))
    while choice <0 or choice > 6:
        print("Invalid input, please try again")
        choice = int(input("Enter your choice: "))
    return choice

def firstUse():
    print("Welcome to the hockey league program.")
    print("As this is the first use, you need to enter the names of the teams in the league")
    print("When you are finished enter '-1' and the loop will end")
    teamNames = []
    temp = ""
    while temp != "-1":
        temp = raw_input("Enter the team names here: ")
        teamNames.append(temp)
        #appends the team names to a list
    teamNames.remove("-1")
    #removes the -1 entry when the user has finished entering
    return teamNames

def LoadNames():
    teamNames = []
    with open("tableFile.txt") as f:
        line = f.readline()
    f.close()
    for x in range(len(line)):
        if line[x] == "]":
            break
    teams = line[1:x]
    #splits the line up so only the teams are loaded
     
    noOfTeams = 1
    for x in range(len(teams)):
        if teams[x] == ",":
            noOfTeams += 1
            #works out how many teams are in the file
        
    for y in range(noOfTeams):
        for x in range(len(teams)):
            if teams[x] == ",":
                teamNames.append(teams[1:x-1])
                teams = teams[x+2:len(teams)]
                break
            #splits the string down into its individual teams
                
    teamNames.append(teams[1:len(teams)-1])
    return teamNames
    
try:
    tableFile = open("tableFile.txt") #try to open textfile
    print("A table has been previously saved, do you want to load it? ")
    print("Note: This will load the names only, please select the load option to load their stats as well")
    load = raw_input("Enter Y or N :")
    while load != "N" and load != "Y":
        print("Invalid input")
        load = raw_input("Please try again: ")
        
    if load == "N":
        teamNames = firstUse()
        #calls first use to ask the user to enter the names
        teamClassNames = []
        for x in range(len(teamNames)):
            temp = str(teamNames[x])+"C"
            teamClassNames.append(temp)
            #adds "C" to the team names and appends them to another list
    else:
        teamNames = LoadNames()
        #calls load names to load the names from the file
        teamClassNames = []
        for x in range(len(teamNames)):
            temp = str(teamNames[x])+"C"
            teamClassNames.append(temp)
            #adds "C" to the team names and appends them to another list
except:
    #if file is not found
    teamNames = firstUse()
    teamClassNames = []
    for x in range(len(teamNames)):
        temp = str(teamNames[x])+"C"
        teamClassNames.append(temp)

LeagueTable = league(teamNames, teamClassNames)

DisplayMenu()
choice = getMenuChoice()

while choice != 0:
    
    if choice == 1:
        teamName = raw_input("Enter the name of the team you want to remove: ")
        if LeagueTable.removeTeam(teamName) == True:
            print("Team has been removed")
        else:
            print("Error, team not found. Please try again")
        DisplayMenu()
        choice = getMenuChoice()
    
    elif choice == 2:
        teamName = raw_input("Enter the team name you want to find: ")
        pos = LeagueTable.teamPosition(teamName)
        if pos == -1:
            print("Error, team not found. Please try again")
        else:
            print(teamName, " is at position: ", pos)
        DisplayMenu()
        choice = getMenuChoice()
        
    elif choice == 3:
        team1 = raw_input("Enter the name of the first team: ")
        score1 = int(input("Enter the score for that team: "))
        team2 = raw_input("Enter the name of the second team: ")
        score2 = int(input("Enter the score for that team: "))
        LeagueTable.updateTeams(team1, score1, team2, score2)
        print("Score saved")

        DisplayMenu()
        choice = getMenuChoice()
        
    elif choice == 4:
        LeagueTable.updateTable()
        table = LeagueTable.displayList()
        stat = LeagueTable.displayStat()
        print("Team:  Stats(W,D,L,P,T):")
        for x in range(len(table)):
            print(table[x], " ", stat[x])
        DisplayMenu()
        choice = getMenuChoice()

    elif choice == 5:
        print("Load successful")
        DisplayMenu()
        choice = getMenuChoice()

    elif choice == 6:
        if LeagueTable.saveFile() == True:
            print("Save successful")
        else:
            print("Error, please try again")
        DisplayMenu()
        choice = getMenuChoice()
        
