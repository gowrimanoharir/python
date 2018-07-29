import random
import inspect
# Day 1 Exercise
print("""
Day 1 - Exercises
-----------------
Alice in the Wonderland - alpha frequency distribution table
""")

filename = "alice_in_wonderland.txt"
file = open(filename, "r")

fileContent = file.read().lower()
alpha = 'abcdefghijklmnopqrstuvwxyz'
frequency = []

for i in range(len(alpha)):
    frequency.append([alpha[i], 0])

for c in range(len(fileContent)):    
    curChar = fileContent[c:c+1]
    if(curChar.isalpha()):
        for i in range(len(frequency)):
            if(frequency[i][0]==curChar):
                frequency[i][1] = frequency[i][1]+1
                break

print("\nFrequency as List of lists: ", frequency)                

print("\nFrequency in required format:\n") 
for i in range(len(frequency)):
    print(frequency[i][0]+': '+str(frequency[i][1]))


# Day 2 Exercise
print("""
Day 2 - Exercises
-----------------
""")    

print("\nNumbers to Letters the chr() method\n")
# There is something small that needs fixing. Can you spot it and fix it? (Hint, we only want A-Z and a-z)
# and Make a function that prints A-Z and a-z

upper = []
lower = []
charDict = {}

for i in range(65,125):
    char = str(chr(i))
    if(char.isalpha()):
        charDict[i] = char
        if(char.isupper()):
            upper.append(char)
        else:
            lower.append(char)

print('ASCII CODES', charDict)  

print("\nA-Z a-z\n")
print('A-Z', upper)                
print('a-z', lower)

# Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher ;))
print("\nCypher message\n")
cypher = []
message = input('Enter your message: ').lower()
for i in range(len(message)):
    cypher.append(ord(message[i]))

print("Your Number cipher is: ", cypher)

#Optional: Write a function that does a ceaser cypher (Google), ask the user a number, and shift their message by that number.
print("\nCeaser Cipher\n")
ceasarCypher = ''
ceasarNum = input('Enter your ceasar number: ')
for i in range(len(cypher)):
    newChar = cypher[i]+int(ceasarNum)
    if(newChar > 122):
        newChar = newChar - 122 + 97 - 1
    ceasarCypher = ceasarCypher+chr(newChar)

print("Your ceaser ciphered message is: ", ceasarCypher)

# Print the world

M = 'land'
o = 'water'

world = [[o,o,o,o,o,o,o,o,o,o,o],
[o,o,o,o,M,M,o,o,o,o,o],
[o,o,o,o,o,o,o,o,M,M,o],
[o,o,o,M,o,o,o,o,o,M,o],
[o,o,o,M,o,M,M,o,o,o,o],
[o,o,o,o,M,M,M,M,o,o,o],
[o,o,o,M,M,M,M,M,M,M,o],
[o,o,o,M,M,o,M,M,M,o,o],
[o,o,o,o,o,o,M,M,o,o,o],
[o,M,o,o,o,M,o,o,o,o,o],
[o,o,o,o,o,o,o,o,o,o,o]]

def printWorld():
    for i in range(len(world)):
        row = ''
        for j in range(len(world[i])):
            row = row+world[i][j]+','
        print('['+row+']\n')

def printReverseWorld():
    for i in range(len(world)-1, 0, -1):
        row = ''
        for j in range(len(world[i])-1, 0, -1):
            row = row+world[i][j]+','
        print('['+row+']\n')

print('\nYour World\n')
printWorld()    

print('\nYour Reverse world\n')  
printReverseWorld()  



#Write a function that generates an n x n sized board with either land or water chosen randomly.
def generateWorld():
    world = []
    for x in range(0, 11):
        row = []
        for y in range(0, 11):
            i = random.randint(0,1)
            if(i==1):
                c = 'X'
            else:
                c = 'o'
            row.append(c)
        world.append(row)
    return world

newWorld = generateWorld()
print('\nNew World:\n')
for i in range(len(newWorld)):
    print('\n', newWorld[i])

