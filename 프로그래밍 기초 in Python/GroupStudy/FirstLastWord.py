import os
from random import randint

def update_computer_brain(x, y):
    with open('FirstLastWord.txt', 'a+', encoding='UTF-8') as f:
        for value in x:
            if value not in y:
                f.write(f"{value}\n")



os.chdir('K:\\Python Group Study\\프로그래밍 기초 in Python\\GroupStudy')

f = open('FirstLastWord.txt','r', encoding='UTF-8') # Brings Words that Computer has

sys_wdbook = [] # List of words that computer has
game_wdbook = [] # List of words that used in game
turn_count = 0 # How many turns went

for line in f : # Read the file that has the words
    sys_wdbook.append(line.strip())

while True: # Select who attacks first
    try:
        print("게임을 종료하시려면 언제든지 2번을 눌러주세요.")
        turn = int(input("선공 후공을 정해주세요.(0: 선공, 1: 후공, 2: 종료) : "))
        if turn == 0 or turn == 1 or turn == 2:
            break
        else:
            print("번호가 잘못되었습니다.")
    except ValueError: #Error exception while choosing the turns
        print("숫자를 입력해주세요.")

while True: # Game starts
    if int(turn) == 2 :
        print("Game Ended!!")
        exit()

    user_input = input("세상에 존재하는 단어(2~3자) 하나를 입력해주세요 :") # User will input word

    if int(turn) == 0 : # User's First Attack
        sys_wdbook_count = 0
        if user_input == "2": 
            print("사용자에 의해 게임이 종료되었습니다.")
            exit()

        if len(user_input) > 3 or len(user_input) < 2:
            print("글자수를 맞춰주세요.")

        elif len(user_input) <= 3 and len(user_input) >= 2:
            if turn_count == 0: # 1st user's input
                game_wdbook.append(user_input)
                turn_count += 1

            elif turn_count > 0 and sys_input[-1] == user_input[0]: # User's input during game
                if user_input not in game_wdbook :
                    game_wdbook.append(user_input)
                    turn_count += 1
                elif user_input in game_wdbook:
                    print("이미 사용된 단어입니다.")
                    print(f"컴퓨터 입력 : {sys_input}")

            elif turn_count > 0 and sys_input[-1] != user_input[0] :
                print(f"{turn_count}번만에 제가 이겼습니다.")
                exit()
        
            for index in sys_wdbook: # Computer input
                sys_wdbook_count += 1
                if index[0] == user_input[-1] and index not in game_wdbook: # Computer has the word that match
                    sys_input = index
                    print(f"컴퓨터 입력 : {sys_input}")
                    game_wdbook.append(sys_input)
                    turn_count += 1
                    break
                elif sys_wdbook_count == len(sys_wdbook):
                    update_computer_brain(game_wdbook, sys_wdbook) # Update word to computer which it doesn't have
                    print(f"{turn_count}번만에 제가 졌습니다.")    
                    exit()

        




    elif int(turn) == 1: # Computer's First Attack
        if turn_count == 0:
            sys_input = sys_wdbook[randint(0,len(sys_wdbook)-1)]
            print(sys_input)
            game_wdbook.append(sys_input)
            
    
            

    
    

        
        
        
        