# First 50 Prime numbers.

def is_prime(num):
    for i in range(2,num):
        if num % i != 0:
            return True
        else:
            return False
    if num == 2:
        return True
for i in range(1, 50):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
