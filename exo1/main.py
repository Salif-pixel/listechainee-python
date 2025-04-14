from liste import Liste


def afficher_menu():
    """Affiche le menu d'options disponibles."""
    print("\n===== MENU - GESTION DE LISTES CHAÎNÉES =====")
    print("1. Créer une nouvelle liste")
    print("2. Afficher la liste")
    print("3. Ajouter une valeur à la fin de la liste")
    print("4. Concaténer une autre liste")
    print("5. Supprimer les éléments inférieurs au premier")
    print("6. Trier la liste (quicksort)")
    print("0. Quitter")
    print("============================================")


def creer_liste():
    """Crée une nouvelle liste chaînée à partir des entrées utilisateur."""
    valeurs = input("Entrez les valeurs séparées par des espaces: ").split()
    if not valeurs:
        return None

    premiere_liste = Liste(valeurs[0])
    liste_courante = premiere_liste

    for i in range(1, len(valeurs)):
        liste_courante.suite = Liste(valeurs[i])
        liste_courante = liste_courante.suite

    return premiere_liste


def main():
    """Fonction principale avec menu interactif."""
    ma_liste = None
    choix = -1

    while choix != 0:
        afficher_menu()

        try:
            choix = int(input("Votre choix: "))
        except ValueError:
            print("Erreur: veuillez entrer un nombre entier.")
            continue

        if choix == 0:
            print("Au revoir!")

        elif choix == 1:
            ma_liste = creer_liste()
            if ma_liste:
                print("Liste créée avec succès!")
            else:
                print("Aucune liste créée.")

        elif choix == 2:
            if ma_liste:
                print("Liste actuelle:", ma_liste)
            else:
                print("Aucune liste à afficher. Créez d'abord une liste.")

        elif choix == 3:
            if ma_liste:
                valeur = input("Entrez la valeur à ajouter: ")
                nouvelle_liste = Liste(valeur)
                ma_liste.append(nouvelle_liste)
                print(f"Valeur '{valeur}' ajoutée à la fin de la liste.")
            else:
                print("Aucune liste existante. Créez d'abord une liste.")

        elif choix == 4:
            if ma_liste:
                autre_liste = creer_liste()
                if autre_liste:
                    ma_liste.append(autre_liste)
                    print("Listes concaténées avec succès!")
                else:
                    print("Aucune liste à concaténer.")
            else:
                print("Aucune liste principale existante. Créez d'abord une liste.")

        elif choix == 5:
            if ma_liste:
                inferieurs = ma_liste.suprimerInferieur()
                print("Éléments inférieurs supprimés.")
                if inferieurs:
                    print("Éléments supprimés:", inferieurs)
                else:
                    print("Aucun élément inférieur trouvé.")
            else:
                print("Aucune liste existante. Créez d'abord une liste.")

        elif choix == 6:
            if ma_liste:
                ma_liste = ma_liste.quicksort()
                print("Liste triée avec succès!")
            else:
                print("Aucune liste à trier. Créez d'abord une liste.")

        else:
            print("Option invalide. Veuillez choisir une option entre 0 et 6.")


if __name__ == "__main__":
    main()