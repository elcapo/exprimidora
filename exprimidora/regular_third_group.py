from exprimidora import IrregularToHave
from exprimidora.personal_conjugation import PersonalConjugation
from exprimidora.imperative_conjugation import ImperativeConjugation

class RegularThirdGroup:
    def __init__(self, infinitive: str):
        if len(infinitive) <= 2:
            raise Exception("Invalid regular verb of the third group as it's length only two characters")
        if not infinitive[-2:] == "ir":
            raise Exception("Invalid regular verb of the third group as it does not terminate in: -ir")
        self.infinitive = infinitive
        self.to_have = IrregularToHave()
        self.personal_conjugation = PersonalConjugation(self.suffixed)
        self.imperative_conjugation = ImperativeConjugation(self.suffixed)

    def root(self) -> str:
        return self.infinitive[:-2]
    
    def suffixed(self, suffix: str) -> str:
        return "{}{}".format(self.root(), suffix)
    
    def gerund(self) -> str:
        return self.suffixed("iendo")

    def participle(self) -> str:
        return self.suffixed("ido")

    def indicative_present(self) -> dict:
        return self.personal_conjugation.conjugate(["o", "es", "ís", "e", "imos", "ís", "en"])

    def indicative_imperfect(self) -> dict:
        return self.personal_conjugation.conjugate(["ía", "ías", "ías", "ía", "íamos", "íais", "ían"])

    def indicative_preterite(self) -> dict:
        return self.personal_conjugation.conjugate(["í", "iste", "iste", "ió", "imos", "isteis", "ieron"])

    def indicative_future(self) -> dict:
        return self.personal_conjugation.conjugate(["iré", "irás", "irás", "irá", "iremos", "iréis", "irán"])

    def indicative_conditional(self) -> dict:
        return self.personal_conjugation.conjugate(["iría", "irías", "irías", "iría", "iríamos", "iríais", "irían"])

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
        return self.personal_conjugation.conjugate(["a", "as", "ás", "a", "amos", "áis", "an"])

    def subjunctive_imperfect_preterite(self, alternate_form: bool = False) -> dict:
        if not alternate_form:
            return self.personal_conjugation.conjugate(["iera", "ieras", "ieras", "iera", "iéramos", "ierais", "ieran"])
        else:
            return self.personal_conjugation.conjugate(["iese", "ieses", "ieses", "iese", "iésemos", "ieseis", "iesen"])

    def subjunctive_future(self) -> dict:
        return self.personal_conjugation.conjugate(["iere", "ieres", "ieres", "iere", "iéremos", "iereis", "ieren"])

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
        return self.imperative_conjugation.conjugate(["e", "í", "a", "amos", "id", "an"])

    def imperative_negative(self) -> dict:
        return self.imperative_conjugation.conjugate(["as", "ás", "a", "amos", "áis", "an"])
