print("Dobrodošli u program za preračunavanje milja u kilometre!")
opet = "da"

while True:
    if opet.lower() == "da":
        km = input("Upišite broj kilometara: ")
        km = float(km.replace(",", "."))
        mi = km * 0.62137
        print(str(km) + " km = " + str(mi) + " mi.")

        opet = input("Nova pretvorba? (da/ne)")
    elif opet.lower() == "ne":
        print("Doviđenja!")
        break
    else:
        print("Pogreška! Upišite da ili ne.")

        opet = input("Nova pretvorba? (da/ne)")
