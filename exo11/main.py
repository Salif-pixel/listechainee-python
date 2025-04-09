from matcarree import MatCarree

def afficher_menu():
    print("\nMenu:")
    print("1. Créer une nouvelle matrice")
    print("2. Vérifier si la matrice est symétrique")
    print("3. Créer une représentation compacte")
    print("4. Accéder à un élément")
    print("5. Afficher la matrice")
    print("6. Quitter")
    return input("Votre choix (1-6): ")


def main():
    m = None
    c = None

    while True:
        choix = afficher_menu()

        if choix == "1":
            n = int(input("Taille de la matrice (n): "))
            m = MatCarree(n)
            print("Entrez les coefficients ligne par ligne:")
            for i in range(n):
                ligne = input(f"Ligne {i + 1} (séparés par des espaces): ").split()
                m.data[i] = [float(x) for x in ligne]
            print("Matrice créée avec succès!")

        elif choix == "2":
            if m is None:
                print("Veuillez d'abord créer une matrice!")
                continue
            if MatCarree.symetrique(m):
                print("La matrice est symétrique")
            else:
                print("La matrice n'est pas symétrique")

        elif choix == "3":
            if m is None:
                print("Veuillez d'abord créer une matrice!")
                continue
            c = MatCarree.sym_compacte(m, m.n)
            if c is not None:
                print("Représentation compacte créée:", c)
            else:
                print("La matrice n'est pas symétrique, impossible de créer une représentation compacte")

        elif choix == "4":
            if c is None:
                print("Veuillez d'abord créer une représentation compacte!")
                continue
            i = int(input("Index i: "))
            j = int(input("Index j: "))
            print(f"Element ({i},{j}): {MatCarree.acces(c, i, j, m.n)}")

        elif choix == "5":
            if c is None:
                print("Veuillez d'abord créer une représentation compacte!")
                continue
            MatCarree.afficher(c, m.n)

        elif choix == "6":
            print("Au revoir!")
            break

        else:
            print("Choix invalide, veuillez réessayer")


if __name__ == "__main__":
    main()