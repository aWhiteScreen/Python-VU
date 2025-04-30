import string

def perfect_pangram(sentence: str) -> bool:
    if not isinstance(sentence, str):
        print("Not a string!")
        return False

    for char in string.ascii_lowercase:
        if sentence.lower().count(char) != 1:
            return False
    return True
