class IntervOuvert:
    def __init__(self, b_inf, b_sup):
        self.b_inf = b_inf
        self.b_sup = b_sup
        self.card = max(0, b_sup - b_inf - 1)

    def est_vide(self):
        return self.b_inf >= self.b_sup - 1

    def est_dans(self, n):
        return self.b_inf < n < self.b_sup

    def contient(self, other):
        return self.b_inf <= other.b_inf and self.b_sup >= other.b_sup

    def intersection(self, other):
        new_inf = max(self.b_inf, other.b_inf)
        new_sup = min(self.b_sup, other.b_sup)
        return IntervOuvert(new_inf, new_sup)

    def __str__(self):
        return f"]{self.b_inf}, {self.b_sup}["


class IntervFerme(IntervOuvert):
    def __init__(self, b_inf, b_sup):
        super().__init__(b_inf, b_sup)
        self.card = max(0, b_sup - b_inf + 1)

    def est_dans(self, n):
        return self.b_inf <= n <= self.b_sup

    def __str__(self):
        return f"[{self.b_inf}, {self.b_sup}]"