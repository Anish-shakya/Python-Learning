class person:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname=lastname
        self.age = age

    def greet(self):
        print(f'Hello, My name is {self.firstname} {self.lastname} and I am {self.age} years old')

person1 = person('James','Burce',20)
person1.greet()