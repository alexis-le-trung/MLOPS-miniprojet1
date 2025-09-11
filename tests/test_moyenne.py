import pytest
from moyenne import compute_average


def test_moyenne_liste_non_vide():
    assert compute_average([1, 2, 3, 4, 5]) == 3

def test_moyenne_liste_vide():
    assert compute_average([]) == 0

def test_moyenne_valeurs_flottantes():
    assert compute_average([1.5, 2.5, 3.5]) == pytest.approx(2.5)

def test_moyenne_un_element():
    assert compute_average([10]) == 10

