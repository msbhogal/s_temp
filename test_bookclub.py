import pytest

import bookclub


@pytest.fixture
def user(request):
    return bookclub.User("test")


@pytest.fixture
def user_with_book(request):
    u = bookclub.User("test")
    u.add_book("Testing title", "Testing author", ['test_genre1', 'test_genre2'])
    return u

@pytest.fixture
def book(user_with_book):
    return next(user_with_book.books)

def test_addbook(user):
    assert not bookclub.state['books']
    b = user.add_book("The adventures of Sherlock Holmes",
                      "Arthur Conan Doyle",
                      ['Victorian', 'Mystery'])
    assert b.added_by == user
    assert b.name == "The adventures of Sherlock Holmes"
    assert b.author == "Arthur Conan Doyle"
    assert b.genres == ['Victorian', 'Mystery']
    assert bookclub.state['books'][0] is b
    
def test_listbooks(user_with_book):
    assert len(list(user_with_book.books)) == 1
    

def test_deletebooks(user_with_book):
    assert len(list(user_with_book.books)) == 1
    user_with_book.delete_book("Testing title") #UNSURE
    assert len(list(user_with_book.books)) == 0
    

def test_get_reviews(book):
    assert len(list(book.reviews)) == 0

def test_add_review(book, user):
    book.add_review(user, "Great book")
    review = list(book.reviews)[0]
    assert review.user == user
    assert review.book == book
    assert review.text == "Great book"

def test_add_repeat_review(book, user):
    book.add_review(user, "Great book")
    with pytest.raises(bookclub.DuplicateReview):
        book.add_review(user, "some other text here")

def test_add_shelf(user):
    assert len(list(bookclub.state['shelves'])) == 0
    s = user.add_shelf("SciFi")
    assert len(list(bookclub.state['shelves'])) == 1
    assert bookclub.state['shelves'][0] == s
    bookclub.state['shelves'].pop()
    
def test_delete_shelf(user):
    assert len(list(bookclub.state['shelves'])) == 0
    s = user.add_shelf("SciFi")
    assert len(list(bookclub.state['shelves'])) == 1
    user.delete_shelf("SciFi")
    assert len(list(bookclub.state['shelves'])) == 0
    
def test_add_book_to_shelf(user, book):
    s = user.add_shelf("SciFi")
    assert len(list(s.books)) == 0
    s.add_book(book)
    assert len(list(s.books)) == 1

def test_add_book_to_shelf(user, book):
    s = user.add_shelf("SciFi")
    assert len(list(s.books)) == 0
    s.add_book(book)
    assert len(list(s.books)) == 1
    s.remove_book(book.name)
    assert len(list(s.books)) == 0

    
    

    
