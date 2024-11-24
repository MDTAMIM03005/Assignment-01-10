# Function to find the second largest number in a list
def second_largest(numbers):
    # Remove duplicates and sort the list in descending order
    unique_numbers = list(set(numbers))

    # Check if there are at least two unique numbers
    if len(unique_numbers) < 2:
        return None  # Return None if there is no second largest number

    unique_numbers.sort(reverse=True)  # Sort in descending order

    # Return the second largest number
    return unique_numbers[1]


# Take input from the user
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Output the second largest number
result = second_largest(numbers)
if result is None:
    print("There is no second largest number.")
else:
    print("The second largest number is:", result)
