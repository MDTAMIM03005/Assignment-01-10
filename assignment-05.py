# Take input from the user
s = input("Enter a string: ")

# Define the vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Initialize a variable to store the count of vowels
vowel_count = 0

# Loop through each character in the string
for char in s:
    # If the character is a vowel, increment the count
    if char in vowels:
        vowel_count += 1

# Output the number of vowels
print("Number of vowels:", vowel_count)
