from exprimidora import IrregularToHave

class RegularFirstGroup:
    def __init__(self, infinitive: str):
        if len(infinitive) <= 2:
            raise Exception("Invalid regular verb of the first group as it's length only two characters")
        if not infinitive[-2:] == "ar":
            raise Exception("Invalid regular verb of the first group as it does not terminate in: -ar")
        self.infinitive = infinitive
        self.to_have = IrregularToHave()
    
    def root(self) -> str:
        return self.infinitive[:-2]
    
    def suffixed(self, suffix: str) -> str:
        return "{}{}".format(self.root(), suffix)
    
    def gerund(self) -> str:
        return self.suffixed("ando")

    def participle(self) -> str:
        return self.suffixed("ado")

    def indicative_present(self) -> dict:
        return {
            "yo": self.suffixed("o"),
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

    def indicative_imperfect(self) -> dict:
        return {
            "yo": self.suffixed("aba"),
            "tú": self.suffixed("abas"),
            "vos": self.suffixed("abas"),
            "usted": self.suffixed("aba"),
            "él": self.suffixed("aba"),
            "ella": self.suffixed("aba"),
            "nosotros": self.suffixed("ábamos"),
            "nosotras": self.suffixed("ábamos"),
            "vosotros": self.suffixed("abais"),
            "vosotras": self.suffixed("abais"),
            "ustedes": self.suffixed("aban"),
            "ellos": self.suffixed("aban"),
            "ellas": self.suffixed("aban"),
        }

    def indicative_preterite(self) -> dict:
        return {
            "yo": self.suffixed("é"),
            "tú": self.suffixed("aste"),
            "vos": self.suffixed("aste"),
            "usted": self.suffixed("ó"),
            "él": self.suffixed("ó"),
            "ella": self.suffixed("ó"),
            "nosotros": self.suffixed("amos"),
            "nosotras": self.suffixed("amos"),
            "vosotros": self.suffixed("asteis"),
            "vosotras": self.suffixed("asteis"),
            "ustedes": self.suffixed("aron"),
            "ellos": self.suffixed("aron"),
            "ellas": self.suffixed("aron"),
        }

    def indicative_future(self) -> dict:
        return {
            "yo": self.suffixed("aré"),
            "tú": self.suffixed("arás"),
            "vos": self.suffixed("arás"),
            "usted": self.suffixed("ará"),
            "él": self.suffixed("ará"),
            "ella": self.suffixed("ará"),
            "nosotros": self.suffixed("aremos"),
            "nosotras": self.suffixed("aréis"),
            "vosotros": self.suffixed("aréis"),
            "vosotras": self.suffixed("aréis"),
            "ustedes": self.suffixed("arán"),
            "ellos": self.suffixed("arán"),
            "ellas": self.suffixed("arán"),
        }

    def indicative_conditional(self) -> dict:
        return {
            "yo": self.suffixed("aría"),
            "tú": self.suffixed("arías"),
            "vos": self.suffixed("arías"),
            "usted": self.suffixed("aría"),
            "él": self.suffixed("aría"),
            "ella": self.suffixed("aría"),
            "nosotros": self.suffixed("aríamos"),
            "nosotras": self.suffixed("aríamos"),
            "vosotros": self.suffixed("aríais"),
            "vosotras": self.suffixed("aríais"),
            "ustedes": self.suffixed("arían"),
            "ellos": self.suffixed("arían"),
            "ellas": self.suffixed("arían"),
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
            "yo": self.suffixed("e"),
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

    def subjunctive_imperfect_preterite(self, alternate_form: bool = False) -> dict:
        if not alternate_form:
            return {
            "yo": self.suffixed("ara"),
            "tú": self.suffixed("aras"),
            "vos": self.suffixed("aras"),
            "usted": self.suffixed("ara"),
            "él": self.suffixed("ara"),
            "ella": self.suffixed("ara"),
            "nosotros": self.suffixed("áramos"),
            "nosotras": self.suffixed("áramos"),
            "vosotros": self.suffixed("arais"),
            "vosotras": self.suffixed("arais"),
            "ustedes": self.suffixed("aran"),
            "ellos": self.suffixed("aran"),
            "ellas": self.suffixed("aran"),
            }
        else:
            return {
            "yo": self.suffixed("ase"),
            "tú": self.suffixed("ases"),
            "vos": self.suffixed("ases"),
            "usted": self.suffixed("ase"),
            "él": self.suffixed("ase"),
            "ella": self.suffixed("ase"),
            "nosotros": self.suffixed("ásemos"),
            "nosotras": self.suffixed("ásemos"),
            "vosotros": self.suffixed("aseis"),
            "vosotras": self.suffixed("aseis"),
            "ustedes": self.suffixed("asen"),
            "ellos": self.suffixed("asen"),
            "ellas": self.suffixed("asen"),
            }

    def subjunctive_future(self) -> dict:
        return {
            "yo": self.suffixed("are"),
            "tú": self.suffixed("ares"),
            "vos": self.suffixed("ares"),
            "usted": self.suffixed("are"),
            "él": self.suffixed("are"),
            "ella": self.suffixed("are"),
            "nosotros": self.suffixed("áremos"),
            "nosotras": self.suffixed("áremos"),
            "vosotros": self.suffixed("areis"),
            "vosotras": self.suffixed("areis"),
            "ustedes": self.suffixed("aren"),
            "ellos": self.suffixed("aren"),
            "ellas": self.suffixed("aren"),
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
            "tú": self.suffixed("a"),
            "vos": self.suffixed("á"),
            "usted": self.suffixed("e"),
            "nosotros": self.suffixed("emos"),
            "nosotras": self.suffixed("emos"),
            "vosotros": self.suffixed("ad"),
            "vosotras": self.suffixed("ad"),
            "ustedes": self.suffixed("en"),
        }

    def imperative_negative(self) -> dict:
        return {
            "tú": self.suffixed("es"),
            "vos": self.suffixed("és"),
            "usted": self.suffixed("e"),
            "nosotros": self.suffixed("emos"),
            "nosotras": self.suffixed("emos"),
            "vosotros": self.suffixed("éis"),
            "vosotras": self.suffixed("éis"),
            "ustedes": self.suffixed("en"),
        }
