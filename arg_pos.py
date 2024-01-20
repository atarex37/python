import customtkinter as ctk

def ajouter_message(message):
    """
    Ajoute un message à la zone de texte.

    Args:
        message: Le message à ajouter.
    """

    global zone_texte

    zone_texte.insert("end", message + "\n")

def main():
    """
    Fonction principale.
    """

    global fenetre, zone_texte

    # Créer la fenêtre principale
    fenetre = ctk.CTk()
    fenetre.title("Affichage de messages")

    # Créer la zone de texte
    style = ctk.CTkStyle()
    style.configure(".", background="lightblue", font="Arial 12")
    zone_texte = ctk.CTkText(fenetre, style=".")
    zone_texte.pack()

    # Créer le bouton "Ajouter un message"
    bouton_ajouter = ctk.CTkButton(fenetre, text="Ajouter un message", command=ajouter_message)
    bouton_ajouter.pack()

    # Démarrer la boucle d'événements
    fenetre.mainloop()

if __name__ == "__main__":
    main()
