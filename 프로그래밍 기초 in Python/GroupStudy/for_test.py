result = [79, 65, 89, 90, 68]

for i in range(0, len(result)) :
    if result[i] >= 80 :
        print(f"{i+1}는 합격입니다.")
    else :
        print(f"{i+1}는 불합격입니다.")

for i in result :
    print(i)