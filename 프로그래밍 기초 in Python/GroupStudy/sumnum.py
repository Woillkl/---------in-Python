sum = 0
x = 0

while x <= 10:
    sum += x
    x += 1



sum = 0
x = 0

num_list = []

while x <= 10 :
    num_list.append(int(x))
    x += 1

sum = sum(num_list)
print(sum)