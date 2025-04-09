class ArbreBin:
    def __init__(self, etiquette=None):
        self.etiquette = etiquette
        self.gauche = None
        self.droite = None

    @staticmethod
    def feuille(A):
        """Print the labels of all leaves, starting from the leftmost leaf"""
        if A is None:
            return

        if A.gauche is None and A.droite is None:
            print(A.etiquette, end=" ")

        ArbreBin.feuille(A.gauche)
        ArbreBin.feuille(A.droite)

    @staticmethod
    def degre(A):
        """Print all nodes with their respective degrees"""
        if A is None:
            return

        deg = 0
        if A.gauche is not None:
            deg += 1
        if A.droite is not None:
            deg += 1

        print(f"Node {A.etiquette} has degree {deg}")

        ArbreBin.degre(A.gauche)
        ArbreBin.degre(A.droite)

    @staticmethod
    def profondeur(A, x, level=0, path=None):
        """Find and print the depth of node x"""
        if path is None:
            path = []

        if A is None:
            return False

        path.append(A.etiquette)

        if A.etiquette == x:
            print(f"Node {x} has depth {level}")
            print(f"Path: {' -> '.join(map(str, path))}")
            return True

        if ArbreBin.profondeur(A.gauche, x, level + 1, path.copy()):
            return True
        if ArbreBin.profondeur(A.droite, x, level + 1, path.copy()):
            return True

        return False

    @staticmethod
    def hauteur(A):
        """Return the height of the tree"""
        if A is None:
            return -1

        hauteur_gauche = ArbreBin.hauteur(A.gauche)
        hauteur_droite = ArbreBin.hauteur(A.droite)

        return 1 + max(hauteur_gauche, hauteur_droite)

    @staticmethod
    def som_noeuds(A):
        """Calculate and return the sum of all node values"""
        if A is None:
            return 0

        return A.etiquette + ArbreBin.som_noeuds(A.gauche) + ArbreBin.som_noeuds(A.droite)