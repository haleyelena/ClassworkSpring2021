import pytest 

@pytest.mark.parametrize("(a, b), (c, d), x, expected", [
    ((1, 2), (3, 4), 2, 3),
    ((1, 5), (4, 9), 3, 8)
])


def test_point_finder((a, b), (c, d), x, expected):
    from cw_211 import point_finder 
    answer = point_finder((a, b), (b, c), x)
    assert answer == expected