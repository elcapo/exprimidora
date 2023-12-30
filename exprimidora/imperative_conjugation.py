from collections.abc import Callable

class ImperativeConjugation:
    def __init__(self, suffixer: Callable[[str], str]):
        self.suffixer = suffixer
    
    def conjugate(self, suffixes: list) -> dict:
        self.tu = self.suffixer(suffixes[0])
        self.vos = self.suffixer(suffixes[1])
        self.usted = self.suffixer(suffixes[2])
        self.nosotros = self.suffixer(suffixes[3])
        self.nosotras = self.suffixer(suffixes[3])
        self.vosotros = self.suffixer(suffixes[4])
        self.vosotras = self.suffixer(suffixes[4])
        self.ustedes = self.suffixer(suffixes[5])
        return self.to_dict()

    def to_dict(self) -> dict:
        return {
            "tú": self.tu,
            "vos": self.vos,
            "usted": self.usted,
            "nosotros": self.nosotros,
            "nosotras": self.nosotras,
            "vosotros": self.vosotros,
            "vosotras": self.vosotras,
            "ustedes": self.ustedes,
        }
