class NoeudABR:
    def __init__(self, nom):
        self.nom = nom
        self.gauche = None
        self.droite = None
        self.numeros = ListeCB()  # Liste chaînée bidirectionnelle


class ListeCB:
    def __init__(self):
        self.tete = None
        self.queue = None


class NoeudNumero:
    def __init__(self, numero):
        self.numero = numero
        self.prec = None
        self.suiv = None


class IndexABR:
    @staticmethod
    def ajout_numero(numero, lcb):
        """Add a page number to the doubly linked list"""
        nouveau = NoeudNumero(numero)

        if lcb.tete is None:
            lcb.tete = nouveau
            lcb.queue = nouveau
        else:
            nouveau.prec = lcb.queue
            lcb.queue.suiv = nouveau
            lcb.queue = nouveau

        return lcb

    @staticmethod
    def ajout_nompropre(nom, t, nombre, a):
        """Insert a new name and its page numbers into the ABR"""
        if a is None:
            a = NoeudABR(nom)
            for i in range(nombre):
                a.numeros = IndexABR.ajout_numero(t[i], a.numeros)
            return a

        if nom < a.nom:
            a.gauche = IndexABR.ajout_nompropre(nom, t, nombre, a.gauche)
        elif nom > a.nom:
            a.droite = IndexABR.ajout_nompropre(nom, t, nombre, a.droite)
        else:
            for i in range(nombre):
                a.numeros = IndexABR.ajout_numero(t[i], a.numeros)

        return a

    @staticmethod
    def supprimer_numero(nom, numero, a):
        """Remove a page number for a given name"""
        if a is None:
            return None

        if nom < a.nom:
            a.gauche = IndexABR.supprimer_numero(nom, numero, a.gauche)
        elif nom > a.nom:
            a.droite = IndexABR.supprimer_numero(nom, numero, a.droite)
        else:
            lcb = a.numeros

            if lcb.tete is None:
                return a

            if lcb.tete.numero == numero:
                if lcb.tete == lcb.queue:
                    lcb.tete = None
                    lcb.queue = None
                else:
                    lcb.tete = lcb.tete.suiv
                    lcb.tete.prec = None
                return a

            if lcb.queue.numero == numero:
                lcb.queue = lcb.queue.prec
                lcb.queue.suiv = None
                return a

            courant = lcb.tete
            while courant is not None and courant.numero != numero:
                courant = courant.suiv

            if courant is not None:
                courant.prec.suiv = courant.suiv
                if courant.suiv is not None:
                    courant.suiv.prec = courant.prec

        return a

    @staticmethod
    def afficher_index(a):
        """Display the index in alphabetical order"""
        if a is None:
            return

        IndexABR.afficher_index(a.gauche)

        print(f"{a.nom}: ", end="")
        courant = a.numeros.tete
        while courant is not None:
            print(courant.numero, end="")
            if courant.suiv is not None:
                print(", ", end="")
            courant = courant.suiv
        print()

        IndexABR.afficher_index(a.droite)

    @staticmethod
    def equilibrer_abr(a):
        """Balance the ABR"""
        nodes = []

        def collect_nodes(node):
            if node is None:
                return
            collect_nodes(node.gauche)
            nodes.append(node)
            collect_nodes(node.droite)

        collect_nodes(a)

        def build_balanced(start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            root = nodes[mid]

            root.gauche = build_balanced(start, mid - 1)
            root.droite = build_balanced(mid + 1, end)

            return root

        if not nodes:
            return None

        return build_balanced(0, len(nodes) - 1)