name = "Carli"
caracter = "c"
nombre = 'Carli'

segundo_nombre = '''

Carli

Las comillas triples son sensibles al salto de linea

Marcela

'''

print(type(segundo_nombre))
print(segundo_nombre)

print(name[0])
print(name[1])
print(name[2])

# print(name[21])

print(name[-1])
print(name[-2])
print(name[-3])

# concatenacion y repeticion
# buenas practicas, legible y replicable

first_name = 'CARLA Marcela'
last_name = '   Florida y RUMANA   '

print(first_name)
print(last_name)
print(first_name + ' ' + last_name)

print (first_name * 6)
print (3 * last_name)

# consultas

print(len(last_name))
print(len(first_name))

# metodos para los strings, porquees propia del string como hay metodos para arrays

print(first_name.lower())
print(last_name.upper())
print(last_name.strip())

