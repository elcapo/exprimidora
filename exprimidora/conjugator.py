from exprimidora import *

def conjugator(infinitive: str) -> Verb:
    if infinitive == "estar":
        return IrregularToBeStanding()
    elif infinitive == "ser":
        return IrregularToBeExisting()
    elif infinitive == "haber":
        return IrregularToHave()
    elif follows_model_request(infinitive):
        return ModelRequest(infinitive)
    elif infinitive.endswith("ar"):
        return RegularFirstGroup(infinitive)
    elif infinitive.endswith("er"):
        return RegularSecondGroup(infinitive)
    elif infinitive.endswith("ir"):
        return RegularThirdGroup(infinitive)
    else:
        raise Exception("Unknown verb")

def follows_model_request(infinitive: str) -> bool:
    if infinitive.endswith("colegir"):
        return True
    if infinitive.endswith("concebir"):
        return True
    if infinitive.endswith("corregir"):
        return True
    if infinitive.endswith("derretir"):
        return True
    if infinitive.endswith("elegir"):
        return True
    if infinitive.endswith("embestir"):
        return True
    if infinitive.endswith("gemir"):
        return True
    if infinitive.endswith("henchir"):
        return True
    if infinitive.endswith("medir"):
        return True
    if infinitive.endswith("pedir"):
        return True
    if infinitive.endswith("petir"):
        return True
    if infinitive.endswith("regir"):
        return True
    if infinitive.endswith("rendir"):
        return True
    if infinitive.endswith("seguir"):
        return True
    if infinitive.endswith("servir"):
        return True
    if infinitive.endswith("vestir"):
        return True
    