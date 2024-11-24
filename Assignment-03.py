# Take a string input from the user
s = input("Enter a string: ")

# Initialize a variable to count the digits
digit_count = 0

# Loop through each character in the string and check if it's a digit
for char in s:
    if char.isdigit():
        digit_count += 1

# Output the number of digits
print("Number of digits:", digit_count)
