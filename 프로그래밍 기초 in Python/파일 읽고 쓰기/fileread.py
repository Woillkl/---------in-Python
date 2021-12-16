# 같은 폴더에 chicken.txt가 있기 때문에 읽을 수 있음 
# 다른 폴더에 있으면 ?/chicken.txt를 써야함

# with open('chicken.txt', 'r', encoding='UTF-8') as f:
#     # 이렇게 코드를 치게 되면 filenotFound Error가 나타나게 됌
#     # 해결 방법은 getcwd(Current Work Directory)를 확인하여 그 경로에서 부터 지정해 줘야함
#     print(type(f))

import os
print(os.getcwd()) # K:\Python Group Study 경로가 나타내게 됌. 절대 경로가 이렇게 지정이 되어 있으니 뒤의 directory부터 적어줘야 결과 값이 나옴

with open('프로그래밍 기초 in Python\\파일 읽고 쓰기\\chicken.txt', 'r', encoding='UTF-8') as f:
    # \를 두번 써주는 이유는 Escape Code \하나만 쓰게되면 Escape Code로 작동을 하기 때문에 \를 읽지 못하기 때문에 2번 작성해 줘야 함
    print(type(f))

# 상대 경로는 "내가 작업하는 위치를 기준"으로 경로가 결정된다.
# 절대 경로는 "내가 작업하는 위치와 상관없이" 절대로 변하지 않는 경로이다.

with open('프로그래밍 기초 in Python\\파일 읽고 쓰기\\chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f: 
        # print(line) # 모든 줄이 출력 되게 된다. 한줄 씩 뛰어 나오는 이유는 엔터가 \n의 역활을 하기 때문
        print(line.strip()) # strip 함수는 맨 앞과 맨 뒤에 있는 화이트 스페이스를 지워주는 역활을 한다. 이때문에 \n이 사라진다.
        
a = []
with open('프로그래밍 기초 in Python\\파일 읽고 쓰기\\chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        a.append(line.strip().split(": ")) # split은 나온 값을 ()안에 들어간 기준으로 잘라서 출력시킨다.
print(a)