class IrregularToHave:
    def __init__(self):
        self.infinitive = "haber"
    
    def gerund(self) -> str:
        return "habiendo"

    def participle(self) -> str:
        return "habido"

    def indicative_present(self) -> dict:
        return {
            "yo": "he",
            "tú": "has",
            "vos": "has",
            "usted": "ha",
            "él": "ha",
            "ella": "ha",
            "nosotros": "hemos",
            "nosotras": "hemos",
            "vosotros": "habéis",
            "vosotras": "habéis",
            "ustedes": "han",
            "ellos": "han",
            "ellas": "han",
        }

    def indicative_imperfect(self) -> dict:
        return {
            "yo": "había",
            "tú": "habías",
            "vos": "habías",
            "usted": "había",
            "él": "había",
            "ella": "había",
            "nosotros": "habíamos",
            "nosotras": "habíamos",
            "vosotros": "habíais",
            "vosotras": "habíais",
            "ustedes": "habían",
            "ellos": "habían",
            "ellas": "habían",
        }

    def indicative_preterite(self) -> dict:
        return {
            "yo": "hube",
            "tú": "hubiste",
            "vos": "hubiste",
            "usted": "hubo",
            "él": "hubo",
            "ella": "hubo",
            "nosotros": "hubimos",
            "nosotras": "hubimos",
            "vosotros": "hubisteis",
            "vosotras": "hubisteis",
            "ustedes": "hubieron",
            "ellos": "hubieron",
            "ellas": "hubieron",
        }

    def indicative_future(self) -> dict:
        return {
            "yo": "habré",
            "tú": "habrás",
            "vos": "habrás",
            "usted": "habrá",
            "él": "habrá",
            "ella": "habrá",
            "nosotros": "habremos",
            "nosotras": "habremos",
            "vosotros": "habréis",
            "vosotras": "habréis",
            "ustedes": "habrán",
            "ellos": "habrán",
            "ellas": "habrán",
        }

    def indicative_conditional(self) -> dict:
        return {
            "yo": "habría",
            "tú": "habrías",
            "vos": "habrías",
            "usted": "habría",
            "él": "habría",
            "ella": "habría",
            "nosotros": "habríamos",
            "nosotras": "habríamos",
            "vosotros": "habríais",
            "vosotras": "habríais",
            "ustedes": "habrían",
            "ellos": "habrían",
            "ellas": "habrían",
        }

    def indicative_present_perfect(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.indicative_present().items()
        }

    def indicative_past_perfect(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.indicative_imperfect().items()
        }

    def indicative_past_anterior(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.indicative_preterite().items()
        }

    def indicative_future_perfect(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.indicative_future().items()
        }

    def indicative_conditional_perfect(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.indicative_conditional().items()
        }

    def subjunctive_present(self) -> dict:
        return {
            "yo": "haya",
            "tú": "hayas",
            "vos": "hayas",
            "usted": "haya",
            "él": "haya",
            "ella": "haya",
            "nosotros": "hayamos",
            "nosotras": "hayamos",
            "vosotros": "hayáis",
            "vosotras": "hayáis",
            "ustedes": "hayan",
            "ellos": "hayan",
            "ellas": "hayan",
        }

    def subjunctive_imperfect_preterite(self, alternate_form: bool = False) -> dict:
        if not alternate_form:
            return {
                "yo": "hubiera",
                "tú": "hubieras",
                "vos": "hubieras",
                "usted": "hubiera",
                "él": "hubiera",
                "ella": "hubiera",
                "nosotros": "hubiéramos",
                "nosotras": "hubiéramos",
                "vosotros": "hubierais",
                "vosotras": "hubierais",
                "ustedes": "hubieran",
                "ellos": "hubieran",
                "ellas": "hubieran",
            }
        else:
            return {
                "yo": "hubiese",
                "tú": "hubieses",
                "vos": "hubieses",
                "usted": "hubiese",
                "él": "hubiese",
                "ella": "hubiese",
                "nosotros": "hubiésemos",
                "nosotras": "hubiésemos",
                "vosotros": "hubieseis",
                "vosotras": "hubieseis",
                "ustedes": "hubiesen",
                "ellos": "hubiesen",
                "ellas": "hubiesen",
            }

    def subjunctive_future(self) -> dict:
        return {
            "yo": "hubiere",
            "tú": "hubieres",
            "vos": "hubieres",
            "usted": "hubiere",
            "él": "hubiere",
            "ella": "hubiere",
            "nosotros": "hubiéremos",
            "nosotras": "hubiéremos",
            "vosotros": "hubiereis",
            "vosotras": "hubiereis",
            "ustedes": "hubieren",
            "ellos": "hubieren",
            "ellas": "hubieren",
        }

    def subjunctive_present_perfect(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.subjunctive_present().items()
        }

    def subjunctive_past_perfect(self, alternate_form: bool = False) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.subjunctive_imperfect_preterite(alternate_form).items()
        }

    def subjunctive_future_perfect(self) -> dict:
        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.subjunctive_future().items()
        }

    def imperative_affirmative(self) -> dict:
        return {
            "tú": "he",
            "vos": "he",
            "usted": "haya",
            "nosotros": "hayamos",
            "nosotras": "hayamos",
            "vosotros": "habed",
            "vosotras": "habed",
            "ustedes": "hayan",
        }

    def imperative_negative(self) -> dict:
        return {
            "tú": "hayas",
            "vos": "hayás",
            "usted": "haya",
            "nosotros": "hayamos",
            "nosotras": "hayamos",
            "vosotros": "hayáis",
            "vosotras": "hayáis",
            "ustedes": "hayan",
        }
