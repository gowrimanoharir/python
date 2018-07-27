import random

## Numbers
## Class
# print('1+2', 1+2)

# print('5 * (12-8) + -15',5 * (12-8) + -15)
# print('98 * (59872 / (13*8)) * -51', 98 * (59872 / (13*8)) * -51)

# print('modulus', 11%2)
# print('power', 2**8)
# print('bitshift', 1<<9)

# print('hours in a year', 365*24)
# print('mins in a decade', 365*24*60*10)
# print('age in seconds', 36*365*24*60*60)

## Exercise
# #Andreas age in seconds 48618000
# print('Andreas age', 48618000/(365*24*60*60)) #age of her son?? :)

# #how many days for a 32 bit system to timeout if integer overflow has a bug
# #Assuming to be signed binary system with one digit used to indicate positive/negative numbers
# print('32 bit signed binary system will time out in', (1<<31)/(24*60*60), 'days')
# print('32 bit signed binary system will time out in', (1<<31)/(24*60*60)/365, 'years')

# #64 bit system to timeout if integer overflow has a bug
# #Assuming to be signed binary system with one digit used to indicate positive/negative numbers
# print('64 bit signed binary system will time out in', (1<<63)/(24*60*60), 'days')
# print('64 bit signed binary system will time out in', (1<<63)/(24*60*60)/365, 'years')

# #calculate age based on birthday including time use python date  time modules


## Strings
## Class

# print('Hello World')
# print('I like '+'Butterpecan icecream') 
# print('blink '*5)

# print('12'+str(12))

# print('\\ escapes single \' OR ')
# print("write single ' inside double \" and vice versa")

# my_string="Be Lazzyyy"
# print("Dont be"+my_string)
# print("Coding"+my_string)

# food="Cereal"
# print("My breakfast was", food)

# food="Sandwich"
# print("My lunch was", food)

# # assignment by value
# var1=8
# var2 = var1
# print(var1, var2)

# var1="eight"
# print(var1, var2)

# # Loops and String lists
# name = "Wonder Women"

# print(name[1])
# print(len(name))

# for i in range(0, 6):
#     print(name[i])

# for i in range(0, len(name)):
#     print(name[i])    

# result = ''
# for i in range(0, len(name)):
#     if i%2 == 0:
#         result = result+name[i] 
# print(result)     

# # X land, o water

# # While

def generateWorld():
    world = []
    for x in range(11):
        for y in range(11):
            i = random.randint(0,1)
            if(i==1):
                c = 'X'
            else:
                c = 'o'
            world[x][y] = c
    return world

print(generateWorld())

marvel = ['Stark', 'Captain', 'Groot', 'Star Lord']
for m in marvel:
    print(m)


