
#Some libraries
from asyncio.windows_events import NULL
import json


#Book ini

class Book:
    def __init__(self, title, author, price):
        
        self.title = title
        self.author = author
        self.price = price
        if price < 0:
            raise ValueError("Why we have negaitve price on:", self.title,"?" )
    
    def to_json(self):
        return {
            'title': self.title,
            'author': self.author,
            'price': self.price
        }

    def __str__(self):
        return f"{self.title} by {self.author} for {self.price}"
    



#Store ini

class BookStore:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def get_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def get_books_by_author(self, author):
        books_by_author = []
        for book in self.books:
            if book.author == author:
                books_by_author.append(book)
        return books_by_author

    def get_total_price(self):
        total_price = 0
        for book in self.books:
            total_price += book.price
        return total_price



#Book add

try:
    book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 111)
except ValueError as e:
    print(str(e))
    print("You can't pay for sellins YOUR item \n")

try:
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 222)
except ValueError as e:
    print(str(e))
    print("You can't pay for sellins YOUR item \n")


try:
    book3 = Book("1984", "George Orwell", -333)
except ValueError as e:
    print(str(e))
    print("You can't pay for sellins YOUR item \n")

try:
    book3 = Book("1984", "George Orwell", 333)
except ValueError as e:
    print(str(e))
    print("You can't pay for sellins YOUR item \n")




#Store add
 
bookstore = BookStore("My Bookstore")




#Put your book in me store

bookstore.add_book(book1)
bookstore.add_book(book2)
bookstore.add_book(book2)
bookstore.add_book(book3)




#What books we have?

print("All books in the bookstore:")
for book in bookstore.books:
    print(book)    
print("")




#Book delete

bookstore.remove_book(book2)




#What books we have now?

print("All books in the bookstore:")
for book in bookstore.books:
    print(book)    
print("\n")




#What books we have, but by J.K.R?

print("Books by J.K. Rowling:")
books_by_rowling = bookstore.get_books_by_author("J.K. Rowling")
for book in books_by_rowling:
    print(book)
print("\n")




#What is prise of books we have?

total_price = bookstore.get_total_price()
print(f"Total price of all books in the bookstore: {total_price}\n")





#Hey out1.json, do you wanna know what books we have?

with open('out1.json', 'w', encoding='utf-8') as out_file:
    books_js = []
    for book in bookstore.books:
        books_js.append(book.to_json())

    json.dump(books_js, out_file)

