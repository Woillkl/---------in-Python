# numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# # 리스트 뒤집기
# # 코드를 입력하세요.
# mid = len(numbers) / 2 # 4
# length = len(numbers) - 1 # 7

# for i in range(len(numbers)):
#     if i  >= mid:
#         break
#     else :
#         temp = numbers[length]
#         numbers[length] = numbers[i]
#         numbers[i] = temp
#         length -= 1

# print("뒤집어진 리스트: " + str(numbers))

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 20, 21]

# 리스트 뒤집기
# 코드를 입력하세요.
mid = len(numbers) / 2 # 4
length = len(numbers) - 1 # 7

for i in range(len(numbers)):
    if i  >= mid:
        break
    else :
        temp = numbers[length]
        numbers[length] = numbers[i]
        numbers[i] = temp
        length -= 1

print("뒤집어진 리스트: " + str(numbers))