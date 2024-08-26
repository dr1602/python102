class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
        
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f'El vehiculo {self.brand}, ha sido vendido.')
        else:
            print(f'El vehiculo {self.brand}, no esta disponible.')
            
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price

    def start_engine(self):
        # levantamos excepcion
        raise NotImplementedError('Este metodo debe ser implementado por la subclase')

    def stop_engine(self):
        # levantamos excepcion
        raise NotImplementedError('Este metodo debe ser implementado por la subclase')
    
class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'El motor del coche {self.model} esta en marcha'
        else:
            return f'El  coche {self.brand} no esta disponible'
            
    def stop_engine(self):
        if not self.is_available:
            return f'El motor del coche {self.model} se ha apagado.'
        else:
            return f'El  coche {self.brand} no esta disponible'
            
class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'La bicicleta {self.model} esta en marcha'
        else:
            return f'La bicicleta {self.brand} no esta disponible'
            
    def stop_engine(self):
        if not self.is_available:
            return f'La bicicleta {self.model} se ha detenido.'
        else:
            return f'La bicicleta {self.brand} no esta disponible'
        
class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'El motor del camion {self.model} esta en marcha'
        else:
            return f'El  camion {self.brand} no esta disponible'
            
    def stop_engine(self):
        if not self.is_available:
            return f'El motor del camion {self.model} se ha apagado.'
        else:
            return f'El  camion {self.brand} no esta disponible'
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []
        
    def buy_car(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f'Lo sient, {vehicle.brand} no esta disponible')
            
    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = 'Disponible'
        else:
            availability = 'No disponible'
        print(f'El estatus del {vehicle.brand} es {availability} y cuesta {vehicle.get_price()}')
        
class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
        
    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f'{vehicle.brand} ha sido agregado al inventario.')
        
    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f'La o el cliente {customer.name} ha sido agregado a la lista de clientes.')
        
    def show_available_vehicles(self):
        print('Los vehiculos disponibles en la tienda son: ')
        for vehicle in inventory:
            if vehicle.check_available():
                print(f'- {vehicle.brand} por {vehicle.get_price()}')
    