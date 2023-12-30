from exprimidora import IrregularToHave
from exprimidora.personal_conjugation import PersonalConjugation
from exprimidora.imperative_conjugation import ImperativeConjugation

class RegularFirstGroup:
    def __init__(self, infinitive: str):
        if len(infinitive) <= 2:
            raise Exception("Invalid regular verb of the first group as it's length only two characters")
        if not infinitive[-2:] == "ar":
            raise Exception("Invalid regular verb of the first group as it does not terminate in: -ar")
        self.infinitive = infinitive
        self.to_have = IrregularToHave()
        self.personal_conjugation = PersonalConjugation(self.suffixed)
        self.imperative_conjugation = ImperativeConjugation(self.suffixed)

    def root(self) -> str:
        return self.infinitive[:-2]
    
    def suffixed(self, suffix: str) -> str:
        return "{}{}".format(self.root(), suffix)
    
    def gerund(self) -> str:
        return self.suffixed("ando")

    def participle(self) -> str:
        return self.suffixed("ado")

    def indicative_present(self) -> dict:
        return self.personal_conjugation.conjugate(["o", "as", "ás", "a", "amos", "áis", "an"])

    def indicative_imperfect(self) -> dict:
        return self.personal_conjugation.conjugate(["aba", "abas", "abas", "aba", "ábamos", "abais", "aban"])

    def indicative_preterite(self) -> dict:
        return self.personal_conjugation.conjugate(["é", "aste", "aste", "ó", "amos", "asteis", "aron"])

    def indicative_future(self) -> dict:
        return self.personal_conjugation.conjugate(["aré", "arás", "arás", "ará", "aremos", "aréis", "arán"])

    def indicative_conditional(self) -> dict:
        return self.personal_conjugation.conjugate(["aría", "arías", "arías", "aría", "aríamos", "aríais", "arían"])

    def indicative_present_perfect(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.indicative_present().items()
        }

    def indicative_past_perfect(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.indicative_imperfect().items()
        }

    def indicative_past_anterior(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.indicative_preterite().items()
        }

    def indicative_future_perfect(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.indicative_future().items()
        }

    def indicative_conditional_perfect(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.indicative_conditional().items()
        }

    def subjunctive_present(self) -> dict:
        return self.personal_conjugation.conjugate(["e", "es", "és", "e", "emos", "éis", "en"])

    def subjunctive_imperfect_preterite(self, alternate_form: bool = False) -> dict:
        if not alternate_form:
            return self.personal_conjugation.conjugate(["ara", "aras", "aras", "ara", "áramos", "arais", "aran"])
        else:
            return self.personal_conjugation.conjugate(["ase", "ases", "ases", "ase", "ásemos", "aseis", "asen"])

    def subjunctive_future(self) -> dict:
        return self.personal_conjugation.conjugate(["are", "ares", "ares", "are", "áremos", "areis", "aren"])

    def subjunctive_present_perfect(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.subjunctive_present().items()
        }

    def subjunctive_past_perfect(self, alternate_form: bool = False) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.subjunctive_imperfect_preterite(alternate_form).items()
        }

    def subjunctive_future_perfect(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.subjunctive_future().items()
        }

    def imperative_affirmative(self) -> dict:
        return self.imperative_conjugation.conjugate(["a", "á", "e", "emos", "ad", "en"])

    def imperative_negative(self) -> dict:
        return self.imperative_conjugation.conjugate(["es", "és", "e", "emos", "éis", "en"])
