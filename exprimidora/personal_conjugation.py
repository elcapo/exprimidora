from collections.abc import Callable

class PersonalConjugation:
    def __init__(self, suffixer: Callable[[str], str]):
        self.suffixer = suffixer
    
    def conjugate(self, suffixes: list) -> dict:
        self.yo = self.suffixer(suffixes[0])
        self.tu = self.suffixer(suffixes[1])
        self.vos = self.suffixer(suffixes[2])
        self.usted = self.suffixer(suffixes[3])
        self.el = self.suffixer(suffixes[3])
        self.ella = self.suffixer(suffixes[3])
        self.nosotros = self.suffixer(suffixes[4])
        self.nosotras = self.suffixer(suffixes[4])
        self.vosotros = self.suffixer(suffixes[5])
        self.vosotras = self.suffixer(suffixes[5])
        self.ustedes = self.suffixer(suffixes[6])
        self.ellos = self.suffixer(suffixes[6])
        self.ellas = self.suffixer(suffixes[6])
        return self.to_dict()

    def to_dict(self) -> dict:
        return {
            "yo": self.yo,
            "tú": self.tu,
            "vos": self.vos,
            "usted": self.usted,
            "él": self.el,
            "ella": self.ella,
            "nosotros": self.nosotros,
            "nosotras": self.nosotras,
            "vosotros": self.vosotros,
            "vosotras": self.vosotras,
            "ustedes": self.ustedes,
            "ellos": self.ellos,
            "ellas": self.ellas,
        }