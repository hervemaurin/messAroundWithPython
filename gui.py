from tkinter import *

"""
from tkinter import messagebox
# Fonction pour afficher une boîte de dialogue avec un message
def show_message():
    messagebox.showinfo("Message", "Bonjour, vous avez cliqué sur le bouton!")
# Création de la fenêtre principale
root = tk.Tk()
root.title("Exemple de widgets")
# Création d'un label
label = tk.Label(root, text="Ceci est un label")
label.pack()
# Création d'un bouton
button = tk.Button(root, text="Cliquez ici", command=show_message)
button.pack()
# Création d'une entrée de texte
entry = tk.Entry(root)
entry.pack()
# Lancement de la boucle principale
root.mainloop()

print(os.getcwd())
"""

root = Tk()
root.title("Interface")
#root.iconbitmap("hour_time_watch_clock_icon_262574.ico")
root.geometry("500x700")
root.minsize(200, 300)
root.maxsize(700,1000)

box= Frame(root, bg="red", border="4")
title = Label(box, text = "Meine Interface")
title.pack(fill=X, pady=10, padx=10)
champ = Entry(box)
champ.pack(fill=X)
hacken = Checkbutton(box, text="hacken")
hacken.pack(fill=X)
knopf = Button(box, text="Click")
knopf.pack(fill=X)

box.pack(side=LEFT, expand=TRUE)


box= Frame(root, bg="red", border="4")
title = Label(box, text = "Meine Interface")
title.pack(fill=X, ipady=10, ipadx=10)
champ = Entry(box)
champ.pack(fill=X)
hacken = Checkbutton(box, text="hacken")
hacken.pack(fill=X)
knopf = Button(box, text="Click")
knopf.pack(fill=X)

box.pack(side=LEFT, expand=TRUE)


root.mainloop()