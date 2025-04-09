from liste import Liste


def menu_liste():
    print("\n=== Menu Liste Chaînée ===")
    print("1. Créer une liste")
    print("2. Ajouter un élément")
    print("3. Trier la liste (Quicksort)")
    print("4. Supprimer éléments inférieurs")
    print("5. Afficher la liste")
    print("6. Quitter")
    return input("Choix (1-6): ")


def main():
    liste = None

    while True:
        choix = menu_liste()

        if choix == "1":
            val = input("Entrez la première valeur: ")
            liste = Liste(val)
            print("Liste créée!")

        elif choix == "2":
            if liste is None:
                print("Créez d'abord une liste!")
                continue
            val = input("Entrez la valeur à ajouter: ")
            liste.append(Liste(val))
            print("Élément ajouté!")

        elif choix == "3":
            if liste is None:
                print("Créez d'abord une liste!")
                continue
            liste = liste.quicksort()
            print("Liste triée!")

        elif choix == "4":
            if liste is None:
                print("Créez d'abord une liste!")
                continue
            inferieurs = liste.supprimer_inferieurs()
            print(f"Éléments supprimés: {inferieurs}")
            print(f"Liste restante: {liste}")

        elif choix == "5":
            if liste is None:
                print("Liste vide")
            else:
                print("Liste:", liste)

        elif choix == "6":
            print("Au revoir!")
            break

        else:
            print("Choix invalide!")


if __name__ == "__main__":
    main()