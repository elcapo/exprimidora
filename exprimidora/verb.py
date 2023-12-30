class Verb:
    def __init__(self):
        self.infinitive = None

    def root(self) -> str:
        return self.infinitive[:-2]
    
    def suffixed(self, suffix: str) -> str:
        return "{}{}".format(self.root(), suffix)

    def personal_conjugation(self, suffixes: list) -> dict:
        return {
            "yo": self.suffixed(suffixes[0]),
            "tú": self.suffixed(suffixes[1]),
            "vos": self.suffixed(suffixes[2]),
            "usted": self.suffixed(suffixes[3]),
            "él": self.suffixed(suffixes[3]),
            "ella": self.suffixed(suffixes[3]),
            "nosotros": self.suffixed(suffixes[4]),
            "nosotras": self.suffixed(suffixes[4]),
            "vosotros": self.suffixed(suffixes[5]),
            "vosotras": self.suffixed(suffixes[5]),
            "ustedes": self.suffixed(suffixes[6]),
            "ellos": self.suffixed(suffixes[6]),
            "ellas": self.suffixed(suffixes[6]),
        }

    def imperative_conjugation(self, suffixes: list) -> dict:
        return {
            "tú": self.suffixed(suffixes[0]),
            "vos": self.suffixed(suffixes[1]),
            "usted": self.suffixed(suffixes[2]),
            "nosotros": self.suffixed(suffixes[3]),
            "nosotras": self.suffixed(suffixes[3]),
            "vosotros": self.suffixed(suffixes[4]),
            "vosotras": self.suffixed(suffixes[4]),
            "ustedes": self.suffixed(suffixes[5]),
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
