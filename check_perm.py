import unittest
import hypothesis
from hypothesis import given, assume, settings
import hypothesis.strategies as st
from math import ceil
import random

def check_is_perm(string1, string2):
    """return True if string1 is a permutation of string2, False otherwise.
    Treats escape sequences as the constituting characters,
    so that \n is a permutation of n\, etc.,"""
    string1, string2 = repr(string1), repr(string2)
    if len(string2) != len(string1):
        return False

    string1 = string_to_dict(string1)
    string2 = string_to_dict(string2)
    string1["'"] -= 2
    string2["'"] -= 2
    for key, value in string1.items():
        if key not in string2 or value != string2[key]:
            return False


    return True


def string_to_dict(string):
    str_dictionary = {}
    for character in string:
        if character not in str_dictionary:
            str_dictionary[character] = 0

        str_dictionary[character] += 1
    
    return str_dictionary


class TestPerm(unittest.TestCase):
    @given(st.text(), st.text())
    def test_perm_smoke(self, str1, str2):
        check_is_perm(str1, str2)


    @given(st.text())
    def test_perm_true_identical(self, test_str):
        self.assertTrue(check_is_perm(test_str, test_str))


    @given(st.text())
    def test_perm_true_reversed(self, test_str):
        string_permed = test_str[::-1]
        self.assertTrue(check_is_perm(test_str, string_permed))


    @settings(suppress_health_check = hypothesis.HealthCheck.all())
    @given(st.text(), st.integers())
    def test_perm_true_scattered(self, test_string, rand_seed):
        random.seed(rand_seed)
        perm_string = test_string
        test_string = [c for c in test_string]
        random.shuffle(test_string)
        new_string = ''
        for c in test_string:
            new_string += c

        assume(perm_string != new_string)
        self.assertTrue(check_is_perm(new_string, perm_string))


    def test_permute_escape(self):
        test_string = 'n\x01'
        test_permuted = '\n01x'
        self.assertTrue(check_is_perm(test_string, test_permuted))


    def test_permute_escape_false(self):
        test_string=r'\\n'
        test_permuted=r'\n'
        self.assertFalse(check_is_perm(test_string, test_permuted))


    def test_permute_white_false(self):
        test_string=' '
        test_permuted=''
        self.assertFalse(check_is_perm(test_string, test_permuted))




if __name__ == "__main__":
    unittest.main()
#    text = "0000"
#    if check_is_perm('/000', text):
#        print("True\n", text)
#    else:
#        print("False\n", text)