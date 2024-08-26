# recursividad factorial

def factorial(n):
    if n == 0:
        return 1
    else: 
        return n * factorial(n-1)

factorial_5 = print(factorial(30))

# recursividad con fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
fibonacci_5 = print(fibonacci(4))

# sumatoria de numeros naturales

def sumatoria(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sumatoria(n - 1)

sumatoria_5 = print(sumatoria(5))
