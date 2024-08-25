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