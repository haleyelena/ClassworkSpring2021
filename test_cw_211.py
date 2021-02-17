import pytest


@pytest.mark.parametrize("p1, p2, x, expected", [
    ((1, 2), (3, 4), 2, 3),
    ((1, 5), (5, 9), 3, 7)
])
def test_point_finder(p1, p2, x, expected):
    from cw_211 import point_finder
    answer = point_finder(p1, p2, x)
    assert answer == expected
