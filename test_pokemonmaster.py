from pokemonmaster import *


def test_lose_health():
    charmender = Pokemon("Charmender", 15, "Fire", 100, 100, "No")

    charmender.lose_health(20)
    assert charmender.current_health == 80


def test_gain_health():
    charizard = Pokemon("Charizard", 15, "Fire", 100, 100, "No")

    charizard.gain_health(20)
    assert charizard.current_health == 100


def test_knockout_pokemon():
    charizard = Pokemon("Charizard", 15, "Fire", 100, 20, "No")
    charizard.lose_health(20)

    assert charizard.knocked_out == "Yes"


def test_revive_pokemon():
    charizard = Pokemon("Charizard", 15, "Fire", 150, 150, "No")
    charizard.lose_health(150)
    charizard.revive_pokemon()
    assert charizard.knocked_out == "No"


def test_attack():
    charmender = Pokemon("Charmender", 15, "Fire", 100, 100, "No")
    bulbasaur = Pokemon("Bulbasaur", 10, "Grass", 100, 100, "No")

    while bulbasaur.current_health >= 0:
        charmender.attack(bulbasaur)

    assert bulbasaur.knocked_out == "Yes"
