import os
print(os.path.abspath('.'))

with open('.new_file.txt', 'w') as f:
    f.write("Hello world!\n")
    f.write("My name is Sean")


