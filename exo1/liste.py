class Liste:
    def __init__(self, valeur, suite=None):
        self.valeur = valeur
        self.suite = suite

    def append(self, valeur):
        """Ajoute une valeur à la fin de la liste"""
        if self.suite is None:
            self.suite = Liste(valeur)
        else:
            self.suite.append(valeur)

    def separer(self):
        """Sépare la liste en éléments inférieurs et supérieurs/égaux au pivot (premier élément)"""
        if self.suite is None:
            return None, None

        try:
            pivot = float(self.valeur)  # Conversion en nombre pour comparaison
        except ValueError:
            pivot = self.valeur  # Si conversion échoue, compare comme string

        inferieurs = None
        dernier_inf = None
        superieurs = None
        dernier_sup = None
        courant = self.suite

        while courant is not None:
            suivant = courant.suite
            courant.suite = None

            try:
                val_courant = float(courant.valeur)
            except ValueError:
                val_courant = courant.valeur

            if val_courant < pivot:
                if inferieurs is None:
                    inferieurs = courant
                    dernier_inf = courant
                else:
                    dernier_inf.suite = courant
                    dernier_inf = courant
            else:
                if superieurs is None:
                    superieurs = courant
                    dernier_sup = courant
                else:
                    dernier_sup.suite = courant
                    dernier_sup = courant

            courant = suivant

        return inferieurs, superieurs

    def quicksort(self):
        """Tri rapide de la liste chaînée"""
        if self.suite is None:
            return self

        inferieurs, superieurs = self.separer()

        # Trier les sous-listes
        if inferieurs is not None:
            inferieurs = inferieurs.quicksort()
        if superieurs is not None:
            superieurs = superieurs.quicksort()

        # Reconstruire la liste triée
        result = Liste(self.valeur)
        if inferieurs is not None:
            dernier_inf = inferieurs
            while dernier_inf.suite is not None:
                dernier_inf = dernier_inf.suite
            dernier_inf.suite = result
        else:
            inferieurs = result

        result.suite = superieurs

        return inferieurs if inferieurs is not None else result

    def __str__(self):
        return f"{self.valeur} -> {self.suite}" if self.suite else str(self.valeur)