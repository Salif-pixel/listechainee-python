class Liste:
    """
    Classe représentant une liste chaînée non vide.
    """

    def __init__(self, valeur, suite=None):
        """
        Constructeur de la classe Liste.

        Args:
            valeur (str): La valeur à stocker dans le maillon
            suite (Liste, optional): Le reste de la liste. Par défaut None.
        """
        self.valeur = valeur
        self.suite = suite

    def __str__(self):
        """Affichage de la liste sous forme de chaîne de caractères."""
        elements = []
        current = self
        while current is not None:
            elements.append(current.valeur)
            current = current.suite
        return " -> ".join(elements)

    def append(self, l):
        """
        Ajoute la liste passée en argument à la fin de la liste actuelle.

        Args:
            l (Liste): La liste à ajouter à la fin
        """
        current = self
        # On parcourt la liste jusqu'au dernier élément
        while current.suite is not None:
            current = current.suite
        # On ajoute la liste l à la fin
        current.suite = l

    def suprimerInferieur(self):
        """
        Supprime les maillons dont la valeur est inférieure à celle du premier maillon
        et renvoie une liste constituée des maillons supprimés.

        Returns:
            Liste: Une liste contenant les maillons supprimés
        """
        if self is None:
            return None

        # Conversion en numérique pour la comparaison si possible
        try:
            pivot_num = float(self.valeur)
            compare_numerically = True
        except ValueError:
            pivot_num = self.valeur
            compare_numerically = False

        elements_inferieurs = None
        current = self

        # On parcourt la liste pour trouver les éléments inférieurs au pivot
        while current is not None and current.suite is not None:
            inferieur = False

            if compare_numerically:
                try:
                    val_courante = float(current.suite.valeur)
                    inferieur = val_courante < pivot_num
                except ValueError:
                    # Si conversion impossible, on compare lexicographiquement
                    inferieur = current.suite.valeur < self.valeur
            else:
                inferieur = current.suite.valeur < self.valeur

            if inferieur:
                # On détache le maillon inférieur
                maillon_inferieur = current.suite
                current.suite = maillon_inferieur.suite

                # On ajoute le maillon détaché à la liste des éléments inférieurs
                maillon_inferieur.suite = elements_inferieurs
                elements_inferieurs = maillon_inferieur
            else:
                current = current.suite

        return elements_inferieurs

    def quicksort(self):
        """
        Trie la liste chaînée avec l'algorithme quicksort.

        Returns:
            Liste: La liste triée
        """
        # Cas de base: liste vide ou avec un seul élément
        if self is None or self.suite is None:
            return self

        # Détermine si on peut comparer numériquement
        try:
            pivot_num = float(self.valeur)
            compare_numerically = True
        except ValueError:
            pivot_num = self.valeur
            compare_numerically = False

        # On crée une liste pour les éléments inférieurs au pivot
        liste_inf = None
        # On crée une liste pour les éléments supérieurs ou égaux au pivot
        liste_sup = None

        # On parcourt la liste (à partir du deuxième élément)
        current = self.suite
        while current is not None:
            # On sauvegarde le maillon suivant
            suivant = current.suite

            inferieur = False
            if compare_numerically:
                try:
                    val_courante = float(current.valeur)
                    inferieur = val_courante < pivot_num
                except ValueError:
                    # Si conversion impossible, on compare lexicographiquement
                    inferieur = current.valeur < self.valeur
            else:
                inferieur = current.valeur < self.valeur

            if inferieur:
                # Si la valeur est inférieure au pivot, on l'ajoute à liste_inf
                current.suite = liste_inf
                liste_inf = current
            else:
                # Si la valeur est supérieure ou égale au pivot, on l'ajoute à liste_sup
                current.suite = liste_sup
                liste_sup = current

            # On passe au maillon suivant
            current = suivant

        # On trie récursivement les deux sous-listes
        if liste_inf is not None:
            liste_inf = liste_inf.quicksort()

        if liste_sup is not None:
            liste_sup = liste_sup.quicksort()

        # On crée une liste résultat en concaténant liste_inf + pivot + liste_sup
        resultat = Liste(self.valeur)

        # Étape 1: Si liste_inf n'est pas vide, on la place au début
        if liste_inf is not None:
            temp = liste_inf
            resultat = temp

            # On va à la fin de liste_inf
            while temp.suite is not None:
                temp = temp.suite

            # On ajoute le pivot à la fin de liste_inf
            temp.suite = Liste(self.valeur)
            temp = temp.suite
        else:
            # Si pas d'éléments inférieurs, on commence par le pivot
            temp = resultat

        # Étape 2: On ajoute liste_sup à la fin
        if liste_sup is not None:
            temp.suite = liste_sup

        return resultat