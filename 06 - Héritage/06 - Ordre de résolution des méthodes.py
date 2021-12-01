class A:
    def m1(self):
        print('La méthode m1 de la classe A')

class B(A):
    def m1(self):
        print('La méthode m1 de la classe B')

class C(A):
    def m1(self):
        print('La méthode m1 de la classe C')

class D(B, C):
    # si je supprime la méthode m1
    # la méthode sera appelée dans la classe B
    pass

# La MRO en Python
my_class = D()
my_class.m1()

print(D.mro())