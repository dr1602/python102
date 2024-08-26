# concesionaria (compra, venta), vehiculos (disponibles, precio), usuarios(comprar, vender, carro, saldo)
class Car:
    def __init__(self, name, model, price):
        self.name = str(name)
        self.model = int(model)
        self.price = int(price)
        self.business_owned = True
        self.person_owned = False
    
    def sold_by_business(self, budget):
        if self.business_owned:
            if self.price >= budget:
                self.business_owned = False
                self.person_owned = True
                print(f'El carro {self.name}, fue vendido por por el negocio')
            else:
                print(f'El carro {self.name}, no puede ser vendido a la persona por falta de presupuesto')
        else:
            print(f'El carro {self.name}, no puede ser vendido ya que no se encuentra disponible en el negocio.')
    
    def sold_by_person(self, budget):
        if self.person_owned:
            if self.price >= budget:
                self.person_owned = False
                self.business_owned = True
                print(f'El carro {self.name}, fue vendido por la persona')
            else:
                print(f'El carro {self.name}, no puede ser comprado por el negocio falta de presupuesto')
        else:
            print(f'El carro {self.name}, no puede ser vendido ya que la persona no cuenta con el carro.')
        
class Person:
    def __init__( self, name, budget ):
        self.name = str(name)
        self.budget = int(budget)
        self.owned_cars = []
        
    def buy_car(self, car):
        if car.business_owned:
            if car.price <= self.budget:         
                car.sold_by_business()
                self.owned_cars.append(car)
                self.budget -= car.price
                print(f'Usted ha comprado el carro {car.name}, por {car.price}. Ahora su presupuesto disponible es: {self.budget}')
            else:
                print(f'Usted no puede comprar el carro {car.name}, le faltan {car.price - self.budget}.')
        else:
            print(f'El carro {car.name} no esta a la venta en el negocio')
    
    def sell_car(self, car, business ):
        if car.person_owned:
            if car.price <= business.budget:         
                car.sold_by_person()
                self.owned_cars.remove(car)
                self.budget += car.price
                business.budget -= car.price
                print(f'Usted ha vendido el carro {car.name}, por {car.price}. Ahora su presupuesto disponible es: {self.budget}')
            else:
                print(f'Usted no puede vender el carro {car.name}, el negocio no tiene suficiente dinero para comprar.')
        else:
            print(f'Usted no tiene el carro {car.name} por lo que no lo puede vender')
            
class Business:
    def __init__( self, name, budget ):
        self.name = str(name)
        self.budget = int(budget)
        self.owned_cars = []
        
    def buy_car(self, car, person):
        if car.person_owned:
            if car.price <= business.budget:         
                car.sold_by_person()
                self.owned_cars.append(car)
                self.budget -= car.price
                person.budget += car.price
                print(f'Usted ha comprado el carro {car.name}, por {car.price}. Ahora su presupuesto disponible es: {self.budget}')
            else:
                print(f'Usted no puede comprar el carro {car.name}, le faltan {car.price - self.budget}.')
        else:
            print(f'El carro {car.name} no esta a la venta por la persona')
        
    def sell_car(self, car, person ):
        if car.business_owned:
            if car.price <= person.budget:         
                car.sold_by_business()
                self.owned_cars.remove(car)
                self.budget += car.price
                person.budget -= car.price
                print(f'Usted ha vendido el carro {car.name}, por {car.price}. Ahora su presupuesto disponible es: {self.budget}')
            else:
                print(f'Usted no puede vender el carro {car.name}, la persona no tiene suficiente dinero para comprar.')
        else:
            print(f'Usted no tiene el carro {car.name} por lo que no lo puede vender')
                
# Create cars
car1 = Car('Toyota', 2020, 10000)
car2 = Car('Honda', 2021, 12000)

# Create person and business
person1 = Person('Carlos', 15000)
business = Business('AutoDealer', 50000)

# Business sells car to person
person1.buy_car(car1)

# Person sells car back to business
person1.sell_car(car1, business)
