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

    def supprimer_inferieurs(self):
        """Supprime les éléments inférieurs au premier et retourne une nouvelle liste"""
        if self.suite is None:
            return None

        courant = self
        result = None
        precedent = None

        while courant is not None:
            if courant.valeur < self.valeur:
                if precedent is not None:
                    precedent.suite = courant.suite
                if result is None:
                    result = Liste(courant.valeur)
                else:
                    result.append(Liste(courant.valeur))
            else:
                precedent = courant
            courant = courant.suite

        return result

    def quicksort(self):
        """Tri rapide de la liste chaînée"""
        if self.suite is None:
            return self

        p = self.valeur
        inferieurs = Liste.supprimer_inferieurs(self)
        superieurs = self.suite

        if inferieurs is not None:
            inferieurs = inferieurs.quicksort()
        if superieurs is not None:
            superieurs = superieurs.quicksort()

        if inferieurs is not None:
            inferieurs.append(Liste(p))
            if superieurs is not None:
                inferieurs.append(superieurs)
            return inferieurs
        else:
            new_list = Liste(p)
            if superieurs is not None:
                new_list.append(superieurs)
            return new_list

    def __str__(self):
        return f"{self.valeur} -> {self.suite}" if self.suite else str(self.valeur)