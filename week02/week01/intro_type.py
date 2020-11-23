# # integer_variable = 6
# # print("integer_variable",type(integer_variable))

# # i = 5
# # print("variable type is ",type(i))

# # i = "bhaskr"
# # print("variable type is ",type(i))

# # s = 4.565

# # print (("variable type ",type(s)))




# # print("hey amrutha enter ur number")
# # num = int(input())

# # print("hey bhaskar enter your num")
# # num2 = int(input())

# # print(num * num2)



# # print("hey! enter your name")
# # name = input()

# # print("hey! enter your age")
# # age = input()

# # print("hey!! my name is",name,"my age is",age)



# print("wts ur name")

# name = input()

# print("wts ur age")

# age = input()

# print ("hey my name is",name,"age is ",age)


# i = "5"

# print ("variable_type",type(i))

# i = int("8")

# print("vaiable_type",type(i))

# print("hey enter your num")

# num = int(input())

# print("the reminder is ", num % 10)


# a = 5
# b = 6

# if a == 5 and b == 6:
#     print(True)
    
# else:
#     print("its false")


# weather = "sunny"

# if weather == "raining":
#     print("I will wear raincoat")
# elif weather == "sunny":

#     print("i will wear sunglasses")


# no1 = 5
# no2 = 20

# if no1 == 5 * 1:
#     if no1 % 2 == 0:
#         print("The no is even")
#     elif no1 % 2 != 0:
#         print ("odd")

# else:
#     print(False)

# print(True)

# no1 = 100
# no2 = 300

# if no1 == 10:
#     print("the num is 100")
# else:
#     if no2 == 300:
#         print("the no is 300")
#         if no1 == 100:

#             print("the no is 100")
#     else:
#         print("not valid")

# a = 1
# b = 20

# if a == 1:
#     print("no need to go elif")
#     if a == 1:
#         print("if fail entered elif")
#     else:
#         print("you fail your expectation")

# print("hey!! ,enter your no")

# user_input = int(input())

# if user_input == 1:
#     print(":)")
# elif user_input == 0:
#     print(":(")
# else:
#     print("enter correct no dear","you entered no", user_input)
    

# first_name = "Koilada"
# last_name = "bhaskar"

# if first_name == "koilada":
#     print("i know you")
# if last_name == "Bhaskar":
#     print("hey bachi i know u")
# else:
#     print("may be know u")

# first_name = "koilada"
# last_name = "Bhaskar"

# if first_name == "Koilada":
#     if last_name == "Bhaskar":
#         print("he is from vizag")
# else:
#     print ("he is not from vizag")


# a = 4
# if (a % 2 == 0 or a >= 4):

#     if (a % 2 == 0):
#         print("The no is even")
    
#         if (a == 4):
#             print("The no is 8")

#     if (a >= 4):
#         print("The no is greater than or equal to 4")

# print("program completed")

# print("enter value")

# user_input = int(input())


# if user_input % 3 == 0 and user_input % 5 == 0:
#     print("fizz_buzz") 
# else:
#     if (user_input % 5 == 0):
#         print("fizz")
#     if (user_input % 3 == 0):
#         print("buzz")

    
# print("this not not divisible by both")



# user_input = int(input("hey enter no"))

# for i in range (1 , user_input + 1):
#     if i % 5 == 0 and i % 3 ==0:
#         print(i,"fizz_buzz")
#     elif i % 5 == 0:
#         print (i,"fizz")
#     elif i % 3 == 0:
#         print (i,"buzz")
#     else:
#         print (i)


# for i in range(3):
#     print ("j loop start for i",i)
#     for j in range(3):
#         print (i,j)
#     print("j loop ends for i",i)



# for i in range(5):
#     for j in range(5):
#         for k in range(5):
#             print(i, j , k)


# print ("hello",end="    ")
# print("hi",end="    ")
# print("hey")

# for i in range(1,21):
#     print("**********************")
#     print("table of ",i)
#     for j in range(1,50+1):
#         print(i, "X", j ,"=", i * j)
#     print("888888888888888")




# table program



# for i in range(1,50):
#     print("______******________******______")
#     for j in range(1,11):
#         print(i, "X", j , "=", i * j)


# sum = 0
# for j in range(2, 4):
#     for i in range(1, 3):
#         if i % 2 == 0:
#             print(i + j)

# patterns

# for i in range(4):
    
#     for j in range(4):
#         print("#", end="")
#     print()

# for i in range (15):
#     for j in range(i):
#         print("#",end="")
#     print()
    
# 

no1 = int(input("enter 1st value.......>" " ")) 
choice = input("enter operator ex: + , - , * , / ->" " ")

no2 = int(input("enter 2nd value.......>" " ")) 

if choice != "+" or "-" or "*" or "/":

    if choice == "+":
        print(no1 + no2)
    elif choice == "-":
        print(no1 - no2)
    elif choice == "*":
        print (no1 * no2)
    print("Please enter valid operator")
