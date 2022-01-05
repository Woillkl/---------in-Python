while True:
    user_input = int(input("Type the number:"))
    if user_input == 0:
        print("Hello")
        user_input += 1
    elif user_input > 0:
        print("World")
    
    for i in range(3):
        print("Hello World")