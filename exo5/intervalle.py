class Intervalle:
    """Classe de base pour les intervalles"""

    def __init__(self, b_inf, b_sup):
        if b_inf > b_sup:
            raise ValueError("La borne inférieure doit être <= à la borne supérieure")
        self.b_inf = b_inf
        self.b_sup = b_sup

    def est_vide(self):
        return self.b_inf > self.b_sup or (
                self.b_inf == self.b_sup and not (self.est_dans(self.b_inf)))

    def contient(self, other):
        return (self.b_inf <= other.b_inf and
                self.b_sup >= other.b_sup and
                (not isinstance(other, IntervFerme) or
                 (isinstance(self, IntervFerme) or self.est_dans(other.b_inf))) and
                (not isinstance(other, IntervFerme) or
                 (isinstance(self, IntervFerme) or self.est_dans(other.b_sup))))

    def intersection(self, other):
        new_inf = max(self.b_inf, other.b_inf)
        new_sup = min(self.b_sup, other.b_sup)

        if new_inf > new_sup:
            return IntervOuvert(new_inf, new_sup)  # intervalle vide

        # Déterminer le type des bornes
        inf_inclus = self.est_dans(new_inf) and other.est_dans(new_inf)
        sup_inclus = self.est_dans(new_sup) and other.est_dans(new_sup)

        if inf_inclus and sup_inclus:
            return IntervFerme(new_inf, new_sup)
        elif inf_inclus:
            return IntervFermeGauche(new_inf, new_sup)
        elif sup_inclus:
            return IntervFermeDroit(new_inf, new_sup)
        else:
            return IntervOuvert(new_inf, new_sup)

    def __str__(self):
        raise NotImplementedError


class IntervOuvert(Intervalle):
    """Intervalle ouvert ]a, b["""

    def __init__(self, b_inf, b_sup):
        super().__init__(b_inf, b_sup)
        self.card = max(0, b_sup - b_inf - 1)

    def est_dans(self, n):
        return self.b_inf < n < self.b_sup

    def __str__(self):
        return f"]{self.b_inf}, {self.b_sup}["


class IntervFerme(Intervalle):
    """Intervalle fermé [a, b]"""

    def __init__(self, b_inf, b_sup):
        super().__init__(b_inf, b_sup)
        self.card = max(0, b_sup - b_inf + 1)

    def est_dans(self, n):
        return self.b_inf <= n <= self.b_sup

    def __str__(self):
        return f"[{self.b_inf}, {self.b_sup}]"


class IntervFermeGauche(Intervalle):
    """Intervalle fermé à gauche [a, b["""

    def __init__(self, b_inf, b_sup):
        super().__init__(b_inf, b_sup)
        self.card = max(0, b_sup - b_inf)

    def est_dans(self, n):
        return self.b_inf <= n < self.b_sup

    def __str__(self):
        return f"[{self.b_inf}, {self.b_sup}["


class IntervFermeDroit(Intervalle):
    """Intervalle fermé à droite ]a, b]"""

    def __init__(self, b_inf, b_sup):
        super().__init__(b_inf, b_sup)
        self.card = max(0, b_sup - b_inf)

    def est_dans(self, n):
        return self.b_inf < n <= self.b_sup

    def __str__(self):
        return f"]{self.b_inf}, {self.b_sup}]"