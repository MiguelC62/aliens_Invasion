from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action

class CollideProjectilBombAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        projectil = cast.get_first_actor(PROJECTILS_GROUP)
        bomb = cast.get_first_actor(ALIENS_GROUP) 
        projectil_body = projectil.get_body()
        bomb_body = bomb.get_body()
        if self._physics_service.has_collided(projectil_body, bomb_body):
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
            cast.remove_actor(BOMBS_GROUP, bomb)
            cast.remove_actor(PROJECTILS_GROUP, projectil)
    
                
                
        
                
                
              
               