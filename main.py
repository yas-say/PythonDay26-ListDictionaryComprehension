# list = [1,2,3]
# newlist = [n+1 for n in list]
# print(newlist)
#
#
# name = "Yasowant"
# name_list = [letter for letter in name]
# print(name_list)
#
# dbl_num = [num*2 for num in range(1, 5)]
# print(dbl_num)
#
#
# names = ["Yas", "Sanjam", "Sarita"]
# new_names = [name.upper() for name in names if len(name) > 3]
# print(new_names)
#
# #square
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [ n ** 2 for n in numbers]
# print(squared_numbers)
#
# #even number
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num % 2 == 0]
# print(result)
#
#
# #common element between file
# with open("file1.txt") as file1:
#     data1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     data2 = file2.readlines()
#
# result = [int(num) for num in data1 if num in data2]
# print(result)


#Dict compre
import random
names = ["Yas", "Sanjam", "Sarita"]
scores = {name:random.randint(1,100) for name in names}
print(scores)

#Dict compre2
passed1 = {k:scores[k] for k in scores.keys() if scores[k] > 45}
passed2 = {k:v for (k,v) in scores.items() if v>45}
print(passed1)
print(passed2)


#Dict compre from list
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sent_list = sentence.split(" ")
result = {k:len(k) for k in sent_list}
print(result)