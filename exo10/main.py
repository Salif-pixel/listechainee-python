from maillon import Maillon


def afficher_menu():
    print("\n=== MENU VECTEUR CREUX ===")
    print("1. Créer un nouveau vecteur creux")
    print("2. Afficher un vecteur creux")
    print("3. Additionner deux vecteurs creux")
    print("4. Quitter")
    return input("Votre choix: ")


def saisir_vecteur():
    try:
        entree = input("Entrez les éléments du vecteur séparés par des espaces: ")
        elements = [float(x) for x in entree.split()]
        return elements
    except ValueError:
        print("Erreur: Veuillez entrer des nombres valides.")
        return saisir_vecteur()


def main():
    vecteurs = {}  # Dictionnaire pour stocker les vecteurs
    compteur_vecteurs = 0

    while True:
        choix = afficher_menu()

        if choix == '1':
            elements = saisir_vecteur()
            compteur_vecteurs += 1
            nom_vecteur = f"v{compteur_vecteurs}"
            vecteurs[nom_vecteur] = Maillon.vecteur_creux(elements, len(elements))
            print(f"Vecteur '{nom_vecteur}' créé avec succès.")

        elif choix == '2':
            if not vecteurs:
                print("Aucun vecteur disponible. Veuillez en créer un d'abord.")
                continue

            print("Vecteurs disponibles:", ", ".join(vecteurs.keys()))
            nom = input("Entrez le nom du vecteur à afficher: ")

            if nom in vecteurs:
                Maillon.afficher_vecteur_creux(vecteurs[nom])
            else:
                print(f"Erreur: Le vecteur '{nom}' n'existe pas.")

        elif choix == '3':
            if len(vecteurs) < 2:
                print("Il faut au moins deux vecteurs pour effectuer une addition.")
                continue

            print("Vecteurs disponibles:", ", ".join(vecteurs.keys()))
            nom1 = input("Entrez le nom du premier vecteur: ")
            nom2 = input("Entrez le nom du deuxième vecteur: ")

            if nom1 in vecteurs and nom2 in vecteurs:
                compteur_vecteurs += 1
                nom_resultat = f"v{compteur_vecteurs}"
                vecteurs[nom_resultat] = Maillon.somme(vecteurs[nom1], vecteurs[nom2])
                print(f"La somme est stockée dans '{nom_resultat}'")
                Maillon.afficher_vecteur_creux(vecteurs[nom_resultat])
            else:
                if nom1 not in vecteurs:
                    print(f"Erreur: Le vecteur '{nom1}' n'existe pas.")
                if nom2 not in vecteurs:
                    print(f"Erreur: Le vecteur '{nom2}' n'existe pas.")

        elif choix == '4':
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()