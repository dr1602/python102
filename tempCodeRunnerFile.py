class Car:
    def __init__(self, name, model, price):
        self.name = str(name)
        self.model = int(model)
        self.price = int(price)
        self.business_owned = True
        self.person_owned = False

    def sold_by_business(self, budget):
        if self.business_owned:
            if self.price <= budget:
                self.business_owned = False
                self.person_owned = True
                print(f'El carro {self.name} fue vendido por el negocio')
            else:
                print(f'El carro {self.name} no puede ser vendido a la persona por falta de presupuesto')
        else:
            print(f'El carro {self.name} no puede ser vendido ya que no se encuentra disponible en el negocio.')

    def sold_by_person(self, budget):
        if self.person_owned:
            if self.price <= budget:
                self.person_owned = False
                self.business_owned = True
                print(f'El carro {self.name} fue vendido por la persona')
            else:
                print(f'El carro {self.name} no puede ser comprado por el negocio por falta de presupuesto')
        else:
            print(f'El carro {self.name} no puede ser vendido ya que la persona no cuenta con el carro.')

class Person:
    def __init__(self, name, budget):
        self.name = str(name)
        self.budget = int(budget)
        self.owned_cars = []

    def buy_car(self, car):
        if car.business_owned:
            if car.price <= self.budget:
                car.sold_by_business(self.budget)  # Pasa el presupuesto de la persona
                self.owned_cars.append(car)
                self.budget -= car.price
                print(f'Usted ha comprado el carro {car.name}, por {car.price}. Ahora su presupuesto disponible es: {self.budget}')
            else:
                print(f'Usted no puede comprar el carro {car.name}, le faltan {car.price - self.budget}.')
        else:
            print(f'El carro {car.name} no está a la venta en el negocio')

    def sell_car(self, car, business):
        if car.person_owned:
            if car.price <= business.budget:
                car.sold_by_person(business.budget)  # Pasa el presupuesto del negocio
                self.owned_cars.remove(car)
                self.budget += car.price
                business.budget -= car.price
                print(f'Usted ha vendido el carro {car.name}, por {car.price}. Ahora su presupuesto disponible es: {self.budget}')
            else:
                print(f'El negocio no tiene suficiente dinero para comprar el carro {car.name}.')
        else:
            print(f'Usted no tiene el carro {car.name} por lo que no lo puede vender')

class Business:
    def __init__(self, name, budget):
        self.name = str(name)
        self.budget = int(budget)
        self.owned_cars = []

    def buy_car(self, car, person):
        if car.person_owned:
            if car.price <= self.budget:
                car.sold_by_person(self.budget)  # Pasa el presupuesto del negocio
                self.owned_cars.append(car)
                self.budget -= car.price
                person.budget += car.price
                print(f'El negocio ha comprado el carro {car.name}, por {car.price}. Ahora su presupuesto disponible es: {self.budget}')
            else:
                print(f'El negocio no puede comprar el carro {car.name}, le faltan {car.price - self.budget}.')
        else:
            print(f'El carro {car.name} no está a la venta por la persona')

    def sell_car(self, car, person):
        if car.business_owned:
            if car.price <= person.budget:
                car.sold_by_business(person.budget)  # Pasa el presupuesto de la persona
                self.owned_cars.remove(car)
                self.budget += car.price
                person.budget -= car.price
                print(f'El negocio ha vendido el carro {car.name}, por {car.price}. Ahora su presupuesto disponible es: {self.budget}')
            else:
                print(f'La persona no tiene suficiente dinero para comprar el carro {car.name}.')
        else:
            print(f'El negocio no tiene el carro {car.name} por lo que no lo puede vender')

# Crear autos
car1 = Car('Toyota', 2020, 10000)
car2 = Car('Honda', 2021, 12000)

# Crear persona y negocio
person1 = Person('Carlos', 15000)
business = Business('AutoDealer', 50000)

# El negocio vende el carro a la persona
person1.buy_car(car1)

# La persona vende el carro de vuelta al negocio
person1.sell_car(car1, business)
