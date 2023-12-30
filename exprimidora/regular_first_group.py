from exprimidora import IrregularToHave
from exprimidora.verb import Verb

class RegularFirstGroup(Verb):
    def __init__(self, infinitive: str):
        if len(infinitive) <= 2:
            raise Exception("Invalid regular verb of the first group as it's length only two characters")
        if not infinitive[-2:] == "ar":
            raise Exception("Invalid regular verb of the first group as it does not terminate in: -ar")
        self.infinitive = infinitive
        self.to_have = IrregularToHave()
   
    def gerund(self) -> str:
        return self.suffixed("ando")

    def participle(self) -> str:
        return self.suffixed("ado")

    def indicative_present(self) -> dict:
        return self.personal_conjugation(["o", "as", "ás", "a", "amos", "áis", "an"])

    def indicative_imperfect(self) -> dict:
        return self.personal_conjugation(["aba", "abas", "abas", "aba", "ábamos", "abais", "aban"])

    def indicative_preterite(self) -> dict:
        return self.personal_conjugation(["é", "aste", "aste", "ó", "amos", "asteis", "aron"])

    def indicative_future(self) -> dict:
        return self.personal_conjugation(["aré", "arás", "arás", "ará", "aremos", "aréis", "arán"])

    def indicative_conditional(self) -> dict:
        return self.personal_conjugation(["aría", "arías", "arías", "aría", "aríamos", "aríais", "arían"])

    def subjunctive_present(self) -> dict:
        return self.personal_conjugation(["e", "es", "és", "e", "emos", "éis", "en"])

    def subjunctive_imperfect_preterite(self, alternate_form: bool = False) -> dict:
        if not alternate_form:
            return self.personal_conjugation(["ara", "aras", "aras", "ara", "áramos", "arais", "aran"])
        else:
            return self.personal_conjugation(["ase", "ases", "ases", "ase", "ásemos", "aseis", "asen"])

    def subjunctive_future(self) -> dict:
        return self.personal_conjugation(["are", "ares", "ares", "are", "áremos", "areis", "aren"])

    def imperative_affirmative(self) -> dict:
        return self.imperative_conjugation(["a", "á", "e", "emos", "ad", "en"])

    def imperative_negative(self) -> dict:
        return self.imperative_conjugation(["es", "és", "e", "emos", "éis", "en"])
