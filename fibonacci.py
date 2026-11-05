# fichier fibonacci.py
# module fibonacci

def fibo(n: int) -> tuple[int, int]:
    """Retourne le couple (F(n), F(n+1)) de la suite de Fibonacci."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a, b
