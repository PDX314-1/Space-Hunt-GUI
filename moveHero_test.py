#import pytest
import shared_items
def move_hero(angle_move, distance_move, game_state):
    """Moves the hero and updates the game state"""
    #   0 - right, 90 - up, 180 - left 270 - down
    
    x_current = game_state['x']
    y_current = game_state['y']
    
    match angle_move:
        case 0:
            game_state['x'] = x_current + distance_move

        case 90:
            game_state['y'] = y_current + distance_move

        case 180:
            game_state['x'] = x_current - distance_move

        case 270:
            game_state['y'] = y_current - distance_move
            
    return (game_state)


#print(move_hero(0,5,{'x':10, 'y':8, 'energy':1000, 'supplies': 100, 'money':1000, 'message':'&&&'}))

def test_1():
    assert move_hero(0,5,{'x':25, 'y':25, 'energy':1000, 'supplies': 100, 'money':1000, 'message':'&&&'}) == \
   {'x':30, 'y':25, 'energy':1000, 'supplies': 100, 'money':1000, 'message':'&&&'}
 
 def test_2():
    assert move_hero(90,5,{'x':25, 'y':25, 'energy':1000, 'supplies': 100, 'money':1000, 'message':'&&&'}) == \
   {'x':25, 'y':30, 'energy':1000, 'supplies': 100, 'money':1000, 'message':'+++'}
    
def test_3():
    assert move_hero(180,5,{'x':25, 'y':25, 'energy':1000, 'supplies': 100, 'money':1000, 'message':'&&&'}) == \
   {'x':20, 'y':25, 'energy':1000, 'supplies': 100, 'money':1000, 'message':'+++'}
    
def test_4():
    assert move_hero(270,5,{'x':25, 'y':25, 'energy':1000, 'supplies': 100, 'money':1000, 'message':'&&&'}) == \
   {'x':25, 'y':20, 'energy':1000, 'supplies': 100, 'money':1000, 'message':'+++'}