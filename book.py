# A book 
# Constructor (__init__) Method:

class Book:
    current_year = 2025
    def __init__(self, title, author, isbn, publisher, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.year = year

# Adding methods
    def display_info(self):
        """Prints the details of the book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Publisher: {self.publisher}")
        print(f"Year: {self.year}")

    def get_age(self, ):
        """Calculates the age of the book."""
        return self.current_year - self.year
    
    def position_of_the_book(self, on_the_shelf):
        """determine the position of the book."""
        return on_the_shelf 
    
# Create a Book object
my_book = Book("How to code in python", "Sitoworks solutions", "978-0345391803", "inmotion Books", 2021)

# Access attributes
print(my_book.title)

# Call methods
my_book.display_info()
book_age = my_book.get_age()
print(f"The book is {book_age} years old.")
print("the book is on the shelf")
print(Book.current_year)