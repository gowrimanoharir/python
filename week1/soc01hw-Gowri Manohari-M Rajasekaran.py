import random
# Day 1 Exercise
print("""
Day 1 - Exercises
-----------------
""")
#Andreas age in seconds 48618000
print('Andreas age', 48618000/(365*24*60*60)) #age of her son?? :)

#how many days for a 32 bit system to timeout if integer overflow has a bug
#Assuming to be signed binary system with one digit used to indicate positive/negative numbers
print('\n32 bit signed binary system will time out in', (1<<31)/(24*60*60), 'days')
print('32 bit signed binary system will time out in', (1<<31)/(24*60*60)/365, 'years')

#64 bit system to timeout if integer overflow has a bug
#Assuming to be signed binary system with one digit used to indicate positive/negative numbers
print('\n64 bit signed binary system will time out in', (1<<63)/(24*60*60), 'days')
print('64 bit signed binary system will time out in', (1<<63)/(24*60*60)/365, 'years')

# Day 3 Exercise
print("""
Day 3 - Exercises
-----------------""")
# Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.

fname = input('\nWhat is your first name: ')
lname = input('What is your last name: ')
print("Hello, "+fname+" "+lname+". Nice to meet you!!")

# Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)
favoriteNum = int(input('\nWhat is your favorite number: '))
print("This would be a Bigger better favorite number: "+str(favoriteNum+random.randint(1, 20)))

# Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:
ask = input('\nWhat do you want: ')
print("WHADDAYA MEAN "+ask.upper()+"?!? YOU'RE FIRED!!")

# Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
chapters = ["Getting Started", "Numbers", "Letters"]
pages = [1, 3, 10]

print("\nTable of Contents:\n")
for i in range(len(chapters)):
    print((("Chapter "+str(i+1)).ljust(11))+chapters[i].ljust(30)+str(pages[i]).rjust(3))

# Generate your random Civilization III world by generating a land 'X' tile or a water 'o' tile randomly:    

print("\nRandom Civilization\n")

world = ""
for x in range(11):
    for y in range(11):
        i = random.randint(0,1)
        if(i==1):
            c = 'X'
        else:
            c = 'o'
        world = world+c
    world = world + '\n'

print(world)

# Day 4 Exercise

# “99 Bottles of Beer on the Wall.” Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”
print("""
Day 4 - Exercises
-----------------""")

print("\nN Bottles of Beer on the Wall lyrics\n")

numBottles = int(input("Enter a number > 1 the song should start with: "))

while(numBottles >= 0):
    if(numBottles == 0):
        print("\nNo more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, 99 bottles of beer on the wall.")
    elif(numBottles == 1):        
        print("\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.") 
    else:               
        print("\n"+str(numBottles)+" bottles of beer on the wall, "+str(numBottles)+" bottles of beer.\nTake one down and pass it around, "+str(numBottles-1)+" bottles of beer on the wall.")
    numBottles = numBottles-1

# Deaf Grandma problem - Extended

print("\nDeaf Grandma Problem extended")

phrase = ''
endphrase = ''
extended = True

while(endphrase!='BYEBYEBYE'):
    if(not(phrase.isupper())):
        phrase = input("\nHUH?! SPEAK UP, GIRL! ")
    else:
        phrase = input("\nNO, NOT SINCE "+str(random.randint(1930, 1950))+"! ")
    if(phrase=='BYE'):
        endphrase=endphrase+phrase
    else:
        endphrase=''           

print("\nOK BYE!!!")

# Leap years problem

print("\nLeap years in given range\n")
start = int(input("Enter a start year: "))
end = int(input("Enter an end year: "))


def isLeapYear(year):
    if(year%4!=0 or (year%100 == 0 and year%400 != 0)):
        return False
    return True

leapYears = []
for i in range(start, end+1):
    if(isLeapYear(i)):
        leapYears.append(i)

print("\nLeap years between you given range are: "+str(leapYears)[1:-1])

# Sort the list entered byb the user
inputs = []
text = input("\nEnter the list of words you want to be sorted: \n")
while(text != ''):
    inputs.append(text)
    text = input()

if(len(inputs)==0):
    print("you did not enter any words")
else:
    print("\nSorted List: \n")
    print('\n'.join(sorted(inputs)))

# print moo n times

print("\n Moo Program\n")
def moo(n):
    for i in range(n):
        print('Moo!!')

n = int(input("Enter no of times to print moo: "))
moo(n)    

# Old style Roman numerals

print("\nRoman numerals\n")

rnumber = int(input("Enter a number between 1 and 3000 for roman numeral conversion: "))

thousands = int(rnumber/1000)
hundreds = int((rnumber%1000)/100)
tens = int((rnumber%100)/10)
units = rnumber%10


def oldRoman(num, str1, str2):
    temp = ''
    if(num >= 5):
        temp = temp+str1
    num = num%5
    for i in range(num):
        temp = temp + str2
    return temp

def newRoman(num, str1, str2, str3):
    temp = ''
    if(num==4):
        temp = str2+str1
        return temp  
    elif(num==9):
        temp = str2+str3
        return temp
    elif(num >= 5 and num < 9):
        temp = temp+str1     
    num = num%5
    for i in range(num):
        temp = temp + str2
    return temp    
 

def calculateRoman(rnumber):
    oldR = ''
    newR = ''       
    if(thousands > 0):
        for i in range(thousands):
            oldR = oldR+'M'
            newR = newR+'M'
    if(hundreds > 0):
        oldR = oldR+oldRoman(hundreds, 'D', 'C') 
        newR = newR+newRoman(hundreds, 'D', 'C', 'M') 
    if(tens > 0):
        oldR = oldR+oldRoman(tens, 'L', 'X') 
        newR = newR+newRoman(tens, 'L', 'X', 'C') 
    if(units > 0):
        oldR = oldR+oldRoman(units, 'V', 'I')         
        newR = newR+newRoman(units, 'V', 'I', 'X')  

    print("\nOld Romam notation for "+str(rnumber)+" is "+oldR)
    print("New Romam notation for "+str(rnumber)+" is "+newR)

if(rnumber < 0 or rnumber > 3000):
    print("\nYou did not enter a valid number between 0 & 3000")
else:
    calculateRoman(rnumber)    