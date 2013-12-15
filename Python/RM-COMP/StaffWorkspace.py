'''
Created on 10 Dec 2012

@author: Ollie, Ryan, Jack, James
'''
from easygui import *


def AddStudent():
    #Enter student details

    msg = "Enter your personal information"
    title = "Enter student information"
    fieldNames = ["Student name","Student Number","Dob. 00/00/0000","Gender. m/f","Address","Course","Modules","Contact number"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg,title, fieldNames)

    studentDetails=fieldValues

    if studentDetails == None:
        msgbox("You closed the box", "", "OK", None, None)
        
  
    while len(studentDetails[7]) != 11:
        msgbox("Contact number must be 11 digits", 'Contact number error',
                   "OK", None, None)
        fieldValues = multenterbox(msg,title, fieldNames, fieldValues)
        studentDetails=fieldValues

    while len(studentDetails[2]) != 10:
        msgbox("Date of birth invalid", 'Date of birth error', "OK", None, None)
    
        fieldValues = multenterbox(msg,title, fieldNames, fieldValues)
        studentDetails=fieldValues

    while (studentDetails[3]) != "m" and (studentDetails[2]) != "f":
        msgbox("Gender invalid", 'Gender error', "Continue", None, None)

        fieldValues = multenterbox(msg,title, fieldNames, fieldValues)
        studentDetails=fieldValues
    
    studentName=(fieldValues[0]).strip()
    studentNumber=(fieldValues[1]).strip()
    studentDob=(fieldValues[2]).strip()
    studentGender=(fieldValues[3]).strip()
    studentAddress=(fieldValues[4]).strip()
    studentCourse=(fieldValues[5]).strip()
    studentModules=(fieldValues[6]).strip()
    studentContactNumber=(fieldValues[7]).strip()


    studentList=open("Student.txt","a")
    print(studentName, file=studentList)
    print(studentNumber, file=studentList)
    print(studentDob, file=studentList)
    print(studentGender, file=studentList)
    print(studentAddress, file=studentList)
    print(studentContactNumber, file=studentList)
    print(studentCourse, file=studentList)
    print(studentModules, file=studentList)

    studentList.close()
    msgbox("The student inforamtion has been stored","Successful save","Finish", None, None)

def AddAppointment():
    msg = "Make an appointment"
    title = "Enter appointment details"
    fieldNames = ["Staff id\n(8 digits)", "Id of who the appointment is with","Date of appointment. 00/00/0000",
            "Appointment slot (1-9) "]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg,title, fieldNames, fieldValues)

    appointmentDetails=fieldValues

    while len(appointmentDetails[0]) != 8:
            cheese=len(appointmentDetails[0])
            msgbox("Staff id must be 8 digits long, you entered  characters", 'Staff id error.',
               "continue", None, None)

            fieldValues = multenterbox(msg,title, fieldNames, fieldValues)    
            appointmentDetails=fieldValues

    while len(appointmentDetails[1]) != 8:
            cheese=len(appointmentDetails[0])
            msgbox("id must be 8 digits long.", 'id error.',
               "continue", None, None)

            fieldValues = multenterbox(msg,title, fieldNames, fieldValues)    
            appointmentDetails=fieldValues

    while len(appointmentDetails[2]) != 10:
            msgbox("Appointment date is not valid, check format", 'Date error.', "Continue", None, None)

            fieldValues = multenterbox(msg,title, fieldNames, fieldValues)    
            appointmentDetails=fieldValues
    try:
        while (int(appointmentDetails[3])) <1 or (int(appointmentDetails[3])) >9:

                msgbox("Slot chosen must be betwen 1 and 9", 'Slot error.', "Continue", None, None)
                fieldValues = multenterbox(msg,title, fieldNames, fieldValues)    
                appointmentDetails=fieldValues
    except:
        msgbox("Please enter number only", "Error", "OK", None, None)
        AddAppointment()

    appStaffID = appointmentDetails[0].strip()
    appStudentID = appointmentDetails[1].strip()
    appDate = appointmentDetails[2].strip()
    appSlot = str(appointmentDetails[3].strip())
    
    myFile = open("appointmentFile.txt", "a")
    print(appStaffID, file=myFile)
    print(appStudentID, file=myFile)
    print(appDate, file=myFile)
    print(appSlot, file=myFile)

def appointmentSearch():
    search=enterbox("View appointments by date","Search","",None, None)
    return search

def displayAppointments():
    search=appointmentSearch()
    #A loop search needs to  find every instance of an appointment
    foundAppointments=[]
    counter=0
    for i in appDate:
        if i == search:
            foundAppointments.append(counter)
        counter += 1
    for x in range(len(foundAppointments)):
        msgbox(("\n","Staff id:",appStaff[foundAppointments[x]],"\n","Student Id:", appStuId[foundAppointments[x]],"\n","Appointment date:" ,
                appDate[foundAppointments[x]],"\n","Appointment slot:", appSlot[foundAppointments[x]]),"appointments","Continue to next appointment",None,None)

