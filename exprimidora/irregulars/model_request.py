from exprimidora.syllable_separator import syllable_separator
from exprimidora.irregulars.to_have import IrregularToHave
from exprimidora.verb import Verb
from typing import Union

class ModelRequest(Verb):
    def __init__(self, infinitive: str):
        if len(infinitive) <= 2:
            raise Exception("Invalid verb for the model of `pedir` as it's length only two characters")
        if not infinitive[-2:] == "ir":
            raise Exception("Invalid verb for the model of `pedir` as it does not terminate in: -ir")
        
        self.to_have = IrregularToHave()
        self.infinitive = infinitive

    def root(self, last_letter: str = "e") -> str:
        except_last_syllable = "".join(self.syllables()[:-1])
        return except_last_syllable[:-1] + last_letter

    def finish(self, suffix: str) -> str:
        last_syllable = self.syllables()[-1]
        last_syllable_prefix = last_syllable[:-2]
        suffix_first_letter = suffix[0]
        if last_syllable_prefix == "gu" and suffix_first_letter in ["a", "o", "u", "á", "ó", "ú"]:
            last_syllable_prefix = "g"
        return last_syllable_prefix + suffix

    def syllables(self) -> list:
        return syllable_separator(self.infinitive)

    def gerund(self) -> str:
        return self.root("i") + self.finish("iendo")

    def participle(self) -> str:
        return self.root() + self.finish("ido")

    def indicative_present(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "yo": self.root("i") + self.finish("o"),
            "tú": self.root("i") + self.finish("es"),
            "vos": self.root() + self.finish("ís"),
            "usted": self.root("i") + self.finish("e"),
            "él": self.root("i") + self.finish("e"),
            "ella": self.root("i") + self.finish("e"),
            "nosotros": self.root() + self.finish("imos"),
            "nosotras": self.root() + self.finish("imos"),
            "vosotros": self.root() + self.finish("ís"),
            "vosotras": self.root() + self.finish("ís"),
            "ustedes": self.root("i") + self.finish("en"),
            "ellos": self.root("i") + self.finish("en"),
            "ellas": self.root("i") + self.finish("en"),
        }

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_imperfect(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "yo": self.root() + self.finish("ía"),
            "tú": self.root() + self.finish("ías"),
            "vos": self.root() + self.finish("ías"),
            "usted": self.root() + self.finish("ía"),
            "él": self.root() + self.finish("ía"),
            "ella": self.root() + self.finish("ía"),
            "nosotros": self.root() + self.finish("íamos"),
            "nosotras": self.root() + self.finish("íamos"),
            "vosotros": self.root() + self.finish("íais"),
            "vosotras": self.root() + self.finish("íais"),
            "ustedes": self.root() + self.finish("ían"),
            "ellos": self.root() + self.finish("ían"),
            "ellas": self.root() + self.finish("ían"),
        }

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_preterite(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "yo": self.root() + self.finish("í"),
            "tú": self.root() + self.finish("iste"),
            "vos": self.root() + self.finish("iste"),
            "usted": self.root("i") + self.finish("ió"),
            "él": self.root("i") + self.finish("ió"),
            "ella": self.root("i") + self.finish("ió"),
            "nosotros": self.root() + self.finish("imos"),
            "nosotras": self.root() + self.finish("imos"),
            "vosotros": self.root() + self.finish("isteis"),
            "vosotras": self.root() + self.finish("isteis"),
            "ustedes": self.root("i") + self.finish("ieron"),
            "ellos": self.root("i") + self.finish("ieron"),
            "ellas": self.root("i") + self.finish("ieron"),
        }

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_future(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "yo": self.root() + self.finish("iré"),
            "tú": self.root() + self.finish("irás"),
            "vos": self.root() + self.finish("irás"),
            "usted": self.root() + self.finish("irá"),
            "él": self.root() + self.finish("irá"),
            "ella": self.root() + self.finish("irá"),
            "nosotros": self.root() + self.finish("iremos"),
            "nosotras": self.root() + self.finish("iremos"),
            "vosotros": self.root() + self.finish("iréis"),
            "vosotras": self.root() + self.finish("iréis"),
            "ustedes": self.root() + self.finish("irán"),
            "ellos": self.root() + self.finish("irán"),
            "ellas": self.root() + self.finish("irán"),
        }

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_conditional(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "yo": self.root() + self.finish("iría"),
            "tú": self.root() + self.finish("irías"),
            "vos": self.root() + self.finish("irías"),
            "usted": self.root() + self.finish("iría"),
            "él": self.root() + self.finish("iría"),
            "ella": self.root() + self.finish("iría"),
            "nosotros": self.root() + self.finish("iríamos"),
            "nosotras": self.root() + self.finish("iríamos"),
            "vosotros": self.root() + self.finish("iríais"),
            "vosotras": self.root() + self.finish("iríais"),
            "ustedes": self.root() + self.finish("irían"),
            "ellos": self.root() + self.finish("irían"),
            "ellas": self.root() + self.finish("irían"),
        }

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_present(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "yo": self.root("i") + self.finish("a"),
            "tú": self.root("i") + self.finish("as"),
            "vos": self.root("i") + self.finish("ás"),
            "usted": self.root("i") + self.finish("a"),
            "él": self.root("i") + self.finish("a"),
            "ella": self.root("i") + self.finish("a"),
            "nosotros": self.root("i") + self.finish("amos"),
            "nosotras": self.root("i") + self.finish("amos"),
            "vosotros": self.root("i") + self.finish("áis"),
            "vosotras": self.root("i") + self.finish("áis"),
            "ustedes": self.root("i") + self.finish("an"),
            "ellos": self.root("i") + self.finish("an"),
            "ellas": self.root("i") + self.finish("an"),
        }

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_imperfect_preterite(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "yo": self.root("i") + self.finish("iera"),
            "tú": self.root("i") + self.finish("ieras"),
            "vos": self.root("i") + self.finish("ieras"),
            "usted": self.root("i") + self.finish("iera"),
            "él": self.root("i") + self.finish("iera"),
            "ella": self.root("i") + self.finish("iera"),
            "nosotros": self.root("i") + self.finish("iéramos"),
            "nosotras": self.root("i") + self.finish("iéramos"),
            "vosotros": self.root("i") + self.finish("ierais"),
            "vosotras": self.root("i") + self.finish("ierais"),
            "ustedes": self.root("i") + self.finish("ieran"),
            "ellos": self.root("i") + self.finish("ieran"),
            "ellas": self.root("i") + self.finish("ieran"),
        }

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_imperfect_preterite_alternate(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "yo": self.root("i") + self.finish("iese"),
            "tú": self.root("i") + self.finish("ieses"),
            "vos": self.root("i") + self.finish("ieses"),
            "usted": self.root("i") + self.finish("iese"),
            "él": self.root("i") + self.finish("iese"),
            "ella": self.root("i") + self.finish("iese"),
            "nosotros": self.root("i") + self.finish("iésemos"),
            "nosotras": self.root("i") + self.finish("iésemos"),
            "vosotros": self.root("i") + self.finish("ieseis"),
            "vosotras": self.root("i") + self.finish("ieseis"),
            "ustedes": self.root("i") + self.finish("iesen"),
            "ellos": self.root("i") + self.finish("iesen"),
            "ellas": self.root("i") + self.finish("iesen"),
        }

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_future(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "yo": self.root("i") + self.finish("iere"),
            "tú": self.root("i") + self.finish("ieres"),
            "vos": self.root("i") + self.finish("ieres"),
            "usted": self.root("i") + self.finish("iere"),
            "él": self.root("i") + self.finish("iere"),
            "ella": self.root("i") + self.finish("iere"),
            "nosotros": self.root("i") + self.finish("iéremos"),
            "nosotras": self.root("i") + self.finish("iéremos"),
            "vosotros": self.root("i") + self.finish("iereis"),
            "vosotras": self.root("i") + self.finish("iereis"),
            "ustedes": self.root("i") + self.finish("ieren"),
            "ellos": self.root("i") + self.finish("ieren"),
            "ellas": self.root("i") + self.finish("ieren"),
        }

        if person:
            return conjugation[person]
        
        return conjugation

    def imperative_affirmative(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "tú": self.root("i") + self.finish("e"),
            "vos": self.root() + self.finish("í"),
            "usted": self.root("i") + self.finish("a"),
            "nosotros": self.root("i") + self.finish("amos"),
            "nosotras": self.root("i") + self.finish("amos"),
            "vosotros": self.root() + self.finish("id"),
            "vosotras": self.root() + self.finish("id"),
            "ustedes": self.root("i") + self.finish("an"),
        }

        if person:
            return conjugation[person]
        
        return conjugation

    def imperative_negative(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "tú": self.root("i") + self.finish("as"),
            "vos": self.root("i") + self.finish("ás"),
            "usted": self.root("i") + self.finish("a"),
            "nosotros": self.root("i") + self.finish("amos"),
            "nosotras": self.root("i") + self.finish("amos"),
            "vosotros": self.root("i") + self.finish("áis"),
            "vosotras": self.root("i") + self.finish("áis"),
            "ustedes": self.root("i") + self.finish("an"),
        }

        if person:
            return conjugation[person]
        
        return conjugation
