# # 사전 (dictionary)
# # key-value pair(키와-값 쌍)
# my_dictionary = {
#     5: 25,
#     2: 4,
#     3: 9    
# }
# # print(type(my_dictionary)) # <class 'dict'>

# # print(my_dictionary[3]) # 9
# my_dictionary[9] = 81
# print(my_dictionary)

my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸'  : '이지영'
}
# print(my_family['아빠']) # 이석진
# print(my_family.values()) # dict_values(['김자옥', '이석진', '이동민', '이지영'])

# print('이지영' in my_family.values()) # True
# print('신우일' in my_family.values()) # False

# for value in my_family.values() :
#     print(value)

# for key in my_family.keys():
#     value = my_family[key]
#     print(key, value)

for key, value in my_family.items():
    print(f"{key} : {value}")