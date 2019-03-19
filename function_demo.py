# def square_plus_one(a):
#     result= a * a + 1
#     return result
# print(square_plus_one(4))
# print(square_plus_one(6))
# #next function
# def give_me_something(a,b):
#     result= a + b
#     return result
# print(give_me_something("pen","paper"))
# #next function quadriatic
# def quadratic(a,b,c):
#     result=((((-1*b)+((b**2)-(4*a*c))
#
#               ))/(2*a))
#     return result
# print(quadratic(1,2,1))
##
##
# # def fab(n):
# #     if n == 1 or n== 2:
# #         return 1
# #     else:
# #         return fab(n-2) + fab(n-1)
# # for i in range(1,10):
# #     print("The {}th Fabonacci number is {}.".format(i,fab(i)))
#     ##
#     ##function for sum of i
# # sum = 0
# # for i in range(1,5):
# #     print('in the {}th iternation, current i is {}'.format(i,i,sum))
# #     sum= sum+ i
# #     print('\t after adding i, the new sum is {}\n'.format(sum))
# # print(sum)
#     ##NEW FUNCTION FOR ITERATION OF A STREAM
# # total_value= 0
# # name='maddison'
# # #
# # for letter in name:
# #     # print(ord(letter))
# #     total_value = total_value+(ord(letter)-96)
# # print('The value of name {} is {}.'.format(name, total_value))
# team= "New England Patriots"
# print(len(team))
# letter = team[1]
# print(team[1])
# print(team[-1])
# print(team[len(team)-1])
# # #####duck functions
# prefixes = 'JKLMNOPQ'
# suffix= 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(letter + 'u' + suffix)
# #     else:
# #         print(letter + suffix)
# result = 0
# for number in range(1,1001):
#     if number%2==1:
#         result = result + number
# print(result)
team ='New England Patriots'
print(team[::-1])
