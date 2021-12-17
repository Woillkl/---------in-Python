import os
import random

# 절대 경로 바꿔주는 코드
os.chdir('K:\\Python Group Study\\프로그래밍 기초 in Python\\파일 읽고 쓰기')

word_book = []

f = open('vocabulary.txt', 'r', encoding='UTF-8')

for line in f :
    word_book.append(line.strip().split(": "))

while True:
    question = word_book[random.randint(0,len(word_book)-1)]
    korean = question[1]
    english = question[0]

    input_english = input(f"{korean}: ")
    if input_english == 'q' :
        break
    elif input_english == english:
        print("맞았습니다!\n")
    else :
        print(f"틀렸습니다. 정답은 {english}입니다.\n")
    
# 정답 코드(Dictionary 사용)
import random

# 사전 만들기
vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# 목록 가져오기
keys = list(vocab.keys())

# 문제 내기
while True:
    # 랜덤한 문제 받아오기
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab[english_word]
    
    # 유저 입력값 받기
    guess = input("{}: ".format(korean_word))
    
    # 프로그램 끝내기
    if guess == 'q':
        break
    
    # 정답 확인하기
    if guess == english_word:
        print("정답입니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))
