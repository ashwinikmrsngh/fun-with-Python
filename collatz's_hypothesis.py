c0 = int(input("Enter a Natural Number: "))
if c0 <= 0:
    c0 = int(input("Enter a Natural Number: "))
    
step = 0

while c0 != 1 :
    
    if c0 % 2 == 0 :
        c0 = c0 / 2
    else :
        c0 = 3 * c0 + 1
    
    step += 1
    print(int(c0))

print("Steps: ", step)