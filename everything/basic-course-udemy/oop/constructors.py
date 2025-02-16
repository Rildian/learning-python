from datetime import datetime
# now it's more intuitive after taking oop :p

class Funcionario:  # self is basically using every paramenter of this object
    def __init__(self, name, date): # this is a constructor btwcd learning-python
        self.name = name
        self.date = date

    def age_employer(self):
        self.age = int(datetime.now().year - self.date)
        return self.age

    def show_infos(self):
        print(f"Name is {self.name}, {self.age_employer()} years old and i was born in {self.date}")

    def double_age(self):
        return (self.age_employer())*2


user = Funcionario(name='Roberto', date=2003)

print(user.name)

print(user.show_infos()) # dont forget to use .nameMethod() to call the method and executes
print(Funcionario.age_employer(user)) # the same thing above
print(user.double_age()) # same thing here
