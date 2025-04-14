from liste import Liste

def menu_liste():
    print("\n=== Menu Liste Chaînée ===")
    print("1. Créer une liste")
    print("2. Ajouter un élément")
    print("3. Trier la liste (Quicksort)")
    print("4. Afficher la liste")
    print("5. Quitter")
    return input("Choix (1-5): ")

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
            liste.append(val)  # On ajoute la valeur directement, pas un objet Liste
            print("Élément ajouté!")

        elif choix == "3":
            if liste is None:
                print("Créez d'abord une liste!")
                continue
            liste = liste.quicksort()
            print("Liste triée!")

        elif choix == "4":
            if liste is None:
                print("Liste vide")
            else:
                print("Liste:", liste)

        elif choix == "5":
            print("Au revoir!")
            break

        else:
            print("Choix invalide!")

if __name__ == "__main__":
    main()