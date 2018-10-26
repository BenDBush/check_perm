import unittest
import hypothesis
from hypothesis import given, assume
import hypothesis.strategies as st
from math import ceil

def check_is_perm(string1, string2):
    """return True if string1 is a permutation of string2, False otherwise.
    Treats escape sequences as the constituting characters,
    so that \n is a permutation of n\a, etc.,"""
    string1, string2 = repr(string1).replace("'", "", 2), repr(string2).replace("'", "", 2)
    for character in string1:
        if character in string2: # causing MemoryErrors.
            string2 = string2.replace(character, '', 1)  # causing the string to expand with \'s
        else:
            return False


    return True


class TestPerm(unittest.TestCase):
    @given(st.text(), st.text())
    def test_perm_smoke(self, str1, str2):
        check_is_perm(str1, str2)


#    @given(st.from_regex(r"^(.+)(-)(?!\1)(.+)$"))  # this isn't right...
#    def test_perm_false(self, test_str):
#        str1, str2 = test_str.split('-', 1)
#        self.assertFalse(check_is_perm(str1, str2))


    @given(st.text(), st.text())  # gives memory errors.
    def test_perm_true(self, test_str, pad_text):
        string_permed = str(pad_text[:ceil(len(pad_text)/2)]) + test_str + str(pad_text[ceil(len(pad_text)/2):])
        self.assertTrue(check_is_perm(test_str, string_permed))


    @given(st.text(), st.text())
    def test_perm_true_reversed(self, test_str, pad_text):
        string_permed = str(pad_text[:ceil(len(pad_text)/2)]) + test_str[::-1] + str(pad_text[ceil(len(pad_text)/2):])
        self.assertTrue(check_is_perm(test_str, string_permed))


    def test_permute_escape(self):
        test_string = 'n\x01'
        test_permuted = '\n01x'
        self.assertTrue(check_is_perm(test_string, test_permuted))


    def test_permute_escape_false(self):
        test_string='\\n'
        test_permuted='\n'
        self.assertFalse(check_is_perm(test_string, test_permuted))


    def test_permute_white_false(self):
        test_string=' '
        test_permuted=''
        self.assertFalse(check_is_perm(test_string, test_permuted))




if __name__ == "__main__":
    unittest.main()
#    text = "'"
#    if check_is_perm('', text):
#        print("True\n", text)
#    else:
#        print("False\n", text)