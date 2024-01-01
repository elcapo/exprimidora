from exprimidora.irregular_to_have import IrregularToHave
from exprimidora.verb import Verb
from typing import Union

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

    def indicative_present(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["o", "es", "és", "e", "emos", "éis", "en"], person)

    def indicative_imperfect(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["ía", "ías", "ías", "ía", "íamos", "íais", "ían"], person)

    def indicative_preterite(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["í", "iste", "iste", "ió", "imos", "isteis", "ieron"], person)

    def indicative_future(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["eré", "erás", "erás", "erá", "eremos", "eréis", "erán"], person)

    def indicative_conditional(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["ería", "erías", "erías", "ería", "eríamos", "eríais", "erían"], person)

    def subjunctive_present(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["a", "as", "ás", "a", "amos", "áis", "an"], person)

    def subjunctive_imperfect_preterite(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["iera", "ieras", "ieras", "iera", "iéramos", "ierais", "ieran"], person)

    def subjunctive_imperfect_preterite_alternate(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["iese", "ieses", "ieses", "iese", "iésemos", "ieseis", "iesen"], person)

    def subjunctive_future(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["iere", "ieres", "ieres", "iere", "iéremos", "iereis", "ieren"], person)

    def imperative_affirmative(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_imperative(["e", "é", "a", "amos", "ed", "an"], person)

    def imperative_negative(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_imperative(["as", "ás", "a", "amos", "áis", "an"], person)
