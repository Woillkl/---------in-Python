# 모듈 사용법

# area 모듈 안의 있는 모든 함수를 가지고 온다.
import area

print(area.PI) # 모듈로 모듈 안의 변수도 가지고 올 수 있다.
print(area.circle(2))
print(area.square(4))

# 어떠한 모듈 안의 특정 함수만을 가지고 온다.
from area import circle

print(circle(2))

# 어떠한 모듈 안의 여러개의 함수를 가지고 온다.
from area import circle, square

print(circle(2))
print(square(4))

# area 모듈을 새로운 이름을 지어준다.
import area as ar

print(ar.circle(2))

# 어떠한 모듈에서 특정한 함수를 가지고 오고 그 함수를 다른 이름으로 설정해준다.
from area import square as sq
print(sq(4))

# 모듈에 있는 모든 내용을 가지고 온다.
# 이 방식을 사용하면 어떤 함수가 어떤 모듈에서 왔는지를 알 수 없기 때문에 권장하지 않는다.
from area import *

print(square(3))
print(circle(2))
print(PI)