from exprimidora.irregular_to_have import IrregularToHave
from exprimidora.verb import Verb
from typing import Union

class RegularThirdGroup(Verb):
    def __init__(self, infinitive: str):
        if len(infinitive) <= 2:
            raise Exception("Invalid regular verb of the third group as it's length only two characters")
        if not infinitive[-2:] == "ir":
            raise Exception("Invalid regular verb of the third group as it does not terminate in: -ir")

        self.to_have = IrregularToHave()
        self.infinitive = infinitive

    def gerund(self) -> str:
        return self.suffixed("iendo")

    def participle(self) -> str:
        return self.suffixed("ido")

    def indicative_present(self, person: str = None) -> Union[dict, str]:
        return self.personal_conjugation(["o", "es", "ís", "e", "imos", "ís", "en"], person)

    def indicative_imperfect(self, person: str = None) -> Union[dict, str]:
        return self.personal_conjugation(["ía", "ías", "ías", "ía", "íamos", "íais", "ían"], person)

    def indicative_preterite(self, person: str = None) -> Union[dict, str]:
        return self.personal_conjugation(["í", "iste", "iste", "ió", "imos", "isteis", "ieron"], person)

    def indicative_future(self, person: str = None) -> Union[dict, str]:
        return self.personal_conjugation(["iré", "irás", "irás", "irá", "iremos", "iréis", "irán"], person)

    def indicative_conditional(self, person: str = None) -> Union[dict, str]:
        return self.personal_conjugation(["iría", "irías", "irías", "iría", "iríamos", "iríais", "irían"], person)

    def subjunctive_present(self, person: str = None) -> Union[dict, str]:
        return self.personal_conjugation(["a", "as", "ás", "a", "amos", "áis", "an"], person)

    def subjunctive_imperfect_preterite(self, person: str = None, alternate_form: bool = False) -> Union[dict, str]:
        if not alternate_form:
            return self.personal_conjugation(["iera", "ieras", "ieras", "iera", "iéramos", "ierais", "ieran"], person)
        else:
            return self.personal_conjugation(["iese", "ieses", "ieses", "iese", "iésemos", "ieseis", "iesen"], person)

    def subjunctive_future(self, person: str = None) -> Union[dict, str]:
        return self.personal_conjugation(["iere", "ieres", "ieres", "iere", "iéremos", "iereis", "ieren"], person)

    def imperative_affirmative(self, person: str = None) -> Union[dict, str]:
        return self.imperative_conjugation(["e", "í", "a", "amos", "id", "an"], person)

    def imperative_negative(self, person: str = None) -> Union[dict, str]:
        return self.imperative_conjugation(["as", "ás", "a", "amos", "áis", "an"], person)