# Day 3 Exercise
print("""
Day 3 - Exercises
-----------------
""")   

# Modify "a" for another name in my_dict. Hint: you will have to create a new key-value pair, copy in the value, and then delete the old one.

my_dict = {
    "a": 35000,
    "b": 8000,
    "z": 450
}    

print("\nMy dict before rename of a: ", my_dict)

my_dict["new"] = my_dict["a"]
del(my_dict["a"])

print("\nMy dict after rename of a to new: ", my_dict)

# Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.

filename = "alice_in_wonderland.txt"
file = open(filename, "r")

fileContent = file.read().lower()
alpha = 'abcdefghijklmnopqrstuvwxyz'
frequency = {}

for i in range(len(alpha)):
    frequency[alpha[i]]=0

for c in range(len(fileContent)):    
    curChar = fileContent[c:c+1]
    if(curChar.isalpha()):
        frequency[curChar] = frequency[curChar]+1

print("\nFrequency as dictionary: ", frequency)     

print("\nFrequency in required format:\n")  
for i in frequency.keys():
    print(i+': '+str(frequency[i]))

# Create a dictionary with your own personal details, feel free to be creative and funny so for example, you could include key-value pairs with quirky fact, fav quote, pet. Practice adding, modifying, accesing.    
my_faves = dict(name = "Gowri", superhero = "Iron Man, Wonder Woman", food = "dosa")

print("\nMy favorites: ", my_faves)

my_faves["iluv"] = "Travel"

print("\nMy favorites after addition: ", my_faves)

my_faves["iluv"] = "Travel, Procedurals"

print("\nMy favorites after modification: ", my_faves)

del(my_faves["superhero"])

print("\nMy favorites after deletion: ", my_faves)

# Review the chat reply of today's beautiful class interaction and instantiate a student variable for everyone who shared their dream.

class Student():
    def __init__(self, name, discord_id, fav_food, dream):
        self.name = name
        self.discord_id = discord_id
        self.fav_food = fav_food
        self.dream = dream

    def my_print(self):
        print(self.name+" "+self.discord_id+" "+self.fav_food+" "+self.dream)

    def self_print(self):
        for attr, value in self.__dict__.items():
            print(attr+": "+value)

s1 = Student("Gowri Rajasekaran", "gowri", "Dosa", "World with Liv & Let Liv")         
s2 = Student("Bituin Callanta", "bituin [gold]", "sashimi", "Lessen the gender wage gap")   
s3 = Student("Andreea Visanoiu", "andreea", "wontonmee", "becoming an University teacher")   
s4 = Student("Jessica", "Jessi_RS [Gold]", "pasta", "work as developer by end of the year")   

print("\nStudent Group:\n")
s1.my_print()
s2.my_print()
s3.my_print()
s4.my_print()

s1.fav_food = "Enchiladas"
del s1.discord_id

print("\nS1 after modification & deletion:\n")
s1.self_print()

#Translate the real world 1MWTT student into a Student class, decide on all the attributes that would be meaningful.

print('\nCreate Student class\n')

class StudentClass():
    def __init__(self, firstname="", lastname="", email="", phoneNum="", country="", genderIdentity="", codingLevel=""):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phoneNum = phoneNum
        self.country = country
        self.genderIdentity = genderIdentity
        self.codingLevel = codingLevel

    def self_print(self):
        for attr, value in self.__dict__.items():
            print(attr+": "+value)

args = inspect.getfullargspec(StudentClass.__init__).args


addMore = True
students = []

while(addMore):
    s=[]
    for i in range(1, len(args)):
        s.append(input('Enter student\'s '+args[i]+': '))
    students.append(StudentClass(*s))
    more = input("\nDo you want to add more students? y/n: ") 
    addMore = more == ('y' or 'Y')

print('\nReview the students that were created:\n')

for i in range(len(students)):
    print('\nStudent '+str(i+1)+':\n')
    students[i].self_print()