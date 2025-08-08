import pytest
import shared_items
def move_hero():
    return ("Hero Moved")



def test_1():
    assert move_hero() == "Hero Stopped"