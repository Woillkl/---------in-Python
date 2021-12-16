f = open('프로그래밍 기초 in Python\\파일 읽고 쓰기\\chicken.txt', 'r', encoding='UTF-8')

chicken = []
amount = 0

for line in f :
    chicken.append(line.strip().split("일: "))
    
month = len(chicken)

for x, y in chicken :
    amount += int(y)

print(amount / month)

# 정답 코드
with open('프로그래밍 기초 in Python\\파일 읽고 쓰기\\chicken.txt', 'r', encoding='UTF-8') as f:
    total_revenue = 0
    total_days = 0
    
    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])  # 그날의 매출 # [0]에는 ?월 이 들어가고 [1]에는 금액이 들어가있음

        total_revenue += revenue
        total_days += 1

    print(total_revenue / total_days)