import os

os.chdir('K:\\Python Group Study\\프로그래밍 기초 in Python\\파일 읽고 쓰기') # 절대 경로를 이 프로그래밍이 실행 된 후 바꿔준다. 프로그램이 끝나면 원상복구 됌

f = open('vocabulary.txt', 'a', encoding='UTF-8')

while True :
    english = input("영어 단어를 입력하세요: ")
    if english == 'q' :
        break

    korean = input("한국어 뜻을 입력하세요: ")
    if korean == 'q' :
        break
        
    f.write(f"{english}: {korean}\n")
