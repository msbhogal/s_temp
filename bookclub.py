state = {'users': [],
         'books': [],
         'shelves' : [],
         'reviews' : []}

class DuplicateReview(Exception):
    pass

class Shelf:
    def __init__(self, user, name):
        self.name = name
        self.owner = user
        self.__books = []

    @property
    def books(self):
        for i in self.__books:
            yield i
        
    def add_book(self, book):
        self.__books.append(book)
    
    def remove_book(self, book_name):
        found = None
        for idx, i in enumerate(self.books):
            if i.name == book_name:
                found = idx
        if found != None:
            self.__books.pop(found)
        else:
            raise KeyError("Book not found")

        
        

class Review:
    def __init__(self, book, user, text):
        self.book = book
        self.user = user
        self.text = text
    

class Book:
    def __init__(self, user, name, author, genres):
        self.name = name
        self.author = author
        self.genres = genres
        self.added_by = user

    @property
    def reviews(self):
        for i in state['reviews']:
            if i.book == self:
                yield i

    def add_review(self, user, text):
        for i in self.reviews:
            if i.user == user:
                raise DuplicateReview("{} has already added a review".format(user.name))
        review = Review(self, user, text)
        state['reviews'].append(review)


class User:
    def __init__(self, name):
        self.name = name
        self.__books = []
    
    def add_book(self, name, author, genre):
        b = Book(self, name, author, genre)
        state['books'].append(b)
        return b

    def delete_book(self, book_name):
        found = None
        for idx, i in enumerate(state['books']):
            if i.added_by == self and i.name == book_name:
                found = idx
        if found != None:
            state['books'].pop(found)
        else:
            raise KeyError("Book not found")
        
    @property
    def books(self):
        for i in state['books']:
            if i.added_by == self:
                yield i

    def add_shelf(self, name):
        s = Shelf(self, name)
        state['shelves'].append(s)
        return s

    @property
    def shelves(self):
        for i in state['shelves']:
            if i.owner == self:
                yield i

    def get_shelf(self, name):
        for i in state['shelves']:
            if i.owner == self and i.name == name:
                return i

    def delete_shelf(self, name):
        found = None
        for idx, i in enumerate(state['shelves']):
            if i.owner == self and i.name == name:
                found = idx
        if found != None:
            state['shelves'].pop(found)
        else:
            raise KeyError("Shelf not found")


        
        
        
        
        
        
        
    

