from polynome import Polynome


def afficher_menu():
    print("\n=== MENU POLYNÔMES ===")
    print("1. Créer un nouveau polynôme")
    print("2. Ajouter un terme au polynôme")
    print("3. Afficher le polynôme")
    print("4. Calculer la dérivée première")
    print("5. Calculer la dérivée k-ième")
    print("6. Quitter")
    return input("Votre choix: ")


def creer_polynome_exemple():
    """Créer un polynôme exemple: 3x^4 + 2x^3 - 5x + 7"""
    p = Polynome()
    p.ajouter_terme(3, 4)
    p.ajouter_terme(2, 3)
    p.ajouter_terme(-5, 1)
    p.ajouter_terme(7, 0)
    return p


def main():
    polynome_courant = None

    while True:
        choix = afficher_menu()

        if choix == '1':
            print("Création d'un nouveau polynôme...")
            option = input("1. Polynôme vide\n2. Polynôme exemple (3x^4 + 2x^3 - 5x + 7)\nChoix: ")

            if option == '1':
                polynome_courant = Polynome()
                print("Un nouveau polynôme vide a été créé.")
            elif option == '2':
                polynome_courant = creer_polynome_exemple()
                print("Le polynôme exemple a été créé:")
                polynome_courant.afficher()
            else:
                print("Option invalide.")

        elif choix == '2':
            if polynome_courant is None:
                print("Aucun polynôme n'a été créé. Veuillez d'abord créer un polynôme.")
                continue

            try:
                coefficient = float(input("Entrez le coefficient: "))
                exposant = int(input("Entrez l'exposant: "))

                polynome_courant.ajouter_terme(coefficient, exposant)
                print(f"Le terme {coefficient}x^{exposant} a été ajouté.")
                print("Polynôme actuel:")
                polynome_courant.afficher()
            except ValueError:
                print("Veuillez entrer des valeurs numériques valides.")

        elif choix == '3':
            if polynome_courant is None:
                print("Aucun polynôme n'a été créé. Veuillez d'abord créer un polynôme.")
                continue

            print("Polynôme actuel:")
            polynome_courant.afficher()

        elif choix == '4':
            if polynome_courant is None:
                print("Aucun polynôme n'a été créé. Veuillez d'abord créer un polynôme.")
                continue

            print("Polynôme original:")
            polynome_courant.afficher()

            derivee = polynome_courant.derivee()
            print("Première dérivée:")
            derivee.afficher()

            option = input("Voulez-vous remplacer le polynôme actuel par sa dérivée? (o/n): ")
            if option.lower() == 'o':
                polynome_courant = derivee
                print("Le polynôme a été remplacé par sa dérivée.")

        elif choix == '5':
            if polynome_courant is None:
                print("Aucun polynôme n'a été créé. Veuillez d'abord créer un polynôme.")
                continue

            try:
                k = int(input("Entrez l'ordre de la dérivée (k): "))
                if k < 0:
                    print("L'ordre de la dérivée doit être non-négatif.")
                    continue

                print(f"Polynôme original:")
                polynome_courant.afficher()

                derivee_k = polynome_courant.derivee_kieme(k)
                print(f"Dérivée d'ordre {k}:")
                derivee_k.afficher()

                option = input(f"Voulez-vous remplacer le polynôme actuel par sa dérivée d'ordre {k}? (o/n): ")
                if option.lower() == 'o':
                    polynome_courant = derivee_k
                    print(f"Le polynôme a été remplacé par sa dérivée d'ordre {k}.")
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

        elif choix == '6':
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()