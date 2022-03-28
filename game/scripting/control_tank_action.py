from constants import *
from game.scripting.action import Action


class ControlTankAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        tank = cast.get_first_actor(TANK_GROUP)
        projectil = cast.get_first_actor(PROJECTILS_GROUP)
        
        if self._keyboard_service.is_key_down(LEFT): 
            tank.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            tank.swing_right()
        elif self._keyboard_service.is_key_down(SPACE):
            tank_body = tank.get_body()
            projectil_body = projectil.get_body()
            tank_position = tank_body.get_position()
            projectil_body.set_position(tank_position)
            projectil.release()
            #cast.remove_actor(PROJECTILS_GROUP, projectil)
        else: 
            tank.stop_moving()        