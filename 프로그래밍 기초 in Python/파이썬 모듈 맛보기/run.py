# import calculator # 같은 폴더에 있는 calculator.py를 사용한다는 뜻

# print(calculator.add(3, 7))
# print(calculator.multiply(3, 4))

# import calculator as calc # as 뒤의 뜻은 매번 calculator를 쓰는 대신 calc를 쓴다는 뜻

# print(calc.add(3, 7))
# print(calc.multiply(3, 4))

# from calculator import add, multiply # 이 뜻은 calculator의 모듈 안에서 add와 multiply 함수만 가지고 온다는 뜻

# print(add(3, 7))
# print(multiply(3, 4))

from calculator import * # 이 뜻은 claculator 모듈에서 * 즉 모든 함수를 가지고 오겠다는 뜻
# 하지만 권장하지 않음 왜냐하면 함수들의 출처가 불분명 해지기 때문