import os
from typing import final

# os.chdir('K:\\Python Group Study\\프로그래밍 기초 in Python\\파일 읽고 쓰기') # 절대 경로를 이 프로그래밍이 실행 된 후 바꿔준다. 프로그램이 끝나면 원상복구 됌

# 절대 경로를 이 프로그래밍이 실행 된 후 바꿔준다. 프로그램이 끝나면 원상복구 됌
os.chdir("프로그래밍 기초 in Python\\파일 읽고 쓰기")


def register():
    while True:
        email = []
        try:
            user_email = input("Please register your email. :  ")
            f = open("user_info.txt", "r", encoding="UTF-8")
        except FileNotFoundError:
            f = open("user_info.txt", "w", encoding="UTF-8")
        finally:
            for line in f:
                email.append(line.strip())
            if user_email in email:
                print(
                    "User Email already exists. Please register with different email."
                )
            else:
                f = open("user_info.txt", "a", encoding="UTF-8")
            f.write(f"{user_email}\n")
            print("Successfully registered.")
            break

        # user_email = input("Please register your email. :  ");

        # f = open('user_info.txt', 'r', encoding='UTF-8')
        # for line in f :
        #     email.append(line.strip())

        # if user_email in email :
        #     print("User Email already exists. Please register with different email.")
        # else :
        #     f = open('user_info.txt', 'a', encoding='UTF-8')
        #     f.write(f"{user_email}\n")
        #     print("Successfully registered.")
        #     break


while True:

    choose = input("Please choose your option. 1:Register 2:Login")

    if choose == "1":
        register()

    elif choose == "2":
        while True:
            email = []
            user_email = input("Log in :  ")

            f = open("user_info.txt", "r", encoding="UTF-8")
            for line in f:
                email.append(line.strip())

            if user_email in email:
                print("Successfully Logined in")
                print("Welcome")
                break

            else:
                print("User Email doesn't exists. Please register your email.")
                register()
