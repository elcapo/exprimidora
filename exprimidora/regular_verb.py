from typing import Union
from exprimidora.irregular_to_have import IrregularToHave
from exprimidora import Verb

class RegularVerb(Verb):
    def __init__(self, infinitive: str):
        self.to_have = IrregularToHave()
        super().__init__(infinitive)
    
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
