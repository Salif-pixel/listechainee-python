import numpy as np

NMAX = 100  # Maximum matrix size


class MatCarree:
    def __init__(self, n):
        """Create a square matrix of size n"""
        self.n = n
        self.data = np.zeros((n, n))

    @staticmethod
    def symetrique(m):
        """Check if a matrix is symmetric"""
        n = m.n
        for i in range(n):
            for j in range(i + 1, n):  # Only check upper triangle
                if m.data[i][j] != m.data[j][i]:
                    return False
        return True

    @staticmethod
    def sym_compacte(m, n):
        """Create a compact representation of a symmetric matrix"""
        if not MatCarree.symetrique(m):
            return None

        # Calculate the size of the compact representation
        size = n * (n + 1) // 2
        compact = np.zeros(size)

        k = 0
        for i in range(n):
            for j in range(i, n):  # Store only lower triangle (including diagonal)
                compact[k] = m.data[i][j]
                k += 1

        return compact

    @staticmethod
    def acces(c, i, j, n):
        """Access element (i,j) in a compact symmetric matrix"""
        # Ensure i <= j (swap if needed)
        if i > j:
            i, j = j, i

        # Calculate the index in the compact array
        idx = (i * (2 * n - i + 1)) // 2 + (j - i)
        return c[idx]

    @staticmethod
    def traiter_coef(x):
        """Example function to process a coefficient"""
        print(f"{x:.2f}", end=" ")

    @staticmethod
    def traiter_ligne(c, n, i):
        """Process row i of the compact matrix"""
        print(f"Row {i}: ", end="")
        for j in range(n):
            MatCarree.traiter_coef(MatCarree.acces(c, i, j, n))
        print()

    @staticmethod
    def afficher(c, n):
        """Display the symmetric matrix in its normal form"""
        print("Matrix:")
        for i in range(n):
            MatCarree.traiter_ligne(c, n, i)