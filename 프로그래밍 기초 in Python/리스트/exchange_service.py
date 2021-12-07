# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    # 코드를 입력하세요.
    dollar = krw / 1000
    return dollar


# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    # 코드를 입력하세요.
    jpy = usd * (1000 / 8)
    return jpy

# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))

# prices를 원화(￦)에서 달러($)로 변환하기
# 코드를 입력하세요.
a = 0 

while a < len(prices) :
    prices[a] = krw_to_usd(prices[a])
    a += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))

# prices를 달러($)에서 엔화(￥)으로 변환하기
# 코드를 입력하세요.
a = 0

while a < len(prices) :
    prices[a] = usd_to_jpy(prices[a])
    a += 1
# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(prices))