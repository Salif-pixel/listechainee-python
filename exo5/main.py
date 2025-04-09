from intervalle import IntervOuvert, IntervFerme


def menu_intervalle():
    print("\n=== Menu Intervalle ===")
    print("1. Créer intervalle ouvert")
    print("2. Créer intervalle fermé")
    print("3. Vérifier appartenance")
    print("4. Calculer intersection")
    print("5. Quitter")
    return input("Choix (1-5): ")


def main():
    intervalles = []

    while True:
        choix = menu_intervalle()

        if choix == "1":
            b_inf = int(input("Borne inférieure: "))
            b_sup = int(input("Borne supérieure: "))
            intervalles.append(IntervOuvert(b_inf, b_sup))
            print("Intervalle ouvert créé!")

        elif choix == "2":
            b_inf = int(input("Borne inférieure: "))
            b_sup = int(input("Borne supérieure: "))
            intervalles.append(IntervFerme(b_inf, b_sup))
            print("Intervalle fermé créé!")

        elif choix == "3":
            if not intervalles:
                print("Créez d'abord un intervalle!")
                continue
            n = int(input("Entier à vérifier: "))
            for i, intervalle in enumerate(intervalles):
                print(f"Intervalle {i + 1}: {intervalle} -> {n} {'∈' if intervalle.est_dans(n) else '∉'} l'intervalle")

        elif choix == "4":
            if len(intervalles) < 2:
                print("Créez au moins 2 intervalles!")
                continue
            intersection = intervalles[0].intersection(intervalles[1])
            print(f"Intersection {intervalles[0]} ∩ {intervalles[1]} = {intersection}")

        elif choix == "5":
            print("Au revoir!")
            break

        else:
            print("Choix invalide!")


if __name__ == "__main__":
    main()