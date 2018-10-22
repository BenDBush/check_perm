import unittest
import hypothesis
from hypothesis import given
import hypothesis.strategies as st

def check_is_perm(string1, string2):
    pass


class TestPerm(unittest.TestCase):
    @given(st.text(), st.text())
    def test_perm_smoke(self, str1, str2):
        check_is_perm(str1, str2)


    @given(st.from_regex(r"^(.*)(-)(?![\1])(.*)$"))
    def test_perm_false(self, str):
        str1, str2 = str.split('-')
        self.assertFalse(check_is_perm(str1, str2))


    @given(st.from_regex(r"^(.*)(-)(?:[\1])(.*)$"))
    def test_perm_false(self, str1, str2):
        str1, str2 = str.split('-')
        self.assertFalse(str1, str2)



        
if __name__ == "__main__":
    unittest.main()