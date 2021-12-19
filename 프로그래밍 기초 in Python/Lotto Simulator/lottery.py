from random import randint

# My Code #
lotto_list = [] # List contains "n" int
num_list = [] # List contains 1 ~ 46

def generate_numbers(n) : # generate number from 1 to 45
    for x in range (1,46) : 
        num_list.append(x)
    
    while True: 
        ran_num = num_list[randint(0,len(num_list) -1)]
        if ran_num not in lotto_list :
            lotto_list.append(ran_num)
        if len(lotto_list) == n :
            break

    return lotto_list

def draw_winning_numbers() : # generate 1 bonus number
# 이 함수의 문제점은 draw_winning_numbers 하나만 호출하게 되면 숫자 한개밖에 나오지 않는다.
# 해결책은 함수 안에 generate_numbers(n)을 호출해 줘야함 
    # while True :
    #     ran_num = randint(1,45)
    #     if ran_num not in lotto_list :
    #         lotto_list.append(ran_num)
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]      
            

def count_matching_numbers(list_1, list_2) : # count matching numbers between user_num and system_num
    win_num_count = 0
    for x in list_1[:6] :
        if x in list_2 :
            win_num_count += 1
    return win_num_count

def check(numbers, winning_numbers) : # check amount
    count = count_matching_numbers(numbers, winning_numbers)
    

    if count == 6 :
        for x in numbers :
            if x == winning_numbers[6] :
                return 50000000
        return 1000000000
    elif count == 5 :
        return 1000000
    elif count == 4 :
        return 50000
    elif count == 3 :
        return 5000
    else : return 0

    




# # 정답 코드
# def generate_numbers(n) :
#     lotto_list = []
#     while len(lotto_list) < n :
#         ran_num = randint(1,45)
#         if ran_num not in lotto_list :
#             lotto_list.append(ran_num)
        
#     return lotto_list

# def draw_winning_numbers() :
#     winning_numbers = generate_numbers(7)
    
#     return sorted(winning_numbers[:6]) + winning_numbers[6:]

# def count_matching_numbers(numbers, winning_numbers):
#     count = 0

#     for num in numbers:
#         if num in winning_numbers:
#             count = count + 1

#     return count