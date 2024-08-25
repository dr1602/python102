# noracion de diccionarios

numbers = {
    1: 'uno',
    2: 'dos',
    3: 'tres',
}

print(numbers)

# referencia a la llave para extraer informacion

print(numbers[2])

information ={
    'nombre': 'Carla',
    'apellido': 'Florida',
    'altura': 1.60,
    'edad': 29,
}

print(information)

del information['edad']
print(information)

# metodos propios de los diccionarios

claves = information.keys()
print(claves)
print(type(claves))

values = information.values()
print(values)
print(type(values))

pairs = information.items()
print(pairs)
print(type(pairs))

contacts ={
    'Persona_1':{
        'Nombre': 'Carla',
        'Apellido': 'Florida',
        'Altura': 1.60,
        'Edad': 29,
    },
    'Persona_2':{
        'Nombre': 'Diego',
        'Apellido': 'Antezana',
        'Altura': 1.81,
        'Edad': 32,
    },
}

print(contacts)
print(contacts['Persona_1'])