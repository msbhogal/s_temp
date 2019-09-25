import pytest

import bookclub


@pytest.fixture
def user(request):
    return bookclub.User("test")

def test_addbook(user):
    assert not bookclub.state['books']
    b = user.add_book("The adventures of Sherlock Holmes",
                      "Arthur Conan Doyle",
                      ['Victorian', 'Mystery'])
    assert b.name == "The adventures of Sherlock Holmes"
    assert b.author == "Arthur Conan Doyle"
    assert b.genres == ['Victorian', 'Mystery']
    assert bookclub.state['books'][0] is b
    
    
    
