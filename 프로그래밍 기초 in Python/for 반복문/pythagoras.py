# # Bad Code #
# for a in range(1, 400):
#     for b in range(1, 400):
#         for c in range(1, 400):
#             if a * a + b * b == c * c and a < b < c and a + b + c == 400:
#                 print(a * b * c)
#                 print(f"{a} {b} {c}")
#                 break


# # Good Code # 
# for a in range(1, 400):
#     for b in range(1, 400):
#         c = 400 - a - b
#         if a * a + b * b == c * c and a < b < c:
#             print(a * b * c)


# for a in range(0, 200):
#     for b in range(0, 200):
#         c = 400 - a - b
#         if a < b < c and a ** 2 + b ** 2 == c ** 2 :
#             print(a * b * c)

for b in range(1, 400) :
    for a in range(1, 200) :
        if b < a :
            break
        c = 400 - a - b
        # if a < b < c and a ** 2 + b ** 2 == c ** 2 : -> a < b는 필요가 없다. 왜냐하면 위에 벌써 b < a 조건을 달아줬기 때문에
        if b < c and a ** 2 + b ** 2 == c ** 2 :
            print(a * b * c)
            break