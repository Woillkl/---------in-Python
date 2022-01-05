def even_check(x):
    if x % 2 == 0:
        return True
    else :
        return False

n = 1
even_list = []

while n <= 100:
    if even_check(n) :
        even_list.append(n)
        n += 1
    else :
        n += 1

print(even_list)

