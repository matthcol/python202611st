# module city

from dataclasses import dataclass

# Nb: redaction moderne d'une classe
#  - @dataclass (inclus dans Python)
#  - pydantic (lib tierce) : + value validation serialization

@dataclass
class CityFr:
    """represents a french City with its name, population and zipcode
    
    Example:

        city = CityFr("Marseille", 500_000, "13000")
    """

    name: str
    population: int
    zipcode: str