state = {'users': [],
         'books': [],
         'shelves' : [],
         'reviews' : []}

class Book:
    def __init__(self, user, name, author, genres):
        self.name = name
        self.author = author
        self.genres = genres
        self.added_by = user

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
        
        
        
        
        
    

