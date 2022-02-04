list_tri = [
    [10, 11, 12],
    [20, 21, 22],
    [5,1,16]
    ]   


for x in range(0,len(list_tri[0])) :
    first = list_tri[0][x]
    for y in range(0, len(list_tri[1])) :
        second = list_tri[1][y]
        for z in range(0, len(list_tri[2])) :
            third = list_tri[2][z]
            if thr_add(first, second, third) :
                print(f"50이 넘는 값을 만들어 내는 세 수는 : {first}, {second}, {third} 입니다.")