'''
Created on 16 Oct 2012

@author: Ollie Poole
'''


def getValidInput():
    num = str(input("Enter the eight digit credit card number: "))
    while len(num) != 8:
        num = str(input("Incorrect input, please try again: "))
    return num
#This function returns valid input only and will keep asking the user for input until correct input is given

def S1function(num):
    S1total = 0
    for count in range(7,0,-2):
        S1total += int(num[count])
    return S1total
    #This function adds the total of the numbers starting from the right hand side of the string with the step of 2
    
def S2function(num):
    S2total = ""
    for count2 in range(0,7,2):
        S2total += str((int(num[count2])*2)) #Converts the credit card numbers into integers to multiply them by 2 then turns them back to generate the string i.e. 10+2 = 102
    return S2total
    #This generates a string of all the numbers multiplied by 2

def S3function(S2total):
    S3total =0#Variable for adding the individual digits from section 2
    for count3 in range(0,len(S2total)):
        S3total += int(S2total[count3])
    return S3total
    #Adds all the digits of the string created in S2function

num = getValidInput()

S1total = S1function(num)
S2total = S2function(num)
S3total = S3function(S2total)

Gtotal = S1total + S3total 
Gtotal = str(Gtotal) #A grand total variable for finding the sum of the totals from Section 1 and Section 3

def checkDigitCheck(Gtotal):
    if Gtotal[-1:] == "0":
        return True
    else:
        return False
        #Function to check whether the Gtotal variable shows that the card is valid or not

if checkDigitCheck(Gtotal) == True:
    print("Your card is valid") #If the function returns the value 'True' it will output a suitable message
else:
    print("Your card is not valid")
    check = str(int(num[-1:])-int(Gtotal[-1:])+10) #Takes the total end digit away from the check digit and adds 10 to avoid negative numbers
    print("To be correct the check digit would be: ", check[-1:]) #Takes the end digit so the check bit is only one digit long
    
    
