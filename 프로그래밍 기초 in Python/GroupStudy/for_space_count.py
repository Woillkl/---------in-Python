from pickletools import read_int4


string = "This is NGL Transportation"

blank_count = 0
for i in range(len(string)-1) :
    print(string[i])
    if string[i] == " " :
        blank_count += 1

print(f"Blank Space : {blank_count}")
