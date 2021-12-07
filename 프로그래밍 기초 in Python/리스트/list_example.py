# 리스트 (list)
numbers = [2, 3, 5, 7, 11, 13] # 정수형이 담긴 리스트
names = ["윤수", "혜린", "태호", "영훈"] # 문자열이 담긴 리스트

# 인덱식 (indexing)
print(names[1]) # 혜린

print(numbers[1] + numbers[3]) # 10

num1 = numbers[1]
num3 = numbers[3]
print(num1 + num3) # 10

# print(numbers[6]) // Index out of range 에러 뜸

print(numbers[-1]) # 13
print(numbers[-6]) # 2

# print(numbers[-7]) // Index out of range 에러 뜸

# 리스트 슬라이싱(list slicing)
print(numbers[0:4]) # [2, 3, 5, 7]  index 0 ~ 3 까지 불러옴

print(numbers[2:]) # [5, 7, 11, 13] index 2 ~ 끝까지

print(numbers[:3]) # [2, 3, 5] index 처음부터 ~ 2 까지

new_list = numbers[:3] # [2, 3, 5]
print(new_list[2]) # 5