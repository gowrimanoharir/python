import random
# # Day 1 Exercise
# print("""
# Day 1 - Exercises
# -----------------
# Alice in the Wonderland - alpha frequency distribution table
# """)


# filename = "alice_in_wonderland.txt"
# file = open(filename, "r")

# fileContent = file.read().lower()
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# frequency = {}

# for i in range(len(alpha)):
#     frequency[alpha[i]]=0

# for c in range(len(fileContent)):    
#     curChar = fileContent[c:c+1]
#     if(curChar.isalpha()):
#         frequency[curChar] = frequency[curChar]+1

# for i in frequency.keys():
#     print(i+': '+str(frequency[i]))

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