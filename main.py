list = [1,2,3]
newlist = [n+1 for n in list]
print(newlist)


name = "Yasowant"
name_list = [letter for letter in name]
print(name_list)

dbl_num = [num*2 for num in range(1, 5)]
print(dbl_num)


names = ["Yas", "Sanjam", "Sarita"]
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

#square
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [ n ** 2 for n in numbers]
print(squared_numbers)

#even number
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)
