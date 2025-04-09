class Maillon:
    def __init__(self, valeur=None):
        self.valeur = valeur
        self.suivant = None

    @staticmethod
    def creer_liste():
        """Crée une liste chaînée avec 10 valeurs saisies au clavier"""
        tete = None

        print("Entrez 10 valeurs:")
        for i in range(10):
            try:
                valeur = int(input(f"Entrez la valeur {i + 1}: "))
                nouveau = Maillon(valeur)

                # Ajout au début
                nouveau.suivant = tete
                tete = nouveau
            except ValueError:
                print("Veuillez entrer un entier valide.")
                # Décrémentation pour réessayer
                i -= 1

        return tete

    @staticmethod
    def afficher_liste(liste):
        """Affiche le contenu de la liste"""
        courant = liste
        while courant is not None:
            print(courant.valeur, end=" ")
            courant = courant.suivant
        print()

    @staticmethod
    def tester_egalite(liste1, liste2):
        """Teste si deux listes sont égales"""
        courant1 = liste1
        courant2 = liste2

        while courant1 is not None and courant2 is not None:
            if courant1.valeur != courant2.valeur:
                return False
            courant1 = courant1.suivant
            courant2 = courant2.suivant

        # Si une liste est plus longue que l'autre
        return courant1 is None and courant2 is None

    @staticmethod
    def copier_liste(liste):
        """Fonction auxiliaire pour copier une liste"""
        if liste is None:
            return None

        resultat = Maillon(liste.valeur)
        dernier = resultat

        courant = liste.suivant
        while courant is not None:
            nouveau = Maillon(courant.valeur)
            dernier.suivant = nouveau
            dernier = nouveau
            courant = courant.suivant

        return resultat

    @staticmethod
    def concatener_new_list(liste1, liste2):
        """Concatène deux listes en créant une troisième"""
        if liste1 is None:
            return Maillon.copier_liste(liste2)
        if liste2 is None:
            return Maillon.copier_liste(liste1)

        # Copie de la première liste
        resultat = None
        dernier = None

        courant = liste1
        while courant is not None:
            nouveau = Maillon(courant.valeur)
            if resultat is None:
                resultat = nouveau
            else:
                dernier.suivant = nouveau
            dernier = nouveau
            courant = courant.suivant

        # Copie et ajout de la deuxième liste
        courant = liste2
        while courant is not None:
            nouveau = Maillon(courant.valeur)
            dernier.suivant = nouveau
            dernier = nouveau
            courant = courant.suivant

        return resultat

    @staticmethod
    def concatener_in_place(liste1, liste2):
        """Concatène des listes sans en créer une troisième"""
        if liste1 is None:
            return liste2

        # Recherche du dernier élément de la première liste
        dernier = liste1
        while dernier.suivant is not None:
            dernier = dernier.suivant

        # Connexion à la deuxième liste
        dernier.suivant = liste2

        return liste1