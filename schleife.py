import listen

for number in range(1, 7): # 7 nicht dabei
    print("Zimmernr: ", number )

for name in listen.names:
    print(name, "hat mich besuchen")

uhr=6

while uhr < 12:
    print("Keine Pause,da nur ",uhr," Uhr")
    uhr = uhr + 1
