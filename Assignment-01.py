# Take an integer input from the user
n = int(input("Enter a number: "))

# A number less than or equal to 1 is not prime
if n <= 1:
    print("Not Prime")
else:
    # Check for factors from 2 to the square root of n
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    # Output the result
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")


