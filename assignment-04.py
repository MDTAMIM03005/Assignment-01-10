# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove any spaces and convert the string to lowercase for consistency
    s = s.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]


# Take input from the user
input_string = input("Enter a string: ")

# Output the result
if is_palindrome(input_string):
    print(True)
else:
    print(False)
