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