from maillon import Maillon


def afficher_menu():
    print("\n=== MENU LISTE CHAÎNÉE ===")
    print("1. Créer une liste")
    print("2. Créer une deuxième liste")
    print("3. Afficher liste 1")
    print("4. Afficher liste 2")
    print("5. Tester l'égalité des listes")
    print("6. Concaténer (nouvelle liste)")
    print("7. Concaténer (sur place)")
    print("8. Quitter")
    return input("Votre choix: ")


def main():
    liste1 = None
    liste2 = None
    liste_concat = None

    while True:
        choix = afficher_menu()

        if choix == '1':
            liste1 = Maillon.creer_liste()
            print("Liste 1 créée.")

        elif choix == '2':
            liste2 = Maillon.creer_liste()
            print("Liste 2 créée.")

        elif choix == '3':
            if liste1 is None:
                print("La liste 1 n'a pas encore été créée.")
            else:
                print("Contenu de la liste 1:")
                Maillon.afficher_liste(liste1)

        elif choix == '4':
            if liste2 is None:
                print("La liste 2 n'a pas encore été créée.")
            else:
                print("Contenu de la liste 2:")
                Maillon.afficher_liste(liste2)

        elif choix == '5':
            if liste1 is None or liste2 is None:
                print("Les deux listes doivent être créées d'abord.")
            else:
                resultat = Maillon.tester_egalite(liste1, liste2)
                if resultat:
                    print("Les listes sont égales.")
                else:
                    print("Les listes sont différentes.")

        elif choix == '6':
            if liste1 is None or liste2 is None:
                print("Les deux listes doivent être créées d'abord.")
            else:
                liste_concat = Maillon.concatener_new_list(liste1, liste2)
                print("Listes concaténées (nouvelle liste):")
                Maillon.afficher_liste(liste_concat)
                print("Liste 1 (inchangée):")
                Maillon.afficher_liste(liste1)
                print("Liste 2 (inchangée):")
                Maillon.afficher_liste(liste2)

        elif choix == '7':
            if liste1 is None or liste2 is None:
                print("Les deux listes doivent être créées d'abord.")
            else:
                # Pour préserver liste1 originale, on fait une copie
                liste1_copie = Maillon.copier_liste(liste1)
                liste_concat = Maillon.concatener_in_place(liste1_copie, Maillon.copier_liste(liste2))
                print("Listes concaténées (sur place):")
                Maillon.afficher_liste(liste_concat)
                print("Liste 1 (originale, inchangée):")
                Maillon.afficher_liste(liste1)
                print("Liste 2 (originale, inchangée):")
                Maillon.afficher_liste(liste2)

        elif choix == '8':
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()