class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, year):
        book = {'isbn': isbn, 'title': title, 'author': author, 'year': year}
        self.books[isbn] = book
