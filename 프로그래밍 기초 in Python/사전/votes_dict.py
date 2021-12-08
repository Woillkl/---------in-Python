# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# My Code #
# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
kim, kang, choi = 0, 0, 0
for name in votes:
    # 코드를 작성하세요.
    if name == '김영자':
        kim += 1
        vote_counter[name] = kim
    elif name == '강승기':
        kang += 1
        vote_counter[name] = kang
    elif name == '최만수':
        choi += 1
        vote_counter[name] = choi

# 후보별 득표수 출력
print(vote_counter)

# Good Code #
# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    if name not in vote_counter:
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1

print(vote_counter)
