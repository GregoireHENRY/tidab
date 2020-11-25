"""
test tidab
"""

from tidab.tidab import hello


def test_hello() -> None:
    """hello test"""
    hello()
    assert True
