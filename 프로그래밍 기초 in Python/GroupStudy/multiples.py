def check_five(num) :
    if num % 5 == 0:
        return True
    else : 
        return False
    
x = 200
plus = 0
num_list = []

while x <= 500 :
    if check_five(x):
        plus += x
        num_list.append(int(x))
        x += 1

    else :
        x += 1

print(plus)

print(sum(num_list))
