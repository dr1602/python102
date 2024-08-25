# si copio una lista (a = b), este apuntara ambien al mismo espacio en memoria
# entonces, si modifico a, estos cambios tambien se veran en b

# si queremos evitar eso, debemos usar slicing

a = [1, 2, 3, 4, 5]
b = a

print(a)
print(b)

del a[0]

print(a)
print(b)

print(id(a))
print(id(b))

c = a[:]

print(id(a))
print(id(b))
print(id(c))

a.append(100)

print(a)
print(b)
print(c)