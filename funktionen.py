

def presentation(name="defaul-name"):
    print("Morgen ich heiße ",name)

presentation()
presentation("Ali")
presentation(name="Aissa")


def multikation(a=5,b=3):
    resul = a*b
    print(resul)
    # multiplikation(a,b) hier für zu endloseschleife

multikation()
values=[2,7]
multikation(*values)



