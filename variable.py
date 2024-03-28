import main
import sys
main.print_hi("Johannes!")

nummer = 10
schuler = 12

print(dir(nummer))
print("Anzahl Schuler = " + str(schuler))
print(type(nummer))
schuler = "Ali"
print(len(schuler))
boolean = schuler == "Ali"
print(boolean)
print(schuler == "John")

nummmer = 1.3
print(type(nummmer))

print(sys.getsizeof(nummer))