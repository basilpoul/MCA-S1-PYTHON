class publisher():
    def __init__(self, name):
        self.name = name
    
    def details(self):
        print(f"Publisher name: {self.name}")

class book(publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author
    
    def details(self):
        super().details()  
        print(f"Book title: {self.title}")
        print(f"Author: {self.author}")

class python(book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages
    
    def details(self):
        super().details()  
        print(f"Price: {self.price}")
        print(f"Pages: {self.pages}")

book1 = python("ABC books", "Wings of Fire", "Subi", "100", "250")
book1.details()  
