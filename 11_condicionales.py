x = 5

# python es estrictamente ordenado

if x > 5:
    print('x es mayor que 5')
    print('adentro del if')
elif x == 5: 
    print('x es igual a 5')
    print('dentro del primer elif')
else:
    print('x es menor que 5')
    print('estamos dentro del else')
    
x = 15
y = 20

if x > 10 and y > 25:
    print('"x" es mayor a 10 y "y" es mayor que 25')

if x > 10 or y > 25:
    print('"x" es mayor a 10 o "y" es mayor que 25')
    
if not x < 10:
    print('"x" no es es menor que 10, capichi')
    
is_member = True
age = 11

if is_member:
    if age >= 15:
        print('Tienes acceso ya queres miembrio y eres mayor que o tienes 15 anios.')
    else:
        print('No tienes acceso ya que eres miembro pero eres menor de 15 anios.')
else:
    print('Lo siento, no eres miembro y NO TIENES ACCESO')