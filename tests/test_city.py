import pytest

from city import CityFr

# --------         F i x t u r e s ---------------------
# https://docs.pytest.org/en/stable/reference/fixtures.html
#https://docs.pytest.org/en/stable/how-to/fixtures.html

@pytest.fixture
def city_marseille() -> CityFr:
    return CityFr("Marseille", 886_040, "13000")

@pytest.fixture
def city_ajaccio() -> CityFr:
    return CityFr("Ajaccio", 76_320, "20000")

@pytest.fixture
def city_bastia() -> CityFr:
    return CityFr("Bastia", 46_867, "20200")


@pytest.fixture
def city_saint_denis() -> CityFr:
    return CityFr("Saint-Denis", 155_634, "97400")

# --------  T e s t s    U n i t a i r e s ------------
def test_city_str(city_marseille: CityFr):
    assert "Marseille (13000)" == str(city_marseille)

def test_city_department_2_digits(city_marseille: CityFr):
    dept = city_marseille.department()
    assert "13" == dept

def test_city_department_2A(city_ajaccio: CityFr):
    dept = city_ajaccio.department()
    assert "2A" == dept

def test_city_department_2B(city_bastia: CityFr):
    dept = city_bastia.department()
    assert "2B" == dept

def test_city_department_dom_tom(city_saint_denis: CityFr):
    dept = city_saint_denis.department()
    assert "974" == dept