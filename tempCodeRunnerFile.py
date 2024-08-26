limitImpar = 9
    
# Generador para impares

def Impares(limit):
    for num in range(1, limit + 1, 2):
        yield num
        
for num in Impares(limitImpar):
    print(num)