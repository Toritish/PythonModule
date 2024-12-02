# Parent class: Book
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages, Genre: {self.genre}"

    def read(self):
        return f"Reading '{self.title}'..."

# Child class: DigitalBook (inherits from Book)
class DigitalBook(Book):
    def __init__(self, title, author, pages, genre, file_size, format):
        super().__init__(title, author, pages, genre)
        self.file_size = file_size  
        self.format = format  

    def description(self):
        return f"'{self.title}' (Digital) by {self.author}, {self.pages} pages, Genre: {self.genre}, Size: {self.file_size}MB, Format: {self.format}"

    def read(self):
        return f"Opening digital version of '{self.title}' in {self.format} format..."

# Example usage
book = Book("To Kill a Mockingbird", "Harper Lee", 281, "Fiction")
print(book.description())
print(book.read())

digital_book = DigitalBook("1984", "George Orwell", 328, "Dystopian", 2.5, "EPUB")
print(digital_book.description())
print(digital_book.read())