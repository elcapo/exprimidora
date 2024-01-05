import re

def has_weird_characters(word: str) -> bool:
    return not bool(re.compile(r'^[a-zA-ZñÑáéíóúüÁÉÍÓÚÜ]+$').search(word))

def is_vowel(word: str, position: int) -> bool:
    if position < 0 or position >= len(word):
        return False
    
    letter = word[position]
    
    if letter in ["a", "e", "i", "o", "á", "é", "í", "ó", "ú", "ü"]:
        return True
    
    if letter in ["u"]:
        previous_position = position - 1
        if previous_position < 0:
            return True
        previous_letter = word[previous_position]
        if previous_letter in ["g", "q"]:
            return False
        return True
    
    if letter == "y":
        next_position = position + 1
        if next_position >= len(word):
            return True
        return not is_vowel(word, next_position)
    
    return False

def is_strong_vowel(word: str, position: int) -> bool:
    if not is_vowel(word, position):
        return False
    
    if position >= len(word):
        return False
    
    letter = word[position]

    return letter in ["a", "e", "o", "á", "é", "í", "ó", "ú"]

def is_weak_vowel(word: str, position: int) -> bool:
    return is_vowel(word, position) and not is_strong_vowel(word, position)

def is_inseparable_consonant_pair(word: str, position: int) -> bool:
    if position < 0 or (position + 1) >= len(word):
        return False
    
    pair = word[position] + word[position + 1]
    
    return pair in ["gu", "qu", "ch", "ll", "rr", "bl", "br", "cl", "cr", "dr", "fl", "fr", "gl", "kl", "gr", "pl", "pr", "tr"]

def syllable_separator(word: str) -> list:
    if has_weird_characters(word):
        raise Exception("Invalid characters found")
    
    syllables = []
    position = len(word) - 1
    remaining = word

    while position >= 0:
        if position - 2 > 0 and is_vowel(remaining, position - 2) and not is_vowel(remaining, position - 1) and is_vowel(remaining, position):
            syllables.append(remaining[position - 1:])
            remaining = remaining[:position - 1]
            position -= 2
            continue
        if position - 2 > 0 and is_inseparable_consonant_pair(remaining, position - 2) and is_vowel(remaining, position):
            syllables.append(remaining[position - 2:])
            remaining = remaining[:position - 2]
            position -= 2
            continue
        if position - 3 > 0 and not is_vowel(remaining, position - 3) and not is_vowel(remaining, position - 2) and not is_vowel(remaining, position - 1) and is_vowel(remaining, position):
            syllables.append(remaining[position - 1:])
            remaining = remaining[:position - 1]
            position -= 2
            continue
        if position - 2 > 0 and not is_vowel(remaining, position - 2) and not is_vowel(remaining, position - 1) and is_vowel(remaining, position):
            syllables.append(remaining[position - 1:])
            remaining = remaining[:position - 1]
            position -= 2
            continue
        if is_strong_vowel(remaining, position - 1) and is_strong_vowel(remaining, position):
            syllables.append(remaining[position:])
            remaining = remaining[:position]
            position -= 1
            continue
        position -= 1

    if remaining != "":
        syllables.append(remaining)

    syllables = reversed(syllables)

    return [s for s in syllables]
