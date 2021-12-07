# numbers = []

## List 길이 나타내는 함수
# print(len(numbers)) # 0

## List 오른쪽 끝에 요소 추가 하는 함수
# numbers.append(5)
# print(numbers) # [5]
# numbers.append(8)
# print(numbers) # [5, 8]
# print(len(numbers)) # 2

## List 요소 삭제 함수
# numbers = [2, 3, 5, 7, 11, 13, 17, 19]
# del numbers[3] # numbers Index의 3번 요소를 삭제한다.
# print(numbers) # [2, 3, 5, 11, 13, 17, 19]


## List 중간에 요소 삽입 하는 함수
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers.insert(4, 37)
print(numbers) # [2, 3, 5, 7, 37, 11, 13, 17, 19]