def AddAssesmentMarks():
    studentId = enterbox(
        msg = 'Enter the student ID',
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
        msg = 'which module would you like to add a grade for',
        title = 'Adding mark for student',
        choices = modchoices)

    temp = modchoices.index(n)

    msg = "Please enter their grades (00/00)"
    title = "Adding grades"
    fieldName1 = ["grade1"]
    fieldName2 = ["grade2"]
    Values = [] # we start with blanks for the values
    gradeList1 = multenterbox(msg,title, fieldName1)
    gradeList2 = multenterbox(msg,title, fieldName2)
    assM1[foundstudents[temp]]=gradeList1[0]
    assM2[foundstudents[temp]]=gradeList2[0]

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

    msgbox("Marks Saved", "Info", "OK", None, None)
def ViewUnsubmitted():
    moduleID = enterbox(
        msg = 'Enter module name',
        title = 'Module',
        default ='',
        strip = True,
        image = None,
        root = None)

    foundmodule = []
    counter = 0 
    for i in assModule:
        if i == moduleID:
            foundmodule.append(counter)
        counter +=1
    modchoices = []
    for x in range (len(foundmodule)):
        modchoices.append(assModule[foundmodule[x]])
    
    nowork = []
    for x in range(0,len(foundmodule)):
        temp = foundmodule[x]
        if assCourse[temp] == 'False':
            nowork.append(assStuID[temp])
            
    outputStr = ""
    for x in range(len(nowork)):
        outputStr += (nowork[x] + "\n")
    
    textbox(msg="Here are the students that have not submitted work",
        title="Submitted work",
        text= outputStr,
        codebox=0)

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
    except:
        msgbox("Module not found", "Error", "Ok", None, None) #Validates user input
         
        
    msgbox(("Module Name:",modName[pos], "\n", "Module ID:",modID[pos],
                "\n", "Module Description:",modDescription[pos], "\n", "Module Numbers:",modNumbers[pos],
                "\n", "Module Leader:", modLead[pos]), "View Assessments", "OK", None, None)
        #Prints entered module information
    
        
def studentSearch():
    search=enterbox("Search for a student", "Search", "",  None, None)
    return search

def displayStudent():
    search=studentSearch()
    try:
        posistion=stuID.index(search)
    except:
        msgbox("User not found", "Error", "OK", None, None)
    #output into msg box
    msgbox(("\n","Student Name:",stuID[posistion],"\n","Date of Birth:",stuDOB[posistion],"\n","Gender:",stuGender[posistion],"\n","Address:",stuAddress[posistion],"\n","Contact Number:",stuContact[posistion],
            "\n","Course:",stuCourse[posistion],"\n","Modules:",stuModules[posistion]),"Student Profile", "Continue", None, None)

def ViewFeedback():
    
    t = choicebox(
        msg = 'You have feedback in these modules:',
        title = 'Feedback',
        choices = feedbackMod)

    relFeedback = [] #Relevent feedback based on the choice above
    counter = 0 
    for i in feedbackMod:
        if i == t:
            relFeedback.append(counter)
        counter +=1
    nonView = []
    View = []
    check = False
    for x in range(len(relFeedback)):
        temp = relFeedback[x]
        if feedbackView[temp]=="False":
            nonView.append(temp)
            check = True
        else:
            View.append(temp)
        
    if check ==False:
        msgbox("You have no new feedback since last check", "Feedback", "OK", None, None)
        Choices = ["Viewed Feedback"]
    else:
        Choices = ["New Feedback", "Viewed Feedback"]
    
    t = choicebox(
        msg = 'What would you like to view',
        title = 'Feedback',
        choices = Choices)

    if t == "New Feedback":
        for x in range(0,len(nonView)):
            temp = nonView[x]
            msgbox(("Feedback:", "\n", feedbackText[temp]), "View Feedback","Next Feedback", None, None)
            feedbackView[temp] == "True"
        
        msgbox("All feedback viewed", "Feedback", "OK", None, None)
        
        counter = 0
        myFile = open("Feedback.txt")
        for y in feedbackMod:
            counter += 1

        for x in range(0,counter):
            print(feedbackText[x], file=myFile)
            print(feedbackMod[x], file=myFile)
            print(feedbackView[x], file=myFile)
    
        myFile.close()

    else:
        for x in range(0,len(View)):
            temp = View[x]
            msgbox(("Feedback:", "\n", feedbackText[temp]), "View Feedback","Next Feedback", None, None)
        msgbox("All feedback viewed", "Feedback", "OK", None, None)
           
