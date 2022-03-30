from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBunkerAndProjectileAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
        
    def execute(self, cast, script, callback):
        projectile = cast.get_first_actor(PROJECTILS_GROUP)
        bunkers = cast.get_actors(BUNKER_GROUP)
    
        
        for bunker in bunkers:
            projectile_body = projectile.get_body()
            bunker_body = bunker.get_body()
            
            if self._physics_service.has_collided(projectile_body, bunker_body):
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                cast.remove_actor(BUNKER_GROUP, bunker)