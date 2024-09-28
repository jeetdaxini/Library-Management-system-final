import pytest
from library import Library

def test_add_book():
    library = Library()
    library.add_book('978-3-16-148410-0', 'Test Book', 'Author', 2023)
    assert len(library.books) == 1
    assert library.books['978-3-16-148410-0'] ['title'] == 'Test Book'

def test_borrow_book():
    library = Library()
    library.add_book('978-3-16-148410-0', 'Test Book', 'Author', 2023)
    library.borrow_book('978-3-16-148410-0')
    assert library.books['978-3-16-148410-0'] ['borrowed'] is True

def test_return_book():
    library = Library()
    library.add_book('978-3-16-148410-0', 'Test Book', 'Author', 2023)
    library.borrow_book('978-3-16-148410-0')
    library.return_book('978-3-16-148410-0')
    assert library.books['978-3-16-148410-0']['borrowed'] is False


