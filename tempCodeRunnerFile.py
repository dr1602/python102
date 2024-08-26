def sumatoria(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sumatoria(n - 1)

sumatoria = print(sumatoria(6))