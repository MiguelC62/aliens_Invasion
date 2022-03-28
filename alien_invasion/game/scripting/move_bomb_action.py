from constants import *
from game.scripting.action import Action

class MoveBombAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        bomb = cast.get_first_actor(BOMBS_GROUP)
        body = bomb.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)

    

        
