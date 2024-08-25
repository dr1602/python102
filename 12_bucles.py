# bucles y controles de iteracion

numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
    print('Aqui es igual a: ', i + 1)
    
# va hasta a un numero antes del que hemos especificado
for i in range(10):
    print(i)
    
# para elegir en que posicion empezar, utilizamos la siguiente estructura
for i in range(3, 10):
    print(i)
    
# dentro de for podemos utilizar el condicional if

fruist = ['Manzana', 'Pera', 'Uva', 'Naranja', 'Melon', 'Tomate', 'Uva']

for fruit in fruist:
    print('Esta es la iteracion numero: ', fruit)
    print(fruit)
    if fruit == 'Naranja':
        print('Naranja encontrada.')
        
# manera de iterar a traves de colecciones cuando etamos sujetos a una condicion

fruist = ['Manzana', 'Pera', 'Uva', 'Naranja', 'Melon', 'Tomate', 'Uva']

x = 0

# hay que tener cuidado en el while, hay que generar la condicion para que para el codigo
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1
    
    
x = 0

# para detener el codigo dada una condicion, usamos break
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1
    
    x = 0

# no terminar el codigo, omitir el paso a evaluar

numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
    if i == 3:
        continue
    print('Aqui es igual a: ', i)
    
# uso de break

for i in numbers:
    if i == 3:
        break
    print('Aqui es igual a: ', i)


    

    

