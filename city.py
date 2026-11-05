# module city

from dataclasses import dataclass

# Nb: redaction moderne d'une classe
#  - @dataclass (inclus dans Python)
#  - pydantic (lib tierce) : + value validation serialization

@dataclass
class CityFr:
    """represents a french City with its name, population and zipcode
        
    Example:

        city = CityFr("Marseille", 886_040, "13000")
    """

    # properties
    name: str
    population: int
    zipcode: str

    # personnalisation de la builtin str
    # par défaut : __repr__ = __str__
    def __str__(self) -> str:
        return f"{self.name} ({self.zipcode})"

    # surcharge d'opérateur +=, -=
    # def __iadd__(self, other: int) -> CityFr:   # python 3.14+
    def __iadd__(self, other: int) -> 'CityFr': # python <3.14
        self.population += other
        return self


    def department(self) -> str:
        match self.zipcode[:2]: 
            case "20" if int(self.zipcode) < 20200:
                # Corse du Sud
                return "2A"
            case "20":
                # Haute-Corse
                return "2B"
            case "97" | "98":
                # DOM/TOM : departement sur 3 chiffres
                return self.zipcode[:3]
            case _:
                return self.zipcode[:2]