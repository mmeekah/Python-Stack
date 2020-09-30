# class Bookshelf:      ----------------------------------> Inheritence
#     def __init__(self, quantity):
#         self.quantity= quantity



#     def __str__(self):
#         return f"Bookshelf with {self.quantity} books."


# shelf = Bookshelf(300)



# class Book(Bookshelf):
#     def __init__(self, name, quantity):
#         super().__init__(quantity)
#         self.name=name

    
#     def __str__(self):
#         return f"Book{self.name}"


# book = Book(" Harry Potter", 120)
# print(book)


class Bookshelf:
    def __init__(self, *books):
        self.books= books


    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."



class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"



book1 = Book("Harry Potter")
book2 = Book("Python")
shelf = Bookshelf(book1, book2)

print(shelf)