def strugglingStudents():
    
    
    search=enterbox("Enter module ID", "search","", None, None) #Allows user input, None relates to GUI
    if search == None:
        msgbox("Returning to the menu", "Info", "OK", None, None)
    else:
        
        while len(str(search)) != 5:
            msgbox("The module needs to be 5 digits long", "Error", "Ok", None, None)
            search=enterbox("Enter module ID", "search","", None, None)
            #Validates user input
        moduleFound = []
        counter = 0
        for i in assModule:
            if i == search:
                moduleFound.append(counter)
            counter += 1
    
        struggling = []
        for x in range(0,len(moduleFound)):
        
            num1 = int(assM1[moduleFound[x]][:2])
            total1 = int(assM2[moduleFound[x]][3:])

            num2 = int(assM2[moduleFound[x]][:2])
            total2 = int(assM2[moduleFound[x]][3:])

            num1per = (num1/total1)*100
            num2per = (num2/total2)*100

            if num1per < 40 or num2per < 40:
                struggling.append(assStuID[moduleFound[x]])

        outputStr = ""
        for x in range(0,len(struggling)):
            outputStr += (struggling[x] + "\n")
    
        textbox(msg="Here are the students who scored below 40% in their modules",
            title="Struggling Students",
            text= outputStr,
            codebox=None)
            
def AssessingTrends():
    search=enterbox("Enter module ID", "search","", None, None) #Allows user input, None relates to GUI
    if search == None:
        exit()

    while len(str(search)) != 5:
        msgbox("The module needs to be 5 digits long", "Error", "Ok", None, None)
        search=enterbox("Enter module ID", "search","", None, None)
    #Validates user input
    moduleFound = []
    counter = 0
    for i in assModule:
        if i == search:
            moduleFound.append(counter)
        counter += 1
    
    ass1percentAv = []
    ass2percentAv = []
    ass1markAv = []
    ass2markAv = []
    
    for x in range(0,len(moduleFound)):
        
        num1 = int(assM1[moduleFound[x]][:2])
        total1 = int(assM2[moduleFound[x]][3:])

        num2 = int(assM2[moduleFound[x]][:2])
        total2 = int(assM2[moduleFound[x]][3:])

        num1per = (num1/total1)*100
        num2per = (num2/total2)*100

        ass1percentAv.append(num1per)
        ass2percentAv.append(num2per)

        ass1markAv.append(num1)
        ass2markAv.append(num2)

    for y in range(1,len(ass1markAv)):
        ass1percentAv[0] += ass1percentAv[y]
        ass2percentAv[0] += ass2percentAv[y]

        ass1markAv[0] += ass1markAv[y]
        ass2markAv[0] += ass2markAv[y]
        
    ass1percentAv[0] /= len(ass1percentAv)
    ass2percentAv[0] /= len(ass2percentAv)
    ass1markAv[0] /= len(ass1markAv)
    ass1markAv[0] /= len(ass1markAv)
    

    outputStr = "Assesment 1 average percentage: " + str(ass1percentAv[0]) + "\n" + "Assessment 2 average percentage: " + str(ass2percentAv[0]) +"\n" + "Assessment 1 average mark: " + str(ass1markAv[0]) + "\n" + "Assessment 2 average mark: " + str(ass2markAv[0])
    
    textbox(msg="Here is the breakdown for the results for each module",
        title="Module breakdown",
        text= outputStr,
        codebox=0)

choice = ""
while choice != None:
    
    myFile = open("appointmentFile.txt")

    appStaff = []
    appStuId = []
    appDate = []
    appSlot = []
    counter = 0
    for x in myFile:
        counter += 1
    myFile.seek(0)

    for y in range(counter//4):
        appStaff.append(myFile.readline().strip())
        appStuId.append(myFile.readline().strip())
        appDate.append(myFile.readline().strip())
        appSlot.append(myFile.readline().strip())

    myFile.close()
    
    myFile = open("assesment.txt")

    assModule = []
    assStuID = []
    assM1 = []
    assM2 = []
    assCourse = []

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
    
    myFile = open("Modules.txt") #Opens the text file, and assigns a name 

    modName = []
    modID = []
    modDescription = []
    modNumbers = []
    modLead = []
    #Turns variables into lists

    counter = 0
    for x in myFile:
        counter += 1
    myFile.seek(0)

    for y in range((counter//4)):
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

    myFile = open("Feedback.txt")

    feedbackText = []
    feedbackMod = []
    feedbackView = []

    counter = 0
    for x in myFile:
        counter += 1

    myFile.seek(0)
    for y in range(counter//3):
        feedbackText.append(myFile.readline().strip())
        feedbackMod.append(myFile.readline().strip())
        feedbackView.append(myFile.readline().strip())
    myFile.close()

    
    msg     = "Which function would you like?"
    title   = "PIP - Staff Workspace"
    choices = ["Add appointment", "View Appointments", "Add Assessment Marks", "Display list of students who have not submitted coursework", "View Module", "View Student", "View struggling students", "View student feedback", "Add a student", "Assess trends"]
    choice   = choicebox(msg, title, choices)

    if choice == "Add a student":
        AddStudent()
    elif choice == "Add appointment":
        AddAppointment()
    elif choice == "View Appointments":
        displayAppointments()
    elif choice == "Add Assessment Marks":
        AddAssesmentMarks()
    elif choice == "Display list of students who have not submitted coursework":
        ViewUnsubmitted()
    elif choice == "View Module":
        displayModule()
    elif choice == "View Student":
        displayStudent()
    elif choice == "View student feedback":
        ViewFeedback()
    elif choice == "View struggling students":
        strugglingStudents()
    elif choice == "Assess trends":
        AssessingTrends()
