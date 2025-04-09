class Polynome:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = []
        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(coeff1 + coeff2)
        return Polynome(new_coeffs)

    def derivee(self):
        if len(self.coefficients) <= 1:
            return Polynome([0])
        return Polynome([i * self.coefficients[i] for i in range(1, len(self.coefficients))])

    def evaluer(self, x):
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** i)
        return result

    def __str__(self):
        terms = []
        for i, coeff in enumerate(self.coefficients):
            if coeff != 0:
                if i == 0:
                    terms.append(str(coeff))
                elif i == 1:
                    terms.append(f"{coeff}x")
                else:
                    terms.append(f"{coeff}x^{i}")
        return " + ".join(terms) if terms else "0"


class Polynome2(Polynome):
    def resoudre_equation(self):
        if len(self.coefficients) != 3:
            raise ValueError("Le polynôme doit être de degré 2")

        a = self.coefficients[2]
        b = self.coefficients[1]
        c = self.coefficients[0]

        delta = b ** 2 - 4 * a * c

        if delta < 0:
            return "Pas de solution réelle"
        elif delta == 0:
            x = -b / (2 * a)
            return f"Solution double: {x}"
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            return f"Deux solutions: {x1} et {x2}"