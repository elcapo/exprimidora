from typing import Union

class BaseVerb:
    def __init__(self):
        self.infinitive = None

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
            conjugation = conjugator()
            if type(conjugation) == str:
                forms = forms.union({conjugation})
            elif type(conjugation) == dict:
                forms = forms.union(set(conjugation.values()))
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
