'''
Created on 10 Dec 2012

@author: Ollie, Ryan, Jack, James
'''
from easygui import *

def RegisterModule():
    studentId = enterbox(
        msg = 'Enter the student ID',
        title = 'Student ID',
        default ='',
        strip = True,
        image = None,
        root = None)
    foundstudents = []
    counter = 0

    if studentId == None:
        msgbox("Function will exit", "Error", "OK", None, None)
    else:
        try:
            assStuID.index(studentId)
        except:
            msgbox("User not found", "Error", "OK", None, None)
            RegisterModule()

        for i in assStuID:
            if i == studentId:
                foundstudents.append(counter)
            counter +=1
            
        modchoices = []
        for x in range(len(foundstudents)):
            modchoices.append(assModule[foundstudents[x]])
            
        moduleList = ["U8001","U8002","U8003","U8004","U8005","U8006","U8007","U8008"]
        for eachItem in modchoices:
            for x in range(len(moduleList)):
                if eachItem == moduleList[x]:
                    moduleList[x] = ""

        if len(modchoices) == 4:
            msgbox("You can only take four modules", "Error", "Ok", None, None)
            
        else:
            n = choicebox(msg = "Which module would you like to take?", title = "Adding a module", choices = moduleList)

            assModule.append(n)
            assStuID.append(studentId)
            assM1.append("99/99")
            assM2.append("99/99")
            assCourse.append("False")

            myFile = open("assesment.txt", "w")
            counter = 0
            for y in assModule:
                counter += 1
            for x in range(0,counter):
                print(assModule[x], file=myFile)
                print(assStuID[x], file=myFile)
                print(assM1[x], file=myFile)
                print(assM2[x], file=myFile)
                print(assCourse[x], file=myFile)
            myFile.close()

            
            pos = modID.index(n)
            modNumbers[pos] = str(int(modNumbers[pos]) +1)

            #Save
            myFile = open("Modules.txt", "r+")
            counter = 0
            for y in modName:
                counter += 1
            for x in range(0,counter):
                print(modName[x], file=myFile)
                print(modID[x], file=myFile)
                print(modDescription[x], file=myFile)
                print(modNumbers[x], file=myFile)
                print(modLead[x], file=myFile)
            myFile.close()

            
                
            pos = stuID.index(studentId)
            stuModules[pos] += (", "+n)
            

            #Save
            myFile = open("Student.txt", "w+")
            counter = 0
            for y in stuName:
                counter += 1
            for x in range(0,counter):
                print(stuName[x], file=myFile)
                print(stuID[x], file=myFile)
                print(stuDOB[x], file=myFile)
                print(stuGender[x], file=myFile)
                print(stuAddress[x], file=myFile)
                print(stuContact[x], file=myFile)
                print(stuCourse[x], file=myFile)
                print(stuModules[x], file=myFile)
            myFile.close()

            msgbox("Module Registered", "Information", "OK", None, None)

def SubmitCoursework():
    studentId = enterbox(
        msg = 'Enter your student ID',
        title = 'Student ID',
        default ='',
        strip = True,
        image = None,
        root = None)
    foundstudents = []
    counter = 0 
    for i in assStuID:
        if i == studentId:
            foundstudents.append(counter)
        counter +=1
    modchoices = []
    for x in range (len(foundstudents)):
        modchoices.append(assModule[foundstudents[x]])
    n = choicebox(
        msg = 'which module would you like to submit coursework for?',
        title = 'submitting work',
        choices = modchoices)

    temp = modchoices.index(n)


    assCourse [foundstudents[temp]] = 'True'

    counter = 0
    myFile = open("assesment.txt","w+")
    for y in assModule:
        counter += 1
    for x in range(0,counter):    
        print(assModule[x], file=myFile)
        print(assStuID[x], file=myFile)
        print(assM1[x], file=myFile)
        print(assM2[x], file=myFile)
        print(assCourse[x], file=myFile)
    myFile.close()

    msgbox("Coursework submitted", "Infomation", "OK", None, None)

