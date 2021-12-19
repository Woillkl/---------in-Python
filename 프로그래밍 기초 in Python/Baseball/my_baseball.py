from random import randint

def generate_numbers(): # Gnereate 3 numbers within 0~9
    numbers = []

    while len(numbers) < 3: # Add numbers in "numbers" list
        rannum = randint(0,9)
        if rannum not in numbers: # List "numbers" duplication check
            numbers.append(rannum)

    return numbers

def take_guess() : # get 3 numbers from user
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = [] # 3 number's list from user input
    input_count = 1

    while input_count < 4 : # get 3 numbers from user input
        user_input = input(f"{input_count}번째 숫자를 입력하세요: ")
        if int(user_input) >= 10 or int(user_input) < 0: 
            print("범위를 벗어나는 숫자입니다. 다시 입려하세요.")
        elif int(user_input) in new_guess :
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else :
            new_guess.append(int(user_input))
            input_count += 1

    return new_guess

def get_score(guesses, solution) :
    strike_count = 0
    ball_count = 0

    for x in range(len(solution)):
        sys_num = solution[x]
        for i in range(len(guesses)):
            user_num = guesses[i]
            if sys_num == user_num and i == x :
                strike_count += 1
            elif sys_num == user_num and i != x :
                ball_count += 1


    return strike_count, ball_count


print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")

count = 1
ans_list = generate_numbers()
print(ans_list)

while True:
    guess_list = take_guess()
    strike, ball = get_score(guess_list, ans_list)
    
    if strike != 3 :
        print(f"{strike}S {ball}B\n")
        count += 1
        


    if strike == 3:
        print(f"{strike}S {ball}B\n") 
        print(f"축하합니다. {count}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.")
        break
    

