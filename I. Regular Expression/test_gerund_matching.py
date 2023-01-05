"""Test gerund-matching regular expression.

Heather Qiu
September 2022

"""

import re
import pytest

# *** ADD YOUR PATTERN BELOW *** #
pattern = r"\w\w+ing"
#raise NotImplementedError("Add your pattern to the test file.")
# *** ADD YOUR PATTERN ABOVE *** #


test_cases = [
    ("writing in english is difficult", True),
    ("seeing is believing", True),
    ("ling loves to sing",False), 
    ("Ana likes having a cup of coffee every morning", True),
    ("that is an interesting idea", True),
    ("she bought a painting from the art fair", True),
    ("someone is swimming in the pool", True),
    ("_0ing is nonsense", True)
]


@pytest.mark.parametrize("string,matches", test_cases)
def test_gerund_matching(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert (re.search(pattern, string) is not None) == matches
