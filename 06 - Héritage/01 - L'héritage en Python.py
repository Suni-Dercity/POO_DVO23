class Human:

    def __init__(self):
        self.name = ""
        self.first_name = ""
        self.age = 0

    def modify_attribute(self, name, first_name, age):
        self.name = name
        self.first_name = first_name
        self.age = age

    def presentation(self):
        print(f"Herro my name is {self.name} {self.first_name} and I am {self.age} years old~!")

class Student(Human):
    pass

class Teacher(Human):

    def __init__(self):
        self.specialite = []

    pass

Suni = Teacher()
Suni.modify_attribute('Ercity', 'Suni', 21)
Suni.presentation()

Suni.specialite = ['Python', 'Being a Jerk']
print(Suni.specialite)

# On n'a pas eu besoin de redéfinir la méthode modify_attribute ni les attributs d'ailleurs
print(Suni)