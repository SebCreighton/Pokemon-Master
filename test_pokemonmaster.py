import pytest
from pokemonmaster import *


#@pytest.mark.parametrize("charmender", "")

@pytest.fixture
def charmender():
    charmender = Pokemon("Charmender", 15, "Fire", 100, 100, "No")

    return charmender

@pytest.fixture
def charizard():
    charizard = Pokemon("Charizard", 15, "Fire", 100, 100, "No")

    return charizard

@pytest.fixture
def bulbasaur():
    bulbasaur = Pokemon("Bulbasaur", 10, "Grass", 100, 100, "No")

    return bulbasaur

def test_lose_health(charmender):

    charmender.lose_health(20)
    assert charmender.current_health == 80


def test_gain_health(charizard):

    charizard.gain_health(20)
    assert charizard.current_health == 100


def test_knockout_pokemon(charizard):
    charizard.lose_health(100)

    assert charizard.knocked_out == "Yes"


def test_revive_pokemon(charizard):
    charizard.lose_health(150)
    charizard.revive_pokemon()
    assert charizard.knocked_out == "No"

def test_attack(bulbasaur, charmender):

    while bulbasaur.current_health > 0:
        charmender.attack(bulbasaur)

    assert bulbasaur.knocked_out == "Yes"