def displayAssessment():

    search=enterbox("Enter module ID", "search","", None, None) #Allows user input, None relates to GUI

    while len(str(search)) != 5:
        msgbox("The module needs to be 5 digits long", "Error", "Ok", None, None)
        search=enterbox("Enter module ID", "search","", None, None)
    #Validates user input

    try:
        moduleList = []
        counter = 0
        for i in assModule:
            if i == search:
                moduleList.append(counter)
            counter += 1
                
        msgbox(("Module Name:",assModule[pos], "\n", "Student ID:",assStuID[pos], "\n", "Module 1:",assM1[pos], "\n", "Module 2:",assM2[pos]), "View Assessments", "OK", None, None) #Prints students assessment information
    except:
        msgbox("Module not found", "Error", "Ok", None, None)
    #Validates user input
        
def enterModule():
    search = enterbox("Enter the module ID", "search","", None, None) #Allows user input
    if search == None:
        #Load previous page <----- MAKE CANCEL WORK
        print()
    while len(str(search)) != 5:
        msgbox("The module ID needs to be 5 digits long", "Error", "Ok", None, None)
    #Validates user input
        search = enterbox("Emter the module ID", "search","", None, None) #Restarts the programme
    return search

def displayModule():
    search = enterModule() #Assign variable name to function for indexing
    try:
        pos = modID.index(search) #Search for inputted ID in the text file
        msgbox(("Module Name:",modName[pos], "\n", "Module ID:",modID[pos],
                "\n", "Module Description:",modDescription[pos], "\n", "Module Numbers:",modNumbers[pos],
                "\n", "Module Leader:", modLead[pos]), "View Assessments", "OK", None, None)
        #Prints entered module information
    except:
        msgbox("Module not found", "Error", "Ok", None, None) #Validates user input
    

def EvaluateModule():
    mod = choicebox(
    msg = 'which module would you like to leave feedback for: ',
    title = 'Leaving feedback',
    choices = modName)
    
    feedback = enterbox("Enter your feedback here", "Feedback", "", None, None)
    
    myFile = open("Feedback.txt", "a")
    print(feedback, file=myFile)
    print(mod, file=myFile)
    print("False", file=myFile)


choice = ""
while choice != None:
    
    myFile = open("assesment.txt")
    
    assModule = []
    assStuID = []
    assM1 = []
    assM2 = []
    assCourse = []
    #Turns variables into lists

    counter = 0
    for x in myFile:
        counter += 1
    myFile.seek(0)

    for y in range(counter//5):
        assModule.append(myFile.readline().strip())
        assStuID.append(myFile.readline().strip())
        assM1.append(myFile.readline().strip())
        assM2.append(myFile.readline().strip())
        assCourse.append(myFile.readline().strip())

    myFile.close()

    myFile = open("Modules.txt")

    modName = []
    modID = []
    modDescription = []
    modNumbers = []
    modLead = []

    counter = 0
    for x in myFile:
        counter += 1
    myFile.seek(0)

    for y in range(counter//4):
        modName.append(myFile.readline().strip())
        modID.append(myFile.readline().strip())
        modDescription.append(myFile.readline().strip())
        modNumbers.append(myFile.readline().strip())
        modLead.append(myFile.readline().strip())
                
    myFile.close()
    
    myFile = open("student.txt")

    stuName = []
    stuID = []
    stuDOB = []
    stuGender = []
    stuAddress = []
    stuContact = []
    stuCourse = []
    stuModules = []

    counter = 0
    for x in myFile:
        counter += 1
    myFile.seek(0)

    for y in range((counter//8)):
        stuName.append(myFile.readline().strip())
        stuID.append(myFile.readline().strip())
        stuDOB.append(myFile.readline().strip())
        stuGender.append(myFile.readline().strip())
        stuAddress.append(myFile.readline().strip())
        stuContact.append(myFile.readline().strip())
        stuCourse.append(myFile.readline().strip())
        stuMod = myFile.readline().strip()
        stuModules.append(stuMod.strip(","))
    myFile.close()
    
    
    
    
    msg     = "Choose which function you would like?"
    title   = "PIP - Student"
    choices = ["Register on a module", "Hand in coursework", "View modules", "View assessments for a module", "Evaluate a module"]
    choice   = choicebox(msg, title, choices)
    
    if choice == "Register on a module":
        RegisterModule()
    elif choice == "Hand in coursework":
        SubmitCoursework()
    elif choice == "View assessments for a module":
        displayAssessment()
    elif choice == "View modules":
        displayModule()
    elif choice == "Evaluate a module":
        EvaluateModule()
        

