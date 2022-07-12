import time

t = int(input("Mention the seconds to be counted: "))

for i in range(t):
    print(i+1,"\"Mississippi\"")
    time.sleep(1)

print("Ready or not, here I come!")
