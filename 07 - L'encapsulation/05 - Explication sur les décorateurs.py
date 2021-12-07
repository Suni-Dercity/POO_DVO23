# Un décorateur c'est une fonction qui permet de modifier le comportement d'autres fonctions
# c'est utile quand on veut ajouter un même code à plusieurs fonction
# ça sera très utile dans le cradre de contrôle commun

user = 'Sam'
def my_decorator(function):

    def control():
        print('Access denied')

    if user!= 'Sam':
        return control

    return function

@my_decorator
def function1():
    print('Execution of the task n°1')

# si le user c'est Sam
# alors Execution of the task n°1
function1()

function1.__dict__