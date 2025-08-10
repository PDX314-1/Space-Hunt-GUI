import pytest
import shared_items
def move_hero(angle_move, distance_move, game_state):
    x_current = game_state['x']
    y_current = game_state['y']
    print("X: ",x_current,"     Y: ",y_current)
    return ("Hero Moved")



def test_1():
    assert move_hero(0,1,{'x':0, 'y':0, 'energy':1000, 'supplies': 100, 'money':1000, 'message':''}) == "Hero Moved"

#move_hero(0,1,{'x':10, 'y':20, 'energy':1000, 'supplies': 100, 'money':1000, 'message':''})