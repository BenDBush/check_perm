import unittest
import hypothesis
from hypothesis import given, assume
import hypothesis.strategies as st

def check_is_perm(string1, string2):
    """return True if string1 is a permutation of string2, False otherwise.
    Treats escape sequences as the constituting characters,
    so that \n is a permutation of n\a, etc.,"""
    for character in repr(string1):
        if character in repr(string2):
            string2= repr(string2).replace(character, '', 1)
        else:
            return False


    return True


class TestPerm(unittest.TestCase):
#    @given(st.text(), st.text())
#    def test_perm_smoke(self, str1, str2):
#        check_is_perm(str1, str2)


    @given(st.from_regex(r"^(.+)(-)(?!\1)(.+)$"))  # this isn't right...
    def test_perm_false(self, test_str):
        str1, str2 = test_str.split('-', 1)
        self.assertFalse(check_is_perm(str1, str2))


    @given(st.text(), st.text(), st.text())  # gives memory errors.
    def test_perm_true(self, test_str, pad_l, pad_r):
        string_permed = pad_l + test_str + pad_r
        self.assertTrue(check_is_perm(test_str, string_permed))


    @given(st.text(), st.text(), st.text())
    def test_perm_true_reversed(self, test_str, pad_l, pad_r):
        string_permed = str(pad_l) + test_str[::-1] + str(pad_r)
        self.assertTrue(check_is_perm(test_str, string_permed))


        
if __name__ == "__main__":
    unittest.main()
