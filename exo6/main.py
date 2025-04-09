from maillon import Maillon


def afficher_menu():
    print("\n=== MENU LISTE CHAÎNÉE ===")
    print("1. Ajouter un mot au début")
    print("2. Ajouter un mot à la fin")
    print("3. Supprimer un mot")
    print("4. Afficher les premiers mots")
    print("5. Purifier la liste (supprimer les doublons)")
    print("6. Quitter")
    return input("Votre choix: ")


def main():
    L = None
    while True:
        choix = afficher_menu()

        if choix == '1':
            mot = input("Entrez le mot à ajouter au début: ")
            L = Maillon.ajoute_debut(mot, L)
            print(f"'{mot}' a été ajouté au début de la liste.")

        elif choix == '2':
            mot = input("Entrez le mot à ajouter à la fin: ")
            L = Maillon.ajoute_fin(mot, L)
            print(f"'{mot}' a été ajouté à la fin de la liste.")

        elif choix == '3':
            mot = input("Entrez le mot à supprimer: ")
            ancien_L = L
            L = Maillon.supprimer(mot, L)
            if L == ancien_L:
                print(f"'{mot}' n'a pas été trouvé dans la liste.")
            else:
                print(f"'{mot}' a été supprimé de la liste.")

        elif choix == '4':
            try:
                n = int(input("Combien de mots voulez-vous afficher? "))
                print("\nPremiers mots de la liste:")
                Maillon.premiers(L, n)
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        elif choix == '5':
            print("Purification de la liste (suppression des doublons)...")
            print("Note: La liste doit être triée pour un résultat correct.")
            Maillon.purifie(L)
            print("Liste purifiée.")

        elif choix == '6':
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()