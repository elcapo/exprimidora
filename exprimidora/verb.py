from typing import Union

class Verb:
    def __init__(self):
        self.infinitive = None

    def root(self) -> str:
        return self.infinitive[:-2]
    
    def suffixed(self, suffix: str) -> str:
        return "{}{}".format(self.root(), suffix)

    def conjugate_personal(self, suffixes: list, person: str = None) -> Union[dict, str]:
        suffix_to_person = {
            "yo": 0,
            "tú": 1,
            "vos": 2,
            "usted": 3,
            "él": 3,
            "ella": 3,
            "nosotros": 4,
            "nosotras": 4,
            "vosotros": 5,
            "vosotras": 5,
            "ustedes": 6,
            "ellos": 6,
            "ellas": 6,
        }

        if person:
            return self.suffixed(suffixes[suffix_to_person[person]])

        return {
            "yo": self.suffixed(suffixes[suffix_to_person["yo"]]),
            "tú": self.suffixed(suffixes[suffix_to_person["tú"]]),
            "vos": self.suffixed(suffixes[suffix_to_person["vos"]]),
            "usted": self.suffixed(suffixes[suffix_to_person["usted"]]),
            "él": self.suffixed(suffixes[suffix_to_person["él"]]),
            "ella": self.suffixed(suffixes[suffix_to_person["ella"]]),
            "nosotros": self.suffixed(suffixes[suffix_to_person["nosotros"]]),
            "nosotras": self.suffixed(suffixes[suffix_to_person["nosotras"]]),
            "vosotros": self.suffixed(suffixes[suffix_to_person["vosotros"]]),
            "vosotras": self.suffixed(suffixes[suffix_to_person["vosotras"]]),
            "ustedes": self.suffixed(suffixes[suffix_to_person["ustedes"]]),
            "ellos": self.suffixed(suffixes[suffix_to_person["ellos"]]),
            "ellas": self.suffixed(suffixes[suffix_to_person["ellas"]]),
        }

    def conjugate_imperative(self, suffixes: list, person: str = None) -> Union[dict, str]:
        suffix_to_person = {
            "tú": 0,
            "vos": 1,
            "usted": 2,
            "nosotros": 3,
            "nosotras": 3,
            "vosotros": 4,
            "vosotras": 4,
            "ustedes": 5,
        }

        if person:
            return self.suffixed(suffixes[suffix_to_person[person]])

        return {
            "tú": self.suffixed(suffixes[suffix_to_person["tú"]]),
            "vos": self.suffixed(suffixes[suffix_to_person["vos"]]),
            "usted": self.suffixed(suffixes[suffix_to_person["usted"]]),
            "nosotros": self.suffixed(suffixes[suffix_to_person["nosotros"]]),
            "nosotras": self.suffixed(suffixes[suffix_to_person["nosotras"]]),
            "vosotros": self.suffixed(suffixes[suffix_to_person["vosotros"]]),
            "vosotras": self.suffixed(suffixes[suffix_to_person["vosotras"]]),
            "ustedes": self.suffixed(suffixes[suffix_to_person["ustedes"]]),
        }

    def all_form_names(self, only_simple: bool = False) -> list:
        simple_form_names = [
            "gerund",
            "participle",
            "indicative_present",
            "indicative_imperfect",
            "indicative_preterite",
            "indicative_future",
            "indicative_conditional",
            "subjunctive_present",
            "subjunctive_imperfect_preterite",
            "subjunctive_future",
            "imperative_affirmative",
            "imperative_negative",
        ]

        compound_form_names = [
            "indicative_present_perfect",
            "indicative_past_perfect",
            "indicative_past_anterior",
            "indicative_future_perfect",
            "indicative_conditional_perfect",
            "subjunctive_present_perfect",
            "subjunctive_past_perfect",
            "subjunctive_future_perfect",
        ]

        if only_simple:
            return simple_form_names
        
        return simple_form_names + compound_form_names

    def all_forms(self, only_simple: bool = False) -> dict:
        forms = {}
        for tense in self.all_form_names(only_simple):
            conjugator = getattr(self, tense)
            forms[tense] = conjugator()
        return forms

    def all_forms_flattened(self, only_simple: bool = False) -> list:
        forms = set()
        for tense in self.all_form_names(only_simple):
            conjugator = getattr(self, tense)
            forms = forms.union(set(conjugator().values()))
        forms = list(forms)
        forms.sort()
        return forms

    def indicative_present_perfect(self, person: str = None) -> Union[dict, str]:
        if person:
            return "{} {}".format(self.to_have.indicative_present(person), self.participle())

        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.indicative_present().items()
        }

    def indicative_past_perfect(self, person: str = None) -> Union[dict, str]:
        if person:
            return "{} {}".format(self.to_have.indicative_imperfect(person), self.participle())

        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.indicative_imperfect().items()
        }

    def indicative_past_anterior(self, person: str = None) -> Union[dict, str]:
        if person:
            return "{} {}".format(self.to_have.indicative_preterite(person), self.participle())

        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.indicative_preterite().items()
        }

    def indicative_future_perfect(self, person: str = None) -> Union[dict, str]:
        if person:
            return "{} {}".format(self.to_have.indicative_future(person), self.participle())

        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.indicative_future().items()
        }

    def indicative_conditional_perfect(self, person: str = None) -> Union[dict, str]:
        if person:
            return "{} {}".format(self.to_have.indicative_conditional(person), self.participle())

        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.indicative_conditional().items()
        }

    def subjunctive_present_perfect(self, person: str = None) -> Union[dict, str]:
        if person:
            return "{} {}".format(self.to_have.subjunctive_present(person), self.participle())

        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.subjunctive_present().items()
        }

    def subjunctive_past_perfect(self, person: str = None) -> Union[dict, str]:
        if person:
            return "{} {}".format(self.to_have.subjunctive_imperfect_preterite(person), self.participle())

        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.subjunctive_imperfect_preterite().items()
        }

    def subjunctive_past_perfect_alternate(self, person: str = None) -> Union[dict, str]:
        if person:
            return "{} {}".format(self.to_have.subjunctive_imperfect_preterite_alternate(person), self.participle())

        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.subjunctive_imperfect_preterite_alternate().items()
        }

    def subjunctive_future_perfect(self, person: str = None) -> Union[dict, str]:
        if person:
            return "{} {}".format(self.to_have.subjunctive_future(person), self.participle())

        return {
            subject: "{} {}".format(conjugated_have, self.participle())
                for subject, conjugated_have in self.to_have.subjunctive_future().items()
        }
