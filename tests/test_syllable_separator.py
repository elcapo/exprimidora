from exprimidora.syllable_separator import *

def test_has_weird_characters():
    assert not has_weird_characters("hola")
    assert has_weird_characters("¡hola!")

def test_is_vowel():
    assert [is_vowel("hola", i) for i in range(len("hola"))] == [False, True, False, True]
    assert [is_vowel("guión", i) for i in range(len("guión"))] == [False, False, True, True, False]
    assert [is_vowel("pingüe", i) for i in range(len("pingüe"))] == [False, True, False, False, True, True]
    assert [is_vowel("que", i) for i in range(len("que"))] == [False, False, True]
    assert [is_vowel("yeye", i) for i in range(len("yeye"))] == [False, True, False, True]
    assert [is_vowel("hay", i) for i in range(len("hay"))] == [False, True, True]

def test_is_strong_vowel():
    assert [is_strong_vowel("hola", i) for i in range(len("hola"))] == [False, True, False, True]
    assert [is_strong_vowel("lío", i) for i in range(len("lío"))] == [False, True, True]

def test_is_weak_vowel():
    assert [is_weak_vowel("piojo", i) for i in range(len("piojo"))] == [False, True, False, False, False]
    assert [is_weak_vowel("lío", i) for i in range(len("lío"))] == [False, False, False]

def test_is_inseparable_consonant_pair():
    assert [is_inseparable_consonant_pair("chucho", i) for i in range(len("chucho"))] == [True, False, False, True, False, False]
    assert [is_inseparable_consonant_pair("cromo", i) for i in range(len("cromo"))] == [True, False, False, False, False]

def test_syllable_separator():
    assert syllable_separator("mano") == ["ma", "no"]
    assert syllable_separator("manto") == ["man", "to"]
    assert syllable_separator("queso") == ["que", "so"]
    assert syllable_separator("chucho") == ["chu", "cho"]
    assert syllable_separator("chanchullo") == ["chan", "chu", "llo"]
    assert syllable_separator("jalear") == ["ja", "le", "ar"]
    assert syllable_separator("paliar") == ["pa", "liar"]
    assert syllable_separator("instructivo") == ["ins", "truc", "ti", "vo"]
    assert syllable_separator("antiguo") == ["an", "ti", "guo"]
    assert syllable_separator("lío") == ["lí", "o"]
    assert syllable_separator("obstinado") == ["obs", "ti", "na", "do"]
