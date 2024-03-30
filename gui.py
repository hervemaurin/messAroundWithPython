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
root.geometry("300x400")
root.minsize(200, 300)
root.maxsize(400,500)

title = Label(root, text = "Meine Interface")
title.pack()
champ = Entry(root)
champ.pack()
hacken = Checkbutton(text="hacken", image="heim.png")
hacken.pack()
knopf = Button(text="Click")
knopf.pack()



root.mainloop()