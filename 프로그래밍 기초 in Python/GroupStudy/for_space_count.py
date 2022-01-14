string = "This is NGL Transportation"
print(string[0])
print(string[1])

blank_count = 0
for i in range(len(string)-1) :
    print(string[i])
    if string[i] == " " :
        blank_count += 1

print(f"Blank Space : {blank_count}")
