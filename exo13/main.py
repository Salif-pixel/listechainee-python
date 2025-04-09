from noeudabr import  IndexABR

def afficher_menu():
    print("\nMenu Index ABR:")
    print("1. Créer l'index exemple")
    print("2. Ajouter un nom avec pages")
    print("3. Supprimer un numéro de page")
    print("4. Afficher l'index")
    print("5. Équilibrer l'arbre")
    print("6. Quitter")
    return input("Votre choix (1-6): ")


def creer_index_exemple():
    """Crée l'index exemple de la démo"""
    index = None

    fatou_pages = [110, 250, 300]
    index = IndexABR.ajout_nompropre("Fatou", fatou_pages, len(fatou_pages), index)

    mamadou_pages = [3, 14, 101]
    index = IndexABR.ajout_nompropre("Mamadou", mamadou_pages, len(mamadou_pages), index)

    ousseynou_pages = [11, 50]
    index = IndexABR.ajout_nompropre("Ousseynou", ousseynou_pages, len(ousseynou_pages), index)

    pierre_pages = [3, 7, 100, 287]
    index = IndexABR.ajout_nompropre("Pierre", pierre_pages, len(pierre_pages), index)

    soda_pages = [6, 10, 34, 66, 98]
    index = IndexABR.ajout_nompropre("Soda", soda_pages, len(soda_pages), index)

    return index


def main():
    index = None

    while True:
        choix = afficher_menu()

        if choix == "1":
            index = creer_index_exemple()
            print("Index exemple créé avec succès!")

        elif choix == "2":
            if index is None:
                print("Veuillez d'abord créer un index!")
                continue
            nom = input("Entrez le nom à ajouter: ")
            pages = input("Entrez les numéros de page (séparés par des espaces): ").split()
            pages = [int(p) for p in pages]
            index = IndexABR.ajout_nompropre(nom, pages, len(pages), index)
            print(f"Nom {nom} ajouté avec succès!")

        elif choix == "3":
            if index is None:
                print("Veuillez d'abord créer un index!")
                continue
            nom = input("Entrez le nom: ")
            numero = int(input("Entrez le numéro de page à supprimer: "))
            index = IndexABR.supprimer_numero(nom, numero, index)
            print(f"Numéro {numero} supprimé pour {nom}")

        elif choix == "4":
            if index is None:
                print("Veuillez d'abord créer un index!")
                continue
            print("\nIndex alphabétique:")
            IndexABR.afficher_index(index)

        elif choix == "5":
            if index is None:
                print("Veuillez d'abord créer un index!")
                continue
            index = IndexABR.equilibrer_abr(index)
            print("Arbre équilibré avec succès!")

        elif choix == "6":
            print("Au revoir!")
            break

        else:
            print("Choix invalide, veuillez réessayer")


if __name__ == "__main__":
    main()