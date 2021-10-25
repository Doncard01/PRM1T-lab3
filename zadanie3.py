N = int(input("Podaj N: "))
pierwsza = True
for i in range(2, N-1):
    if(N%i == 0):
        pierwsza = False
        print(f"{N} nie jest liczbą pierwszą, ma dzielnik {i}")
        break

if(pierwsza == True):
    print(f"{N} jest liczbą pierwszą")
