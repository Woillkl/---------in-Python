# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
# 코드를 입력하세요
def append(a) :
    return numbers.append(a)
append(1)
append(7)
append(3)
append(6)
append(5)
append(2)
append(13)
append(14)
print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요
b = 0
while b < len(numbers) :
    if numbers[b] % 2 != 0 :
        del numbers[b]
        continue
    b += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0,20)
print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
numbers.sort()
print(numbers)
