from arbrebin import ArbreBin


def afficher_menu():
    print("\nMenu Arbre Binaire:")
    print("1. Créer un arbre exemple")
    print("2. Afficher les feuilles")
    print("3. Afficher les degrés des nœuds")
    print("4. Trouver profondeur d'un nœud")
    print("5. Calculer la hauteur de l'arbre")
    print("6. Calculer la somme des nœuds")
    print("7. Quitter")
    return input("Votre choix (1-7): ")


def creer_arbre_exemple():
    """Crée l'arbre exemple de la démo"""
    root = ArbreBin(10)
    root.gauche = ArbreBin(5)
    root.droite = ArbreBin(15)
    root.gauche.gauche = ArbreBin(3)
    root.gauche.droite = ArbreBin(7)
    root.droite.gauche = ArbreBin(12)
    root.droite.droite = ArbreBin(20)
    return root


def main():
    arbre = None

    while True:
        choix = afficher_menu()

        if choix == "1":
            arbre = creer_arbre_exemple()
            print("Arbre exemple créé avec succès!")

        elif choix == "2":
            if arbre is None:
                print("Veuillez d'abord créer un arbre!")
                continue
            print("Feuilles de l'arbre:", end=" ")
            ArbreBin.feuille(arbre)
            print()

        elif choix == "3":
            if arbre is None:
                print("Veuillez d'abord créer un arbre!")
                continue
            print("\nDegrés des nœuds:")
            ArbreBin.degre(arbre)

        elif choix == "4":
            if arbre is None:
                print("Veuillez d'abord créer un arbre!")
                continue
            x = int(input("Entrez l'étiquette du nœud à trouver: "))
            if not ArbreBin.profondeur(arbre, x):
                print(f"Nœud {x} non trouvé dans l'arbre")

        elif choix == "5":
            if arbre is None:
                print("Veuillez d'abord créer un arbre!")
                continue
            print(f"Hauteur de l'arbre: {ArbreBin.hauteur(arbre)}")

        elif choix == "6":
            if arbre is None:
                print("Veuillez d'abord créer un arbre!")
                continue
            print(f"Somme des nœuds: {ArbreBin.som_noeuds(arbre)}")

        elif choix == "7":
            print("Au revoir!")
            break

        else:
            print("Choix invalide, veuillez réessayer")


if __name__ == "__main__":
    main()