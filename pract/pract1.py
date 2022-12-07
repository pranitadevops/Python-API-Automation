# # data = input("Please enter number:  ")
# # data= int(data)
# # if (data%2==0):
# #     print("Even number")
# #
# # else:
# #     print ("ODD")
#
#
# # If number is positive, print message
# # if number is Negative, print message
# # check number is even or odd
#
# num = input("Please enter the number: ")
# num = int(num)
#
# # if num < 0:
# #     print("Number is Negative")
# # else:
# #     if  num % 2 == 0:
# #         print("number is even and positive")
# # else:
# #         print("Number is Odd")
# # elif num % 2 == 0:
# #         print("number is even and positive"
# # else:
# #         print("Number is Odd")
#
#
# # ******** And OR*********
# # if num >= 0 | num % 2 == 0:
# #     print("Number is even")
# # else:
# #     print("Not correct")
#
#
# if num >= 0:
#     if num % 2 == 0:
#         print("Number is even")
#     else:
#         print("Number is ODD")
#
# else:
#     print("number is less than given input :)")


# ******************* Addition of two numbers:
# A= 5
# B = 10
# sum = A + B
# print(sum)


# *********************Factorial
# import math
#
# num = input("Enter the number:::")
# num = int(num)
# fact = math.factorial(num)
# print("Factorial is", fact)

# Intrest rate

# P = 10000
# I = 5
# T = 5

# p = int(input("Enter the pricipal amt:"))
# i = int(input("Enter the interest amt:"))
# t = int(input("Enter the time:"))
# total = p*i*t/100
# print(total)


# if OR and AND conditions
# var = int(input("Enter a Marks: "))
#
# if var > 100 or var < 0:
#     print("Marks are appropriate")
# else:
#     print("Not upto level")

programing_lang = ['java', 'php', 'java','py',"c","py","jscript","css","py","c","c++"]
new_list = []
for lang in programing_lang:
    if(programing_lang.count(lang)==1):
        new_list.append(lang)

print(new_list)






