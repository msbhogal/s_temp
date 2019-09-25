state = {'users': [],
         'books': [],
         'shelves' : [],
         'reviews' : []}

class Book:
    def __init__(self, user, name, author, genres):
        self.name = name
        self.author = author
        self.genres = genres
        self.user = user
        

class User:
    def __init__(self, name):
        self.name = name

        
        

        
        
