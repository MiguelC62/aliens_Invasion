from constants import *
from game.scripting.action import Action

class MoveBombAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        bombs = cast.get_actors(BOMBS_GROUP)
        for x in range(1):
            bomb = bombs[x]
            body = bomb.get_body()
            position = body.get_position()
            velocity = body.get_velocity() 
            position = position.add(velocity)
            body.set_position(position)
            
   