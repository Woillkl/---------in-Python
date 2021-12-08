# 자리수 합 리턴
def sum_digit(num):
    # 코드를 입력하세요.
    str_num = str(num)
    total = 0
    for i in range(len(str_num)) :
        total += int(str_num[i])
    return total


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.
main_total = 0

for i in range(1,1001):
    main_total += sum_digit(i)

print(main_total)