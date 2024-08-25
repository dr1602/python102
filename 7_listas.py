# sintaxis de lista, estar dentro de []
to_do = [
    'dirigirnos al hotel',
    'ir a almozar',
    'visitar un museo',
    'volver al hotel',
]

print(to_do)
print(type(to_do))

numbers = [
    1,
    2,
    3,
    'cuatro',
    'cinco',
    'seis',
]

print(numbers)
print(type(numbers))

mix = [
    'uno',
    2,
    3.141592365,
    True,
    [ 1, 2, 3, 'cuatro']
]

print(mix)
print(len(mix))
print('Tercer elemento es:', mix[2])
print('El ultimo elemento dentro del cuarto elemento es:', mix[4][-1])

# slicing para extraer porciones de informacion

string = 'Hola mundo'

print(string)
print(len(string))
print('El primer elemento es:', string[0])
print('El segundo elemento es:', string[1])
print('El ultimo elemento es:', string[-1])

# este es el slicing, el final lo considerando restandole uno en lugar de 3 es 3-1 = 2
print(mix[0:3])
print(mix[:3])
print(mix[3:])
print(mix[2:-2])
print(mix)

mix.append(False)
print(mix)

mix[4].append(True)
print(mix)

mix.append(['a', 'b'])
print(mix)

mix.insert(1,['y','z'])
print(mix)

# para buscar un elemento en una lista
print(mix.index(['a', 'b']))

numbers = [
    1,
    2,
    100,
    90.45,
    3,
    4,
    200,
    23e12,
    5,
    6,
    100000e-8
]

print(numbers)
print('El elemento de mayor magnitud es: ', max(numbers))
print('El elemento de menor magnitud es: ', min(numbers))

del numbers[-1]
print(numbers)

del numbers[:6]
print(numbers)

del numbers
print(numbers)