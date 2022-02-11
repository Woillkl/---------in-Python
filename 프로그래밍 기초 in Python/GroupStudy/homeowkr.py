def compare(sys_word, user_input) :
    if sys_word[-1] == user_input[0] :
        print("정답입니다.")
    else :
        print("틀렸습니다.")



print("끝말잇기 게임을 시작하겠습니다. ")
fixed = input("첫 단어를 입력하세요: ")

while True :
    com_word = input("다음 단어를 입력하세요.(Exit:2) : ")
    
    if com_word == "2" :
        exit()

    compare(fixed,com_word)
    fixed = com_word
    
