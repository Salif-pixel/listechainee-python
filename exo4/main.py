from polynome import Polynome, Polynome2


def menu_polynome():
    print("\n=== Menu Polynôme ===")
    print("1. Créer un polynôme")
    print("2. Additionner deux polynômes")
    print("3. Calculer la dérivée")
    print("4. Évaluer en un point")
    print("5. Résoudre équation 2nd degré")
    print("6. Quitter")
    return input("Choix (1-6): ")


def main():
    polynomes = []

    while True:
        choix = menu_polynome()

        if choix == "1":
            coeffs = input("Entrez les coefficients (séparés par des virgules): ")
            coeffs = [float(c) for c in coeffs.split(",")]
            p = Polynome(coeffs)
            polynomes.append(p)
            print("Polynôme créé:", p)

        elif choix == "2":
            if len(polynomes) < 2:
                print("Créez au moins 2 polynômes!")
                continue
            print("Résultat:", polynomes[0] + polynomes[1])

        elif choix == "3":
            if not polynomes:
                print("Créez d'abord un polynôme!")
                continue
            print("Dérivée:", polynomes[0].derivee())

        elif choix == "4":
            if not polynomes:
                print("Créez d'abord un polynôme!")
                continue
            x = float(input("Entrez la valeur de x: "))
            print("Résultat:", polynomes[0].evaluer(x))

        elif choix == "5":
            if not polynomes:
                print("Créez d'abord un polynôme!")
                continue
            if len(polynomes[0].coefficients) != 3:
                print("Le polynôme doit être de degré 2!")
                continue
            p2 = Polynome2(polynomes[0].coefficients)
            print("Solutions:", p2.resoudre_equation())

        elif choix == "6":
            print("Au revoir!")
            break

        else:
            print("Choix invalide!")


if __name__ == "__main__":
    main()