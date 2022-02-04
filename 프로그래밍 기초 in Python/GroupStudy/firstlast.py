while True :
    word = input("세글자 단어를 입력하세요(종료 : 2) : ")
    if word == "2" :
        exit()

    else :
        if word[0] == word[-1] :
            print(f"{word}는 첫번째와 마지막 글자가 같다.")
        else :
            print(f"{word}는 첫번째와 마지막 글자가 다르다.")