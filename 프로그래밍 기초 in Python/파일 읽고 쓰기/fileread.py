# 같은 폴더에 chicken.txt가 있기 때문에 읽을 수 있음 
# 다른 폴더에 있으면 ?/chicken.txt를 써야함
with open('chicken.txt', 'r') as f: 
    print(type(f))


