from constants import *
from game.scripting.action import Action


class MoveProjectilAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        projectils = cast.get_actors(PROJECTILS_GROUP)
        for x in range(1):
            projectil = projectils[x]
            body = projectil.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)
