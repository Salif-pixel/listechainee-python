from maillon import Maillon


def afficher_menu():
    print("\n=== MENU LISTE DOUBLEMENT CHAÎNÉE ===")
    print("1. Ajouter un élément au début")
    print("2. Supprimer un élément")
    print("3. Afficher la liste (début -> fin)")
    print("4. Afficher la liste (fin -> début)")
    print("5. Quitter")
    return input("Votre choix: ")


def main():
    # On n'utilise pas de variables globales, mais on passe premier et dernier en paramètres
    premier = None
    dernier = None

    while True:
        choix = afficher_menu()

        if choix == '1':
            info = input("Entrez l'information à ajouter: ")
            premier, dernier = Maillon.ajouter_devant(info, premier, dernier)
            print(f"'{info}' a été ajouté au début de la liste.")

        elif choix == '2':
            if premier is None:
                print("La liste est vide.")
                continue

            info = input("Entrez l'information à supprimer: ")
            ancien_premier = premier
            premier, dernier = Maillon.supprimer(info, premier, dernier)

            # Vérification simpliste si quelque chose a été supprimé
            if premier != ancien_premier or premier is None:
                print(f"'{info}' a été supprimé de la liste.")
            else:
                print(f"'{info}' n'a pas été trouvé dans la liste.")

        elif choix == '3':
            print("\nContenu de la liste (début -> fin):")
            Maillon.afficher(premier)

        elif choix == '4':
            print("\nContenu de la liste (fin -> début):")
            Maillon.afficher_inverse(dernier)

        elif choix == '5':
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()