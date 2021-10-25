import math
N = int(input("Podaj N: "))

for i in range(N+1):
    kwadrat = i**2
    pierwiastek = math.sqrt(i)
    print(f"Wartość: {i}, kwadrat: {kwadrat}, pierwiastek: {pierwiastek}")