sitz=30
messages = int(input("Anzahl Passagiere bitte!"))

if sitz > messages:
    print("jede Passagiere werden sitz haben")
else:
    print("es gibt nicht genuge Plätzen")

geld = int(input("Wieviel haben Sie?"))
esparnisse = int(input("Wieviel haben Sie in gespart?"))
ordi=3000

if geld>ordi:
    print("Sie konnen sich den ordi leisten")
elif (geld+esparnisse)>ordi:
    print("Sie können sich den ordi leisten indem sie auf Ihre"
          "sparkonnto zugreifen")
else:
    print("Sie können sich nicht den computer leisten")

#tenäre operator
var = "ja" if 3 > 2 else "nein"
print(var)