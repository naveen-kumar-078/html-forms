# age=20

# if age>18:
#     print("you are eligible")
# else:
#     print("you are not eligible")



# mark = 66

# if mark>=100:
#     print("grade a")
# elif mark > 80:
#     print("GRADE B")
# elif mark > 70:
#     print("Grade C")
# else:
#     print("GRADE F")


# num = 19

# if num > 20:
#     print("its an positive")
#     if num %2 == 0:
#         print("its an even number")
#     else:
#         print("its an odd number")
# else:
#  print("its an negative number")

# Creating a list (array)


# from array import array

# numbers = array("i",[20,30,40,50])
# print(numbers)
# print(numbers[0])
# numbers.append(70)
# numbers.remove(40)
# print("updated list:",numbers)


# import numpy as nk

# numbers = nk.array([10,20,30,40,50])
# print("Numpy values",numbers)
# print("first element:",numbers[0])
# print("updated element:",numbers*2)



# the_list = [10,20,30,40]

# print("List of number:",the_list)

# the_list.append(60)
# the_list.remove(30)

# print("the updated list",the_list)


# fruits = ["apple","orange","mango","banana"]
# print(fruits[0])
# fruits.append('watermelon')
# print(fruits)




# array = [1,2,3,3,4]
# s = set(array)
# print(s)


# marks = {
#     "kumar":[98,97,96],
#     "ravi":[88,87,86],
#     "siva":[78,77,76]
# }

# marks["jj"]=[90,60,80]
# print(marks)

# print(marks["jj"][0])





# # import array

# # marks = {
# #     "jessi": array.array("i",[90,95,92,98]),
# #     "rosy": array.array("i",[10,11,12])
# # }

# # print(marks["rosy"][0])
# # print(marks)


# fruits = ["apple","orange","mango"]

# for fruit in fruits:
#     print(fruit)


# for i in range(5):
#     print(i)



#     for letter in "loop":
        # print(letter)



# for i in range(3):
#     for j in range(2):
#         print(i,j)


# int_str = "7,8,35"
# number = int_str.split()
# first = ord(number[0][0])-ord('0') # so the value is 7
# second  = ord(number[-1][-1])-ord("0") # so the value is 5
# result  = first + second
# print(result)



# int_str = ("12345")
# first = int(int_str[0][0])+int(int_str[-1][-1])
# print(first)


import math

a =9.75

print(round(a))