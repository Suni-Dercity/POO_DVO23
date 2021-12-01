# Le polymorphisme c'est :
# - le fait de créer des méthodes différentes pour des classes qui héritent l'une de l'autre (Overriding)
# - le fait de définir plusieurs fois la même méthode avec des arguments différents (overloading) (plus utilisé dans des langages comme ptn de JAVA)

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

    def work(self,work = 'need define'):
        print(f"Hi I am currently doing {work}")
class Student(Human):
    pass

    def work(self,work= "homework"):
        print(f'Override of the method work in the Student class')
        print(f'Hi I am currently doing {work}')

class Teacher(Human):

    def __init__(self):
        self.specialite = []

Student1 = Student()
Student1.work()

Teacher1 = Teacher()
Teacher1.work("correcting some of your dumbasses WORK")