from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action

from game.casting.label import Label
from game.casting.point import Point
from game.casting.text import Text 

class CollideTankAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        bomb = cast.get_first_actor(BOMBS_GROUP)
        tank = cast.get_first_actor(TANK_GROUP)
        projectil = cast.get_first_actor(PROJECTILS_GROUP)
        
        bomb_body = bomb.get_body()
        tank_body = tank.get_body()

        if self._physics_service.has_collided(bomb_body, tank_body):
            #ball.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
            #cast.clear_actors(TANK_GROUP)
            projectil.stop_moving()
            bomb.stop_moving()
            cast.clear_actors(DIALOG_GROUP)
            text = Text(WAS_GOOD_GAME, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
            position = Point(CENTER_X, CENTER_Y)
            label = Label(text, position)
            cast.add_actor(DIALOG_GROUP, label)
            self._audio_service.release()
    