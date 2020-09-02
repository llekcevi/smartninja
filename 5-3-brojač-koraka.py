def koraci(udaljenost, duzina_koraka):
    rezultat = udaljenost / duzina_koraka
    return rezultat


br1 = input("Unesi udaljenost. ")
br2 = input("Unesi dužinu svog koraka. ")
br1 = float(br1.replace(",", "."))
br2 = float(br2.replace(",", "."))

print(f"Potrebno je {koraci(br1, br2)} koraka.")
