# operadores numericos
a = 10
b = 3

print('Suma:', a + b)
print('Resta:', a - b)
print('Multiplicacion:', a * b)
print('Division:', a / b)

# operadores especiales, el module

print('Modulo:', a % b)
print('Parte Entera de Division:', a // b)
print('Potencia:', a ** b)

# atajos o shorcuts de operaciones

print('Atajos de operaciones')

a = 10

a = a + 2
print(a)
#12

a += 2
print(a)
#14

a -= 2
print(a)
#12

a *= 2
print(a)
#24

a **= 2
print(a)
#576

a /= 2
print(a)
#288.0

a //= 2
print(a)
#144.0

a %= 2
print(a)
#0.0

operation_1 = 2 + 3 * 4
operation_2 = (2 + 3) * 4
print(operation_1)
print(operation_2)

operation_3 = (2 + 3) * (4 ** 2) / 8 - 1

print(operation_3)

a = 10
b = 3

print ( a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)