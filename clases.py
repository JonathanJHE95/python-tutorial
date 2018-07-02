class myClass():
    def method1(self):
        print('Gemelo')

    def method2(self, someString):
        print('Software testing: ' + someString)

def main():
    # Ejecutando metodos de una clase
    c = myClass()
    c.method1()
    c.method2('Soy un metodo')


if __name__ == '__main__':
    main()

class myClass2():
    def method1(self):
        print('Gemelo')

    def method2(self, someString):
        print('Software testing: ' + someString)


class childClass(myClass2):
    def method1(self):
        myClass.method1(self)
        print('childClass method1')

    def method2(self):
        print('childClass method2')


def main():
    # Ejecutando metodos de una clase
    c2 = childClass()
    c2.method1()
    c2.method2()


if __name__ == '__main__':
    main()


class User:
    name = ''

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print('Bienvenido, ' + self.name)


User1 = User('Jonathan')
User1.sayHello()
