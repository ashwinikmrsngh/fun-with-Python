# First verify that the sides can form a triangle. Then verify if it is a right triangle or not. 
# Find the area of the triangle(Using Heron's Formula).

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2 
    if b > a and b > c:
        return  b ** 2 == a ** 2 + c ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
        
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
 
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
        
a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print("Yes, it can be a triangle.")
else:
    print("No, it can\'t be a triangle.")
    
if is_a_right_triangle(a, b, c):
    print("Yes, it is a right triangle.")
else:
    print("No, it\'s not a right triangle.")

print("The area of the triangle is: ", area_of_triangle(a, b,c))
