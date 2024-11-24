# Define the Book class
class Book:
    # The __init__ method initializes the book with title, author, and number of pages
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # The get_description method returns a description of the book in the required format
    def get_description(self):
        return f'"{self.title}" by {self.author}, page: {self.pages}'

# Sample input: Creating an instance of the Book class
book1 = Book("1984", "George Orwell", 328)

# Output: Calling the get_description method to print the description
print(book1.get_description())
