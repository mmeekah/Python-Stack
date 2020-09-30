class Book:
    TYPES = ("hardcover", "paperback")


    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, Book.TYPES[0], page_weight +100)   # also return Book(name, Book.TYPES[0], page_weight +100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, Book.TYPES[1], page_weight)       #also return Book(name, Book.TYPES[1], page_weight)

book = Book("Harry Potter", "hardcover", 1500)  #repr

book =  Book.hardcover("Harry Potter", 1500)   #classmethod
light = Book.paperback("Harry Potter", 600)    #classmethod for paperback

print(book.name)
print(book)
print(light)