from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action

class CollideBunkerAndBombAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
    
        
    def execute(self, cast, script, callback):
        bomb = cast.get_first_actor(BOMBS_GROUP)
        bunkers = cast.get_actors(BUNKER_GROUP) 
        # stats = cast.get_first_actor(STATS_GROUP)
        
        for bunker in bunkers:
            bomb_body = bomb.get_body()
            bunker_body = bunker.get_body()

            if self._physics_service.has_collided(bomb_body, bunker_body):
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                cast.remove_actor(BUNKER_GROUP, bunker)