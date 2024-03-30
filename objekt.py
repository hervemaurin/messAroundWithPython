class auto:
    idNumer = 0

    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe
        auto.idNumer += 1

    def __str__(self):
        return "Idennr: " + str(auto.idNumer) +" , "+ self.marke + " , " + self.farbe

a1 = auto("Mercedess", "Rot")
a2 = auto("Mercedesse", "Grun")

print(a1 , a2)

class spieler:
    def __init__(self, name, life, kugel):
        self.name = name
        self.life = life
        self.kugel = kugel

    def get_life(self):
        return self.life
    def get_kugel(self):
        return self.kugel

    def attack(self, spielerx, kugel):
        spielerx.life = spielerx.get_life() - kugel
        self.kugel = self.kugel - kugel
        print("Du hast spieler <" + spielerx.name + "> "
              + str(kugel) + " mal getroffen. Dir bleibt nur " +
              str(self.kugel) + " Kügel übrig.")

    def __str__(self):
        return "name: " + self.name + ", Gesundheit: " + str(self.life) + ", Kugel: " + str(self.kugel)

naruto = spieler("naruto", 20, 15)
boruto = spieler("boruto", 20, 15)
print(boruto)
print(naruto)


naruto.attack(boruto, 8)

print(boruto)
print(naruto)

