from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBombsAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        #bombs = cast.get_actors(BOMBS_GROUP)
        bomb = cast.get_first_actor(BOMBS_GROUP)
        bunker = cast.get_first_actor(BUNKER_GROUP)
        bomb_body = bomb.get_body()
        bunker_body = bunker.get_body()
        #for bomb in bombs:
        bomb_body = bomb.get_body()
        position = bomb_body.get_position()
        y = position.get_y()
       
        if y >= (FIELD_BOTTOM - BOMBS_WIDTH):
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
            cast.remove_actor(BOMBS_GROUP, bomb)
            #projectil.stop_moving()

        if self._physics_service.has_collided(bomb_body, bunker_body):
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
            cast.remove_actor(BOMBS_GROUP, bomb)
            
    