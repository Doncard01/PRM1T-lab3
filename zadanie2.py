a1 = int(input(f"Podaj a1: "))
n = int(input(f"Podaj n: "))
r = int(input(f"Podaj r: "))
suma = 0
for i in range(n):
   an = a1 + i*r
   print(an)
   suma += an
print(f"Suma: {suma}")