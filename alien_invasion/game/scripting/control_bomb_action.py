from constants import *
from game.scripting.action import Action
from game.casting.point import Point
import random

class ControlBombAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        bombs = cast.get_actors(BOMBS_GROUP)
        
        for bomb in bombs:
        # body = bomb.get_body()
        # x = random.randint(BOMBS_WIDTH, SCREEN_WIDTH - BOMBS_WIDTH)
        # y = FIELD_TOP + 4 * ALIENS_HEIGHT
        # position = Point(x,y)
        # body.set_position(position)
            bomb.release()
        # self._keyboard_service.is_key_down(SPACE):
        #cast.remove_actor(PROJECTILS_GROUP, projectil)
       