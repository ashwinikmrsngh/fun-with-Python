# Find the factorial of the number.

def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
num = int(input("Enter a number: "))
print("The value of", num, "! is: ", factorial(num))