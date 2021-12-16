import random

# 코드를 작성하세요.
num = random.randint(1, 20)
print(num)
count = 4
tried = 1

while count >= 0 :
    if count == 0 :
        print(f"아쉽습니다. 정답은 {num}였습니다.") 
        break 

    user_num = int(input(f"기회가 {count}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: "))
    
    if user_num > num :
        print("Down")
        count -= 1
        tried += 1
    elif user_num < num :
        print("Up")
        count -= 1
        tried += 1
    elif user_num == num :
        print(f"축하합니다. {tried}번만에 숫자를 맞히셨습니다.")
        break
    

