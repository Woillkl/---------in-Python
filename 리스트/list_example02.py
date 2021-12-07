numbers = [19, 13, 2, 5, 3, 11, 7, 17]

# # 작은 것 부터 큰 것으로 정렬
# new_list = sorted(numbers)
# print(new_list) # [2, 3, 5, 7, 11, 13, 17, 19]

# # 큰 것부터 작은 것으로 정렬
# new_list = sorted(numbers, reverse=True)
# print(new_list) # [19, 17, 13, 11, 7, 5, 3, 2]


# Wrong Code -> sort함수는 List 자체를 sorting 하므로 Return 값이 없다. #
# print(numbers.sort())
# Correct Code #
# 작은 것에서 큰것으로 정렬
numbers.sort()
print(numbers) # [2, 3, 5, 7, 11, 13, 17, 19]
# 큰 것에서 작은 것으로 정렬
numbers.sort(reverse=True)
print(numbers) # [19, 17, 13, 11, 7, 5, 3, 2]

## sorted : 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
## sort : 아무것도 리턴하지 않고, 기존 리스트를 정렬





