from exprimidora import IrregularToHave

class RegularSecondGroup:
    def __init__(self, infinitive: str):
        if len(infinitive) <= 2:
            raise Exception("Invalid regular verb of the second group as it's length only two characters")
        if not infinitive[-2:] == "er":
            raise Exception("Invalid regular verb of the second group as it does not terminate in: -er")
        self.infinitive = infinitive
        self.to_have = IrregularToHave()
    
    def root(self) -> str:
        return self.infinitive[:-2]
    
    def suffixed(self, suffix: str) -> str:
        return "{}{}".format(self.root(), suffix)
    
    def gerund(self) -> str:
        return self.suffixed("iendo")

    def participle(self) -> str:
        return self.suffixed("ido")

    def indicative_present(self) -> dict:
        return {
            "yo": self.suffixed("o"),
            "tú": self.suffixed("es"),
            "vos": self.suffixed("és"),
            "usted": self.suffixed("e"),
            "él": self.suffixed("e"),
            "ella": self.suffixed("e"),
            "nosotros": self.suffixed("emos"),
            "nosotras": self.suffixed("emos"),
            "vosotros": self.suffixed("éis"),
            "vosotras": self.suffixed("éis"),
            "ustedes": self.suffixed("en"),
            "ellos": self.suffixed("en"),
            "ellas": self.suffixed("en"),
        }

    def indicative_imperfect(self) -> dict:
        return {
            "yo": self.suffixed("ía"),
            "tú": self.suffixed("ías"),
            "vos": self.suffixed("ías"),
            "usted": self.suffixed("ía"),
            "él": self.suffixed("ía"),
            "ella": self.suffixed("ía"),
            "nosotros": self.suffixed("íamos"),
            "nosotras": self.suffixed("íamos"),
            "vosotros": self.suffixed("íais"),
            "vosotras": self.suffixed("íais"),
            "ustedes": self.suffixed("ían"),
            "ellos": self.suffixed("ían"),
            "ellas": self.suffixed("ían"),
        }

    def indicative_preterite(self) -> dict:
        return {
            "yo": self.suffixed("í"),
            "tú": self.suffixed("iste"),
            "vos": self.suffixed("iste"),
            "usted": self.suffixed("ió"),
            "él": self.suffixed("ió"),
            "ella": self.suffixed("ió"),
            "nosotros": self.suffixed("íamos"),
            "nosotras": self.suffixed("íamos"),
            "vosotros": self.suffixed("isteis"),
            "vosotras": self.suffixed("isteis"),
            "ustedes": self.suffixed("ieron"),
            "ellos": self.suffixed("ieron"),
            "ellas": self.suffixed("ieron"),
        }

    def indicative_future(self) -> dict:
        return {
            "yo": self.suffixed("eré"),
            "tú": self.suffixed("erás"),
            "vos": self.suffixed("erás"),
            "usted": self.suffixed("erá"),
            "él": self.suffixed("erá"),
            "ella": self.suffixed("erá"),
            "nosotros": self.suffixed("eremos"),
            "nosotras": self.suffixed("eréis"),
            "vosotros": self.suffixed("eréis"),
            "vosotras": self.suffixed("eréis"),
            "ustedes": self.suffixed("erán"),
            "ellos": self.suffixed("erán"),
            "ellas": self.suffixed("erán"),
        }

    def indicative_conditional(self) -> dict:
        return {
            "yo": self.suffixed("ería"),
            "tú": self.suffixed("erías"),
            "vos": self.suffixed("erías"),
            "usted": self.suffixed("ería"),
            "él": self.suffixed("ería"),
            "ella": self.suffixed("ería"),
            "nosotros": self.suffixed("eríamos"),
            "nosotras": self.suffixed("eríamos"),
            "vosotros": self.suffixed("eríais"),
            "vosotras": self.suffixed("eríais"),
            "ustedes": self.suffixed("erían"),
            "ellos": self.suffixed("erían"),
            "ellas": self.suffixed("erían"),
        }

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
        return {
            "yo": self.suffixed("a"),
            "tú": self.suffixed("as"),
            "vos": self.suffixed("ás"),
            "usted": self.suffixed("a"),
            "él": self.suffixed("a"),
            "ella": self.suffixed("a"),
            "nosotros": self.suffixed("amos"),
            "nosotras": self.suffixed("amos"),
            "vosotros": self.suffixed("áis"),
            "vosotras": self.suffixed("áis"),
            "ustedes": self.suffixed("an"),
            "ellos": self.suffixed("an"),
            "ellas": self.suffixed("an"),
        }

    def subjunctive_imperfect_preterite(self, alternate_form: bool = False) -> dict:
        if not alternate_form:
            return {
            "yo": self.suffixed("iera"),
            "tú": self.suffixed("ieras"),
            "vos": self.suffixed("ieras"),
            "usted": self.suffixed("iera"),
            "él": self.suffixed("iera"),
            "ella": self.suffixed("iera"),
            "nosotros": self.suffixed("iéramos"),
            "nosotras": self.suffixed("iéramos"),
            "vosotros": self.suffixed("ierais"),
            "vosotras": self.suffixed("ierais"),
            "ustedes": self.suffixed("ieran"),
            "ellos": self.suffixed("ieran"),
            "ellas": self.suffixed("ieran"),
            }
        else:
            return {
            "yo": self.suffixed("iese"),
            "tú": self.suffixed("ieses"),
            "vos": self.suffixed("ieses"),
            "usted": self.suffixed("iese"),
            "él": self.suffixed("iese"),
            "ella": self.suffixed("iese"),
            "nosotros": self.suffixed("iésemos"),
            "nosotras": self.suffixed("iésemos"),
            "vosotros": self.suffixed("ieseis"),
            "vosotras": self.suffixed("ieseis"),
            "ustedes": self.suffixed("iesen"),
            "ellos": self.suffixed("iesen"),
            "ellas": self.suffixed("iesen"),
            }

    def subjunctive_future(self) -> dict:
        return {
            "yo": self.suffixed("iere"),
            "tú": self.suffixed("ieres"),
            "vos": self.suffixed("ieres"),
            "usted": self.suffixed("iere"),
            "él": self.suffixed("iere"),
            "ella": self.suffixed("iere"),
            "nosotros": self.suffixed("iéremos"),
            "nosotras": self.suffixed("iéremos"),
            "vosotros": self.suffixed("iereis"),
            "vosotras": self.suffixed("iereis"),
            "ustedes": self.suffixed("ieren"),
            "ellos": self.suffixed("ieren"),
            "ellas": self.suffixed("ieren"),
        }

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
        return {
            "tú": self.suffixed("e"),
            "vos": self.suffixed("é"),
            "usted": self.suffixed("a"),
            "nosotros": self.suffixed("amos"),
            "nosotras": self.suffixed("amos"),
            "vosotros": self.suffixed("ed"),
            "vosotras": self.suffixed("ed"),
            "ustedes": self.suffixed("an"),
        }

    def imperative_negative(self) -> dict:
        return {
            "tú": self.suffixed("as"),
            "vos": self.suffixed("ás"),
            "usted": self.suffixed("a"),
            "nosotros": self.suffixed("amos"),
            "nosotras": self.suffixed("amos"),
            "vosotros": self.suffixed("ais"),
            "vosotras": self.suffixed("ais"),
            "ustedes": self.suffixed("an"),
        }
