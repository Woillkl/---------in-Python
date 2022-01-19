thisdict = {
    "사과" : "apple", 
    "바나나" : "banana", 
    "사자" : "lion", 
    "기차" : "train",
    "호랑이" : "tiger", 
    "나무" : "tree", 
    "감자" : "potato", 
    "사랑" : "love"
    }

print("Dictionary 안의 '사'로 시작하는 단어의 영단어 입니다.")
for key, value in thisdict.items() :
    if key[0] == "사" :
        print(f"{key} : {value}")


for key, value in thisdict.items() :
    word = "{}".format(key)
