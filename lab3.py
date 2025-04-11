import string
import doctest
import unittest

def perfect_pangram(sentence: string):
    """Function that returns true if string is a perfect pangram
    and false if it isn't

    >>> correct_string = "Blowzy night-frumps vex'd Jack Q."
    >>> incorrect_string = "aabbccddeeffgghijklmnopqrstuvwxyz"
    >>> perfect_pangram(correct_string)
    True
    >>> perfect_pangram(incorrect_string)
    False
    >>> number = 90
    >>> bool = True
    >>> perfect_pangram(number)
    Not a string!
    False
    >>> perfect_pangram(bool)
    Not a string!
    False

    """
    if not isinstance(sentence, str):
        print("Not a string!")
        return False

    for char in string.ascii_lowercase:
        if sentence.lower().count(char) != 1:
            return False
    return True

class TestPerfectPangram(unittest.TestCase):
    def test_correctString(self):
        correct_string = "Blowzy night-frumps vex'd Jack Q."
        self.assertTrue(perfect_pangram(correct_string))
    
    def test_incorrectString(self):
        incorrect_string = "aabbccddeeffgghijklmnopqrstuvwxyz"
        self.assertFalse(perfect_pangram(incorrect_string))

    def test_integer(self):
        number = 90
        self.assertFalse(perfect_pangram(number))

    def test_bool(self):
        bool = True
        self.assertFalse(perfect_pangram(bool))

if __name__ == "__main__":
    doctest.testmod()
    unittest.main()