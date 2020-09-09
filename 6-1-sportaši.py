class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

print("\n Dobrodošli u program za unos podataka o sportašima. \n")

izbor = input("Želiš li unijeti podatke o košarkašu ili nogometašu? (upiši 'k' ili 'n')")

if izbor.lower() == "n":

    print("Unesi podatke o nogometašu!")

    f_name = input("Ime: ")
    l_name = input("Prezime: ")
    height = input("Visina: ")
    weight = input("Težina: ")
    goals = input("Golovi: ")
    y_cards = input("Žuti kartoni: ")
    r_cards = input("Crveni kartoni: ")

    new_player = FootballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight),
                                goals=int(goals), yellow_cards=int(y_cards), red_cards=int(r_cards))

elif izbor.lower() == "k":
    print("Unesi podatke o košarkašu!")

    f_name = input("Ime: ")
    l_name = input("Prezime: ")
    height = input("Visina: ")
    weight = input("Težina: ")
    points = input("Poeni: ")
    rebounds = input("Skokovi: ")
    assists = input("Asistencije: ")

    new_player = BasketballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight),
                                points=int(points), rebounds=int(rebounds), assists=int(assists))

with open("players.txt", "w") as football_file:
    football_file.write(str(new_player.__dict__))


print("Player successfully entered!")
print("Player's data: {0}".format(new_player.__dict__))
