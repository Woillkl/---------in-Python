# 상수 (constant) -> 바뀌지 않는 변수
# 상수를 만드는 규칙(대문자)
# pi = 3.14 # 원주율 '파이'
PI = 3.14

# 반지름을 받아서 원의 넓이 계산
def calculate_area(r):
    return PI * r * r

radius = 4 # 반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 6
print("반지름이 %d면, 넓이는 %.2f" %(radius, calculate_area(radius)))

radius = 7
print(f"반지름이 {radius}이면, 넓이는 {calculate_area(radius)}")