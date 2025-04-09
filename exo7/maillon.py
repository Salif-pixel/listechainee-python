class Maillon:
    def __init__(self, info=None):
        self.info = info  # String information
        self.suivant = None
        self.precedent = None

    @staticmethod
    def ajouter_devant(s, premier=None, dernier=None):
        """Ajoute un nouveau nœud avec la chaîne s au début de la liste"""
        nouveau = Maillon(s)

        # Si la liste est vide
        if premier is None:
            premier = nouveau
            dernier = nouveau
        else:
            nouveau.suivant = premier
            premier.precedent = nouveau
            premier = nouveau

        return premier, dernier

    @staticmethod
    def supprimer(s, premier=None, dernier=None):
        """Supprime le premier nœud contenant la chaîne s, s'il existe"""
        if premier is None:
            return premier, dernier  # Liste vide

        # Si la chaîne est dans le premier nœud
        if premier.info == s:
            if premier == dernier:  # Un seul nœud
                premier = None
                dernier = None
            else:
                premier = premier.suivant
                premier.precedent = None
            return premier, dernier

        # Recherche du nœud
        courant = premier
        while courant is not None and courant.info != s:
            courant = courant.suivant

        # Si le nœud a été trouvé
        if courant is not None:
            # Si c'est le dernier nœud
            if courant == dernier:
                dernier = courant.precedent
                dernier.suivant = None
            else:
                courant.precedent.suivant = courant.suivant
                courant.suivant.precedent = courant.precedent

        return premier, dernier

    @staticmethod
    def afficher(premier):
        """Affiche tous les éléments de la liste"""
        courant = premier
        if courant is None:
            print("La liste est vide.")
            return

        while courant is not None:
            print(courant.info)
            courant = courant.suivant

    @staticmethod
    def afficher_inverse(dernier):
        """Affiche tous les éléments de la liste en ordre inverse"""
        courant = dernier
        if courant is None:
            print("La liste est vide.")
            return

        while courant is not None:
            print(courant.info)
            courant = courant.precedent