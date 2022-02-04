first_variable = "PYTHON"
print("Value of first:", first_variable)
print("Reference of first:", id(first_variable))

print("--------------")

second_variable = first_variable # making an alias
print("Value of second:", second_variable)
print("Reference of second:", id(second_variable))

second_variable = "TEST"
print("Value of second:", second_variable)
print("Reference of second:", id(second_variable))

first_list = [1,2,3,4]
print("Value of first:", first_list)
print("Reference of first:", id(first_list))

second_list = first_list
print("Value of first:", second_list)
print("Reference of first:", id(second_list))

second_list[0] = 4
print("Value of first:", first_list)
print("Reference of first:", id(first_list))
print("Value of first:", second_list)
print("Reference of first:", id(second_list))

second_list = [1,2,3,4]
second_list = list(first_list)