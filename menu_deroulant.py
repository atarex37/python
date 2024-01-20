import os
import tkinter
from tkinter import ttk
from tkinter import *

os.system('cls')

root = tkinter.Tk() 
root.geometry('300x200')

# création du bouton quitter
btn_quit = Button(root , text = "Fermer la fenêtre !" , command = quit)
btn_quit.place(x = 100 , y = 50)

"""
def action(event):
    # Obtenir l'élément sélectionné
    select = listeCombo.get()
    print("Vous avez sélectionné : '", select,"'")
"""

labelChoix = tkinter.Label(root, text = "Veuillez faire un choix !")
labelChoix.pack()

List_files = []

path = os.getcwd()
print('path : ', path)

xlsx_path = os.path.join(path, "Excel")
print('xlsx_path : ', xlsx_path)

List_files = os.listdir("D:\OneDrive\Documents\Emmanuel\Python\Excel")
print('List_files : ', List_files)

#print(len(List_files))
for val in List_files :
    #print(val)
    if ".xlsx" not in val :
      
        List_files.remove(val)


print('List_files avec uniquement extension xlsx : ', List_files)
# Création de la Combobox via la méthode ttk.Combobox()
listeCombo = ttk.Combobox(root, values=List_files)
# Choisir l'élément qui s'affiche par défaut
listeCombo.current(0)
listeCombo.pack()
select = listeCombo.get()
#listeCombo.bind("<<ComboboxSelected>>", action)
root.mainloop()


print("Vous avez sélectionné : '", select,"'")