broj = int(input("Upiši jedan broj između 1 i 100."))
print(broj)

for x in range(1, broj + 1):
    if x % 3 == 0 and x % 5 != 0:
        print(" fizz ")
    elif x % 5 == 0 and x % 3 != 0:
        print(" buzz ")
    elif x % 3 == 0 and x % 5 == 0:
        print(" fizz buzz")
    else:
        print(x)
