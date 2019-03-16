# print(3.14e-2)
# length1_of_number= len(str(2**1000000))
# print(length1_of_number)
# # print(len('Maddison'))
# import math
# print(math.pi)
# print(math.sqrt(25))
# import random
# print(random.random())
# print(int(random.random()*100))
# print(random.randint(1,6))
# # print(random.choice({"ben","alice","joe"}))
# print(random.choice([2,3,4]))
# lower = int(input("please a number as the lover bound:"))
# upper = int(input("another one as upper bound:"))
# print(random.randint(lower,upper))
######Strings
# print("I'am\"OK\".")
# print('I\'m learning\n\nPython.')
# #####Boolean
# print(3>2)
# print(3>5)
# print(3>2 or 3>5 or False or 100 < 100)
age=int(input("How old are you?"))
answer= input('Are you in US?')
IS_IN_US = True
if answer == "no":
    IS_IN_US = False
if age <= 21 and IS_IN_US == True :
    print("no you cant")
else:
    print("yes")
