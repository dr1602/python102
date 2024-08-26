# como crear una persona

class Person:
    #constructor es una funcion especial de las clases para definir los atributos
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)
        
    def greet(self):
        print(f'Hola, mi nombre es {self.name} y tengo {self.age}')

person1 = Person('Ana', 30)
person2 = Person('Ricardo', 21)

person1.greet()
person2.greet()

# como crear una cuenta bancaria

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
        
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f'Se ha depositado {amount}. El saldo actual es: {self.balance}')
        else:
            print('La cuenta no esta activia, no se puede depositar.')
            
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f'Se ha retirado {amount}. El saldo actual es: {self.balance}')
            else:
                print('Saldo insuficiente, no se puede retirar esa cantidad.')
        else:
            print('La cuenta no esta activa, no se puede retirar.')
            
    def deactivate(self):
        self.is_active = False
        print(f'La cuenta de {self.account_holder} ha sido desactivada')
        
    def activate(self):
        self.is_active = True
        print(f'La cuenta de {self.account_holder} ha sido activada')

account1 = BankAccount('Ana', 500)
account2 = BankAccount('Luis', 1200)

# Llamando a los metodos

account1.deposit(2000)
account2.deposit(500)
account1.deactivate()
account1.withdraw(300)
account1.activate()
account1.withdraw(30000)

#en python todo es una clase            