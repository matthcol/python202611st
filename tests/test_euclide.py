import pytest

from euclide import gcd


def test_gcd_simple():
    a = 15
    b = 21
    assert 3 == gcd(a, b)


@pytest.mark.parametrize(
    "a, b, expected_gcd",
    [
        [1, 1, 1],
        [1, 5, 1],
        [5, 1, 1],
        [7, 13, 1],
        [15, 21, 3],
        [21, 15, 3],
        [354224848179261915075, 573147844013817084101, 1],
    ],
    ids=[
        "both 1",
        "first 1",
        "second 1",
        "primes",
        "a lesser than b",
        "a greater than b",
        "2 consecutive fibonacci nbs",
    ]
)
def test_gcd_ok(a, b, expected_gcd):
    assert expected_gcd == gcd(a, b)


@pytest.mark.parametrize(
    "a, b",
    [
        [0, 5],
        [5, 0],
        [0, 0],
        [-13, 5],
        [5, -13],
        [-13, -47],
    ],
    ids=[
        "first 0",
        "second 0",
        "both 0",
        "first negative",
        "second negative",
        "both negative",
    ]
)
def test_gcd_ko(a, b):
    # TODO: add a timeout
    with pytest.raises(ValueError):
        _ = gcd(a, b)

# NB: avec le typage déclaratif, pas la peine de rédiger ce type de test
# def test_gcd_dummy():
#     gcd(None, "toto")
