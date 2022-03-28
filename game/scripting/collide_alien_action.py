from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
#from game.casting.projectils import Projectils

class CollideAlienAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        projectil = cast.get_first_actor(PROJECTILS_GROUP)
        aliens = cast.get_actors(ALIENS_GROUP) 
        stats = cast.get_first_actor(STATS_GROUP)
        
        for alien in aliens:
            projectil_body = projectil.get_body()
            alien_body = alien.get_body()
            if self._physics_service.has_collided(projectil_body, alien_body):
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = alien.get_points()
                stats.add_points(points)
                cast.remove_actor(ALIENS_GROUP, alien)
                projectil.stop_moving()
                
                
        
                
                
              
               