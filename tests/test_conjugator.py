from exprimidora import conjugator

def test_dispatches_to_be_standing():
    verb = conjugator("estar")
    assert type(verb).__name__ == "IrregularToBeStanding"
    assert verb.indicative_present("yo") == "estoy"

def test_dispatches_to_be_existing():
    verb = conjugator("ser")
    assert type(verb).__name__ == "IrregularToBeExisting"
    assert verb.indicative_present("yo") == "soy"

def test_dispatches_to_have():
    verb = conjugator("haber")
    assert type(verb).__name__ == "IrregularToHave"
    assert verb.indicative_present("yo") == "he"

def test_dispatches_model_request():
    verb = conjugator("vestir")
    assert type(verb).__name__ == "ModelRequest"
    assert verb.indicative_present("yo") == "visto"

def test_dispatches_regular_first_group():
    verb = conjugator("amar")
    assert type(verb).__name__ == "RegularFirstGroup"
    assert verb.indicative_present("yo") == "amo"

def test_dispatches_regular_second_group():
    verb = conjugator("temer")
    assert type(verb).__name__ == "RegularSecondGroup"
    assert verb.indicative_present("yo") == "temo"

def test_dispatches_regular_third_group():
    verb = conjugator("partir")
    assert type(verb).__name__ == "RegularThirdGroup"
    assert verb.indicative_present("yo") == "parto"
