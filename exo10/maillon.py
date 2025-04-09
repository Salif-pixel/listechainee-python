class Maillon:
    def __init__(self, indice=0, valeur=0.0, suivant=None):
        self.indice = indice
        self.valeur = valeur
        self.suivant = suivant

    @staticmethod
    def nouveau_maillon(indice, valeur, suivant=None):
        """Crée un nouveau maillon avec les valeurs données"""
        return Maillon(indice, valeur, suivant)

    @staticmethod
    def vecteur_creux(t, n):
        """Convertit un tableau en représentation de vecteur creux"""
        tete = None

        # Parcourt le tableau à l'envers pour insérer au début (pour l'efficacité)
        for i in range(n - 1, -1, -1):
            if t[i] != 0:  # Ne stocke que les composantes non nulles
                tete = Maillon(i, t[i], tete)

        return tete

    @staticmethod
    def afficher_vecteur_creux(v):
        """Affiche un vecteur creux"""
        print("Vecteur creux: ", end="")
        courant = v
        while courant is not None:
            print(f"({courant.indice}: {courant.valeur})", end=" ")
            courant = courant.suivant
        print()

    @staticmethod
    def somme(a, b):
        """Additionne deux vecteurs creux a et b"""
        resultat = None
        dernier = None

        # Traite les deux vecteurs tant qu'il reste des éléments dans les deux
        while a is not None and b is not None:
            if a.indice < b.indice:
                # Prend l'élément de a
                nouveau = Maillon(a.indice, a.valeur)
                a = a.suivant
            elif b.indice < a.indice:
                # Prend l'élément de b
                nouveau = Maillon(b.indice, b.valeur)
                b = b.suivant
            else:  # a.indice == b.indice
                # Additionne les valeurs des deux vecteurs
                somme_valeurs = a.valeur + b.valeur
                if somme_valeurs != 0:  # Ne stocke que les résultats non nuls
                    nouveau = Maillon(a.indice, somme_valeurs)
                else:
                    # Saute cet élément si la somme est nulle
                    a = a.suivant
                    b = b.suivant
                    continue
                a = a.suivant
                b = b.suivant

            # Ajoute le nouveau nœud au résultat
            if resultat is None:
                resultat = nouveau
            else:
                dernier.suivant = nouveau
            dernier = nouveau

        # Ajoute les éléments restants de a
        while a is not None:
            nouveau = Maillon(a.indice, a.valeur)
            if resultat is None:
                resultat = nouveau
            else:
                dernier.suivant = nouveau
            dernier = nouveau
            a = a.suivant

        # Ajoute les éléments restants de b
        while b is not None:
            nouveau = Maillon(b.indice, b.valeur)
            if resultat is None:
                resultat = nouveau
            else:
                dernier.suivant = nouveau
            dernier = nouveau
            b = b.suivant

        return resultat