# fichier euclide.py
# module euclide

def gcd(a: int, b: int) -> int:
    if a <= 0 or b <= 0:
        raise ValueError("argument <= 0")
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a