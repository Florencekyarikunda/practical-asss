class Dog:
    def __init__(self,gender,color,age):
        self.gender=gender
        self.color=color
        self.age=age

    def bark(self):
        return f'Dog is barking'

    def eat(self):
        return f'Its eating'