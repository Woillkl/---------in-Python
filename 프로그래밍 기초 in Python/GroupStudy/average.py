count = 0
totalrate = 0

for i in range(0,5) :
    rate = int(input("Driver RAte :")) 
    totalrate += rate
    count += 1

print(f"Average of Driver Rate : {totalrate / count}")