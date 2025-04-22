class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    
    def bark(self):
        print('Whoof Whoof!!')
 
 
class owner:
    def __init__(self,name,address,contact_number):
        self.name = name
        self.address =address
        self.contact_number = contact_number

owner1 = owner('ABC','Nepal','123456789')
owner2 = owner('CDE','USA','987654321')
            
dog1 = Dog('Bruno','Scottish Terrier',owner1)
print(f'Dog Owner : {dog1.owner.name} | Owner Address : {dog1.owner.address} | Owner Contact : {dog1.owner.contact_number}')
print(f'Dog Name : {dog1.name} | Dog Breed : {dog1.breed}')
dog1.bark()


dog2 = Dog('Freya','Greyhound',owner2)
print(f'Dog Owner : {dog2.owner.name} | Owner Address : {dog2.owner.address} | Owner Contact : {dog2.owner.contact_number}')
print(f'Dog Name : {dog2.name} | Dog Breed : {dog2.breed}')
dog2.bark()