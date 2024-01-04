from exprimidora import *

def conjugator(infinitive: str) -> Verb:
    if infinitive == "estar":
        return IrregularToBeStanding()
    elif infinitive == "ser":
        return IrregularToBeExisting()
    elif infinitive == "haber":
        return IrregularToHave()
    elif infinitive.endswith("ar"):
        return RegularFirstGroup(infinitive)
    elif infinitive.endswith("er"):
        return RegularFirstGroup(infinitive)
    elif infinitive.endswith("ir"):
        return RegularFirstGroup(infinitive)
    else:
        raise Exception("Unknown verb")
