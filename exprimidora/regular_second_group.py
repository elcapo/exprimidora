from exprimidora.irregular_to_have import IrregularToHave
from exprimidora.verb import Verb

class RegularSecondGroup(Verb):
    def __init__(self, infinitive: str):
        if len(infinitive) <= 2:
            raise Exception("Invalid regular verb of the second group as it's length only two characters")
        if not infinitive[-2:] == "er":
            raise Exception("Invalid regular verb of the second group as it does not terminate in: -er")
        
        self.to_have = IrregularToHave()
        self.infinitive = infinitive
    
    def gerund(self) -> str:
        return self.suffixed("iendo")

    def participle(self) -> str:
        return self.suffixed("ido")

    def indicative_present(self) -> dict:
        return self.personal_conjugation(["o", "es", "és", "e", "emos", "éis", "en"])

    def indicative_imperfect(self) -> dict:
        return self.personal_conjugation(["ía", "ías", "ías", "ía", "íamos", "íais", "ían"])

    def indicative_preterite(self) -> dict:
        return self.personal_conjugation(["í", "iste", "iste", "ió", "imos", "isteis", "ieron"])

    def indicative_future(self) -> dict:
        return self.personal_conjugation(["eré", "erás", "erás", "erá", "eremos", "eréis", "erán"])

    def indicative_conditional(self) -> dict:
        return self.personal_conjugation(["ería", "erías", "erías", "ería", "eríamos", "eríais", "erían"])

    def subjunctive_present(self) -> dict:
        return self.personal_conjugation(["a", "as", "ás", "a", "amos", "áis", "an"])

    def subjunctive_imperfect_preterite(self, alternate_form: bool = False) -> dict:
        if not alternate_form:
            return self.personal_conjugation(["iera", "ieras", "ieras", "iera", "iéramos", "ierais", "ieran"])
        else:
            return self.personal_conjugation(["iese", "ieses", "ieses", "iese", "iésemos", "ieseis", "iesen"])

    def subjunctive_future(self) -> dict:
        return self.personal_conjugation(["iere", "ieres", "ieres", "iere", "iéremos", "iereis", "ieren"])

    def imperative_affirmative(self) -> dict:
        return self.imperative_conjugation(["e", "é", "a", "amos", "ed", "an"])

    def imperative_negative(self) -> dict:
        return self.imperative_conjugation(["as", "ás", "a", "amos", "áis", "an"])
