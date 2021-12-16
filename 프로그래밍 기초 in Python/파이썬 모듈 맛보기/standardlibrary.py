# standard library (표준 라이브러리)
# 표준 라이브러리 안에는 다양한 모듈들이 존재함

# import math

# print(math.log10(100))
# print(math.cos(0))
# print(math.pi)

# import random

# random.random() # 0.0과 1.0 사이의 랜던한 갑이 출력이 됌
# print(random.random())
# print(random.randint(1, 20))

import os # 우리의 운영체제를 조작하기 위한 모듈

print(os.getlogin()) # 현재 사용하고 있는 컴퓨터의 어떤 계정에 로그인 되어 있나를 구할 수 있음
print(os.getcwd()) # 현재 작업하고 있는 파일의 경로를 구할 수 있음

import datetime
today = datetime.datetime.now() # 오늘 날짜와 시간을 구하는 모듈
print(today)