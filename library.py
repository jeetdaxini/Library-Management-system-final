class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, year):
        book = {'isbn': isbn, 'title': title, 'author': author, 'year': year, 'borrowed': False}
        self.books[isbn] = book

    def borrow_book(self, isbn):
        if self.books[isbn]['borrowed']:
            raise ValueError("Book is already borrowed.")
        self.books[isbn]['borrowed'] = True
