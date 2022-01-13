i = 1

while i <= 9 :
    if i % 2 == 0 :
        for z in range(1, 10) :
            print(f"{i} ^ {z} = {i ** z}")
    else :
        for z in range(1, 10) :
            print(f"{i} * {z} = {i * z}")
    i += 1