# Function to find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    # Use the Euclidean algorithm to find the GCD
    while b != 0:
        a, b = b, a % b
    return a

# Take input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Output the GCD
print("The GCD of", a, "and", b, "is:", gcd(a, b))
