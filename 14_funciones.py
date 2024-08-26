def greet(name, last_name='No tiene apellido'):
    print('Hola', name, last_name)
    
greet('Dave', "Mesteem")
greet('my friend')

greet(last_name = 'Florida', name = 'Carli')

# funcion calculadora

def add(a, b):
    return a + b

def substrac(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculadora():
    while True:
        print('Seleccione una operacion')
        print('1 Suma')
        print('2 Resta')
        print('3 Multiplicacion')
        print('4 Division')
        print('5 Salir')
        
        option = int(input('Ingresa el numero de la operacion deseada (1, 2, 3, 4, 5): '))
        
        if option == 5:
            print('Saliendo de la calculadora')
            break
        
        if option in [1, 2, 3, 4]:
            num1 = float(input('Ingrese el primer numero:'))
            num2 = float(input('Ingrese el segundo numero:'))
            
            if option == int(1):
                print('La suma es:', add(num1, num2))
            elif option == int(2):
                print('La resta es:', substrac(num1, num2))
            elif option == int(3):
                print('La multiplicacion es:', multiply(num1, num2))
            elif option == int(4):
                print('La division es:', divide(num1, num2))
        else:
            print('Opcion no valida, por favor intenta de nuevo.')
                
calculadora()  