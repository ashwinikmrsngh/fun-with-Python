# Find the Fibonacci Series for the given first n numbers.

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
num = int(input("Enter a number for Fibonacci Series")) 
for num in range(1, num):
    print(num, "->", fib(num))