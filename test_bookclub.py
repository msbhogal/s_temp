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
    

def test_get_reviews(user_with_book):
    book = list(user_with_book.books)[0]
    assert len(list(book.reviews)) == 0

    

    
