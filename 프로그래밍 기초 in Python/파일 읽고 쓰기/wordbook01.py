import os

os.chdir('K:\\Python Group Study\\프로그래밍 기초 in Python\\파일 읽고 쓰기') # 절대 경로를 이 프로그래밍이 실행 된 후 바꿔준다. 프로그램이 끝나면 원상복구 됌

f = open('vocabulary.txt', 'r', encoding='UTF-8')

wordbook = []

for line in f :
    wordbook.append(line.strip().split(": "))

for english, korean in wordbook :
    input_english = input(f"{korean}: ")
    
    if input_english == english :
        print("맞았습니다!\n")
    else :
        print("아쉽습니다. 정답은 {}입니다.\n".format(english))


# 정답 코드
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        print(data)
        # english_word, korean_word = data[0], data[1]
        
        # # 유저 입력값 받기
        # guess = input("{}: ".format(korean_word))
        
        # # 정답 확인하기
        # if guess == english_word:
        #     print("맞았습니다!\n")
        # else:
        #     print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))
        
    


