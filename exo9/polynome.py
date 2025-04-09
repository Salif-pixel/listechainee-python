class Terme:
    def __init__(self, coefficient=0, exposant=0):
        self.coefficient = coefficient
        self.exposant = exposant
        self.suivant = None


class Polynome:
    def __init__(self):
        self.premier = None

    def ajouter_terme(self, coefficient, exposant):
        """Ajoute un terme au polynôme"""
        if coefficient == 0:
            return  # Ne pas ajouter les coefficients nuls

        nouveau = Terme(coefficient, exposant)

        # Si le polynôme est vide ou si on doit ajouter au début
        if self.premier is None or exposant > self.premier.exposant:
            nouveau.suivant = self.premier
            self.premier = nouveau
            return

        # Trouver où insérer le terme (garder les termes triés par exposant décroissant)
        courant = self.premier
        while courant.suivant is not None and courant.suivant.exposant > exposant:
            courant = courant.suivant

        # S'il y a déjà un terme avec cet exposant, additionner les coefficients
        if courant.suivant is not None and courant.suivant.exposant == exposant:
            courant.suivant.coefficient += coefficient
            # Si le coefficient devient nul, supprimer le terme
            if courant.suivant.coefficient == 0:
                courant.suivant = courant.suivant.suivant
        else:
            nouveau.suivant = courant.suivant
            courant.suivant = nouveau

    def afficher(self):
        """Afficher le polynôme"""
        if self.premier is None:
            print("0")
            return

        courant = self.premier
        first = True

        while courant is not None:
            # Gestion du signe
            if first:
                if courant.coefficient < 0:
                    print("-", end="")
            else:
                print(" + " if courant.coefficient > 0 else " - ", end="")

            # Afficher le coefficient (valeur absolue)
            coef = abs(courant.coefficient)
            if coef != 1 or courant.exposant == 0:
                print(coef, end="")

            # Afficher la variable et l'exposant
            if courant.exposant > 0:
                print("x", end="")
                if courant.exposant > 1:
                    print(f"^{courant.exposant}", end="")

            courant = courant.suivant
            first = False

        print()

    def derivee(self):
        """Calculer la dérivée du polynôme"""
        resultat = Polynome()
        courant = self.premier

        while courant is not None:
            if courant.exposant > 0:  # Les termes avec exposant 0 deviennent 0 dans la dérivée
                nouveau_coefficient = courant.coefficient * courant.exposant
                nouveau_exposant = courant.exposant - 1
                resultat.ajouter_terme(nouveau_coefficient, nouveau_exposant)
            courant = courant.suivant

        return resultat

    def derivee_kieme(self, k):
        """Calculer la k-ième dérivée du polynôme"""
        if k < 0:
            raise ValueError("L'ordre de la dérivée doit être non-négatif")

        if k == 0:
            # Retourner une copie du polynôme
            resultat = Polynome()
            courant = self.premier
            while courant is not None:
                resultat.ajouter_terme(courant.coefficient, courant.exposant)
                courant = courant.suivant
            return resultat

        # Calculer les dérivées récursivement
        resultat = self.derivee()
        for _ in range(1, k):
            resultat = resultat.derivee()

        return resultat