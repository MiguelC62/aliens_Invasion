from constants import *
from game.scripting.action import Action


class MoveProjectilAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        projectil = cast.get_first_actor(PROJECTILS_GROUP)
        body = projectil.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
