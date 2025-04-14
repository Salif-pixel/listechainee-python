class Liste:
    def __init__(self, valeur, suite=None):
        self.valeur = valeur
        self.suite = suite

    def append(self, l):
        """Ajoute la liste l à la fin de la liste courante"""
        if self.suite is None:
            self.suite = l
        else:
            self.suite.append(l)

    def separer(self):
        """Sépare la liste en éléments inférieurs et supérieurs/égaux au pivot (premier élément)"""
        if self.suite is None:
            return None, None

        pivot = self.valeur
        inferieurs = None
        superieurs = None
        courant = self.suite

        while courant is not None:
            if courant.valeur < pivot:
                if inferieurs is None:
                    inferieurs = Liste(courant.valeur)
                else:
                    inferieurs.append(Liste(courant.valeur))
            else:
                if superieurs is None:
                    superieurs = Liste(courant.valeur)
                else:
                    superieurs.append(Liste(courant.valeur))
            courant = courant.suite

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
            # Trouver la fin de la liste inferieurs
            dernier_inf = inferieurs
            while dernier_inf.suite is not None:
                dernier_inf = dernier_inf.suite
            dernier_inf.suite = result
        else:
            inferieurs = result

        if superieurs is not None:
            result.suite = superieurs

        return inferieurs if inferieurs is not None else result

    def __str__(self):
        return f"{self.valeur} -> {self.suite}" if self.suite else str(self.valeur)


