alphabet_string = "ABCDEFGHIJ"

print(alphabet_string[0]) # A
print(alphabet_string[1]) # B
print(alphabet_string[2]) # C
print(alphabet_string[-1]) # J

print(alphabet_string[0:5]) # A, B, C, D, E
print(alphabet_string[4:]) # E, F, G, H, I, J
print(alphabet_string[:4]) # A, B, C, D

# 문자열은 추가는 가능하지만 수정은 안된다.
# 가능한 것 #
hello = "Hello" + "World"

# 불가능 한 것 #
# helloworld = "Hello World"
# helloworld[1] = "E"

