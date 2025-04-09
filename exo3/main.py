from grand_entier import GrandInt


def menu_grand_entier():
    print("\n=== Menu Grand Entier ===")
    print("1. Créer à partir d'un entier")
    print("2. Afficher le grand entier")
    print("3. Nombre de chiffres")
    print("4. Quitter")
    return input("Choix (1-4): ")


def main():
    grand_int = None

    while True:
        choix = menu_grand_entier()

        if choix == "1":
            nombre = int(input("Entrez un nombre entier: "))
            grand_int = GrandInt.from_int(nombre)
            print("Grand entier créé!")

        elif choix == "2":
            if grand_int is None:
                print("Créez d'abord un grand entier!")
            else:
                print("Grand entier:", grand_int)

        elif choix == "3":
            if grand_int is None:
                print("Créez d'abord un grand entier!")
            else:
                print("Nombre de chiffres:", grand_int.nombre_de_chiffres())

        elif choix == "4":
            print("Au revoir!")
            break

        else:
            print("Choix invalide!")


if __name__ == "__main__":
    main()