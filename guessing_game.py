secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

n = int(input("Guess the number: "))

while (n != secret_number):
    print("Ha ha! You're stuck in my loop!")
    n = int(input("Guess the number: "))

print(n, "Well done, muggle! You are free now.")
