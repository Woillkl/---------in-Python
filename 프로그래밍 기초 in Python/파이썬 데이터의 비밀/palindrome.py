import math
import time

start = time.time()
# My Code #

def is_palindrome(word):
    # 코드를 입력하세요.
    for i in range(len(word)):
        if word[i] == word[len(word)-1-i]:
            boolean = True
            if len(word)-1-i == i or len(word)-1-i <= 0:
                return boolean
        
        else :
            return False
            

# # Good Code #
# def is_palindrome(word):
#     for left in range(len(word) // 2):
#         # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
#         right = len(word) - left - 1
#         if word[left] != word[right]:
#             return False

#     # for문에서 나왔다면 모든 쌍이 일치
#     return True



# 테스트

print(is_palindrome("saippuakivikauppias"))
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

end = time.time()
print(f"{end-start: .5f} sec")