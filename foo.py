import collections.abc

class Book:
    def __init__(self, name):
        self.name = name


class Shelf(collections.abc.MutableSequence):
    def __init__(self, name):
        self.books = []
    
    def __getitem__(self, name):
        for i in self.books:
            if i.name == name:
                return b
        raise KeyError("{} not found".format(name))

    def __setitem__(self, name, book):
        pass

    def __delitem__(self, book):
        self.books.remove(book)
            
    def __len__(self):
        return len(self.books)
    
    def insert(self, idx, book):
        self.books.append(book)
    
    def __iter__(self):
        return iter(self.books)

