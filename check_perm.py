import unittest
import hypothesis
from hypothesis import given, assume
import hypothesis.strategies as st

def check_is_perm(string1, string2):
    """return True if string1 is a permutation of string2, False otherwise."""
    for character in repr(string1):
        if character in repr(string2):
            string2= repr(string2).replace(character, '', 1)
        else:
            return False


    return True


class TestPerm(unittest.TestCase):
    @given(st.text(), st.text())
    def test_perm_smoke(self, str1, str2):
        check_is_perm(str1, str2)


    @given(st.from_regex(r"^(.+)(-)(?!\1)(.+)$"))  # this isn't right...
    def test_perm_false(self, test_str):
        str1, str2 = test_str.split('-', 1)
        self.assertFalse(check_is_perm(str1, str2))  # fails when one is empty and one is white space.


    @given(st.from_regex(r"^(.*)(-)(.*)(?=\1)(.*)"))
    def test_perm_true(self, test_str):
        str1, str2 = test_str.split('-', 1)
        self.assertTrue(check_is_perm(str1, str2))



        
if __name__ == "__main__":
#    unittest.main()
    if check_is_perm(' ', '\n'):
        print("True")
