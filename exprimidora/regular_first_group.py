from exprimidora.irregular_to_have import IrregularToHave
from exprimidora.verb import Verb
from typing import Union

class RegularFirstGroup(Verb):
    def __init__(self, infinitive: str):
        if len(infinitive) <= 2:
            raise Exception("Invalid regular verb of the first group as it's length only two characters")
        if not infinitive[-2:] == "ar":
            raise Exception("Invalid regular verb of the first group as it does not terminate in: -ar")

        self.to_have = IrregularToHave()
        self.infinitive = infinitive
   
    def gerund(self) -> str:
        return self.suffixed("ando")

    def participle(self) -> str:
        return self.suffixed("ado")

    def indicative_present(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["o", "as", "ás", "a", "amos", "áis", "an"], person)

    def indicative_imperfect(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["aba", "abas", "abas", "aba", "ábamos", "abais", "aban"], person)

    def indicative_preterite(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["é", "aste", "aste", "ó", "amos", "asteis", "aron"], person)

    def indicative_future(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["aré", "arás", "arás", "ará", "aremos", "aréis", "arán"], person)

    def indicative_conditional(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["aría", "arías", "arías", "aría", "aríamos", "aríais", "arían"], person)

    def subjunctive_present(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["e", "es", "és", "e", "emos", "éis", "en"], person)

    def subjunctive_imperfect_preterite(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["ara", "aras", "aras", "ara", "áramos", "arais", "aran"], person)

    def subjunctive_imperfect_preterite_alternate(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["ase", "ases", "ases", "ase", "ásemos", "aseis", "asen"], person)

    def subjunctive_future(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_personal(["are", "ares", "ares", "are", "áremos", "areis", "aren"], person)

    def imperative_affirmative(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_imperative(["a", "á", "e", "emos", "ad", "en"], person)

    def imperative_negative(self, person: str = None) -> Union[dict, str]:
        return self.conjugate_imperative(["es", "és", "e", "emos", "éis", "en"], person)
