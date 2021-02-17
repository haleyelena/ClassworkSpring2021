import pytest 

@pytest.mark.parametrize("a, expected", [
    (65, "Normal"),
    (50, "Borderline Low"),
    (30, "Low"),
])


def test_analyze_HDL_normal(a, expected):
    from blood_tests import analyze_HDL 
    answer = analyze_HDL(a)
    assert answer == expected

   