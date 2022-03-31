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
        # projectil = cast.get_first_actor(PROJECTILS_GROUP)
        
        bomb_body = bomb.get_body()
        tank_body = tank.get_body()

        if self._physics_service.has_collided(bomb_body, tank_body):
            stats = cast.get_first_actor(STATS_GROUP)
            stats.lose_life()


            if stats.get_lives() > 0:
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                callback.on_next(TRY_AGAIN)
            else:
                callback.on_next(GAME_OVER)
                sound = Sound(OVER_SOUND)
                self._audio_service.play_sound(sound)
    