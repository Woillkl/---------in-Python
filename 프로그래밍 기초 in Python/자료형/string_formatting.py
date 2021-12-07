# 오늘은 2021년 12월 3일입니다.
year = 2021
month = 12
day = 3
# Wrong Syntex #
# print("오늘은" + year + "년" + month + "월" + day + "일입니다.")
# Correct Syntex #
print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")

# format method
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day)) # String Formatting

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day)) # 오늘은 2021년 12월 3일입니다.

print("저는 {1}, {0}, {2}를 좋아합니다.".format("박지성", "유재석", "빌 게이츠")) # 저는 유재석, 박지성, 빌 게이츠를 좋아합니다.

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2}입니다".format(num_1, num_2, num_1 / num_2)) # 1 나누기 3은 0.3333333333333333입니다
print("{0} 나누기 {1}은 {2:.2f}입니다".format(num_1, num_2, num_1 / num_2)) # 1 나누기 3은 0.33입니다
print("{0} 나누기 {1}은 {2:.4f}입니다".format(num_1, num_2, num_1 / num_2)) # 1 나누기 3은 0.3333입니다
print("{0} 나누기 {1}은 {2:.0f}입니다".format(num_1, num_2, num_1 / num_2)) # 1 나누기 3은 0입니다

# format method
# 가장 오래된 방식 (%)
name = "Sean"
age = 26
print("My name is %s and I am %d years old." % (name, age)) # My name is Sean and I am 26 old.

# 현재 가장 많이 쓰는 방식 (format method)
print("My name is {} and I am {} years old.".format(name, age)) # My name is Sean and I am 26 old.

# 새로운 방식(f-string)
print(f"My name is {name} and I am {age} years old.") # My name is Sean and I am 26 old.