# para trabajar con colecciones de forma eficiente,
# podemos trabjara con grandes cantidades de informacion si almacnear todo a la misma vez en memoria

# ITERADORES, iteran los elementos sin utilizar indices

# Crear una lista
my_list = [1, 2, 3, 4]

# Obtener el iterador
my_iter = iter(my_list)

# usar el iterador
# next ayuda a saber que valroes se guardan o almacenan en memoria
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(type(next(my_iter)))

# iterar en cadenas

# creando la caden
text = 'Hola mundo'

# creando el objeto iterador
iter_text = iter(text)

# iterar en la cadena
for char in iter_text:
    print(char)

# Crear un iterador para los numeros impares

# Limite
limit = 10

# crear iterador de impares
odd_iter = iter(range(1, limit + 1, 2))

# usar el iterador para encontrar impares
for num in odd_iter:
    print(num)
    
# crear iterador de pares
pair_iter = iter(range(0, limit + 1, 2))

# usar el iterador para encontrar pares
for num in pair_iter:
    print(num)
    
# GENERADOR, produce una secuencia de numeros donde podemos iterar.
# ahora usaremos yield para devolver un valor

def my_generator():
    yield 1
    yield 2
    yield 3
    
for value in my_generator():
    print(value)
    
# Fibonacci
# 0 1 1 2 3 5 8 13 21...

def Fibonacci(limit):
    a, b = 0, 1
    while a < limit :
        yield a
        a, b = b, a + b
        
for num in Fibonacci(10):
    print(num)
    
# crear generadores para ver numeros pares e impares
