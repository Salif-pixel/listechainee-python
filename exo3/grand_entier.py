class GrandInt:
    def __init__(self, chiffre, suite=None):
        """
        Construit un grand entier
        :param chiffre: chiffre courant (0-9)
        :param suite: GrandInt représentant les chiffres plus significatifs
        """
        self.chiffre = chiffre
        self.suite = suite

    @classmethod
    def from_int(cls, nombre):
        """Convertit un entier en GrandInt"""
        if nombre == 0:
            return cls(0)

        digits = []
        while nombre > 0:
            digits.append(nombre % 10)
            nombre = nombre // 10

        grand_int = None
        for d in digits:
            grand_int = cls(d, grand_int)

        return grand_int

    def nombre_de_chiffres(self):
        """Retourne le nombre de chiffres"""
        if self.suite is None:
            return 1
        return 1 + self.suite.nombre_de_chiffres()

    def __str__(self):
        if self.suite is None:
            return str(self.chiffre)
        return f"{self.suite}{self.chiffre}"