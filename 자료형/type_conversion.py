# 형변환 (Type Conversion or Type Casting) : 값을 한 자료형에서 다른 자료형으로 바꾸는 것

print(int(3.8)) # 3 -> 괄호안의 값을 정수로 바꿔라

print(float(3)) # 3.0 -> 괄호안의 값을 소수로 바꿔라

print(int("2") + int("5")) # 7

print(float("1.1") + float("2.5")) # 3.6

print(str(2) + str(5)) # 25 -> 괄호안의 값을 문자열로 바꿔라

age = 7
# Wrong Syntex #
# print("제 나이는 " + age + "살입니다.")
# Correct Syntex #
print("제 나이는 " + str(age) + "살 입니다.") # 제 나이는 7살 입니다.

# Wrong Syntex #
# print(int("Hello world!")) -> 문자열은 Int로 형변환 불가

