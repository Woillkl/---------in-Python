# 사용자의 값을 입력받기 위한 함수 input
name = input("이름을 입력하세요 : ")
print(name)

# # input 함수를 사용할때의 주의 사항
# x = input("숫자를 입력하세요 : ")
# print(x + 5) # x 는 숫자를 입력한다고 하여도 문자열로 받아들인다.

# 올바른 코드
x = int(input("숫자를 입력하세요 : "))
print(x + 5)