# arreglos de datos que son mutables

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[0])

# tuplas, arreglos con dato no mutables/ INMUTABLES

number = (1, 2, 3, 4, 5)

print(number)
print(type(number))
print(number[0])

number[0] = 'uno'
print(number)

numbers = 1, 2, 3, 4, 5, 6

print(numbers)
print(type(numbers))