class Maillon:
    def __init__(self, mot=None):
        self.mot = mot
        self.suiv = None

    @staticmethod
    def ajoute_debut(mot, L):
        """Ajoute un mot au début de la liste chaînée"""
        nouveau = Maillon(mot)
        nouveau.suiv = L
        return nouveau

    @staticmethod
    def ajoute_fin(mot, L):
        """Ajoute un mot à la fin de la liste chaînée"""
        nouveau = Maillon(mot)
        if L is None:
            return nouveau

        courant = L
        while courant.suiv is not None:
            courant = courant.suiv

        courant.suiv = nouveau
        return L

    @staticmethod
    def supprimer(mot, L):
        """Supprime le nœud contenant le mot donné"""
        if L is None:
            return None

        # Si le mot est dans le premier nœud
        if L.mot == mot:
            return L.suiv

        courant = L
        while courant.suiv is not None and courant.suiv.mot != mot:
            courant = courant.suiv

        # Si le mot a été trouvé
        if courant.suiv is not None:
            courant.suiv = courant.suiv.suiv

        return L

    @staticmethod
    def premiers(liste, n):
        """Affiche les n premiers mots de la liste"""
        count = 0
        courant = liste
        while courant is not None and count < n:
            print(courant.mot)
            courant = courant.suiv
            count += 1

    @staticmethod
    def purifie(liste):
        """Supprime les doublons d'une liste chaînée triée"""
        if liste is None or liste.suiv is None:
            return

        courant = liste
        while courant is not None and courant.suiv is not None:
            if courant.mot == courant.suiv.mot:
                courant.suiv = courant.suiv.suiv
            else:
                courant = courant.suiv


# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une liste avec quelques mots
    L = None
    words = ["apple", "banana", "cherry", "apple", "date"]
    for word in words:
        L = Maillon.ajoute_debut(word, L)

    print("Liste originale:")
    Maillon.premiers(L, 10)

    print("\nAprès suppression de 'cherry':")
    L = Maillon.supprimer("cherry", L)
    Maillon.premiers(L, 10)

    # Ajout d'un mot à la fin
    L = Maillon.ajoute_fin("fig", L)
    print("\nAprès ajout de 'fig' à la fin:")
    Maillon.premiers(L, 10)

    # Tri de la liste (pour la fonction purifie)
    # Dans un scénario réel, vous implémenteriez une fonction de tri appropriée
    sorted_words = sorted(words + ["fig"])
    sorted_L = None
    for word in sorted_words:
        sorted_L = Maillon.ajoute_fin(word, sorted_L)

    print("\nListe triée avec doublons:")
    Maillon.premiers(sorted_L, 10)

    Maillon.purifie(sorted_L)
    print("\nAprès suppression des doublons:")
    Maillon.premiers(sorted_L, 10)