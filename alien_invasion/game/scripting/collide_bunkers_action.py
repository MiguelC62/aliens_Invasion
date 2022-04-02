from operator import index
from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.animation import Animation
from game.casting.bunker import Bunker

class CollideBunkersAction(Action):

    def __init__(self, physics_service, audio_service, video_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._video_service = video_service
        self._index_bunker1 = 1
        self._index_bunker2 = 1
        self._index_bunker3 = 1

    def execute(self, cast, script, callback):
        
        projectil = cast.get_first_actor(PROJECTILS_GROUP)
        bunkers = cast.get_actors(BUNKER_GROUP)
        
        for bunker in bunkers:
            projectil_body = projectil.get_body()
            bunker_body = bunker.get_body()
            if self._physics_service.has_collided(projectil_body, bunker_body):
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                cast.remove_actor(PROJECTILS_GROUP, projectil)
                bunker_position = bunker_body.get_position()
                x = bunker_position.get_x()
                
                if x == ((CENTER_X-300) - BUNKER_WIDTH / 2):
                    index = self.destroy_bunker(cast, bunker, bunker_body, self._index_bunker1)
                    self._index_bunker1 = index
                elif x == ((CENTER_X) - BUNKER_WIDTH / 2):
                    index = self.destroy_bunker(cast, bunker, bunker_body, self._index_bunker2)
                    self._index_bunker2 = index
                elif x == ((CENTER_X + 300) - BUNKER_WIDTH / 2):
                    index = self.destroy_bunker(cast, bunker, bunker_body, self._index_bunker3)
                    self._index_bunker3 = index
                else:
                    cast.remove_actor(BUNKER_GROUP,bunker)
                

    def replace_image(self,cast, bunker, image, bunker_body):
        cast.remove_actor(BUNKER_GROUP, bunker)
        animation = Animation(image, BUNKER_RATE)
        bunker = Bunker(bunker_body, animation)
        cast.add_actor(BUNKER_GROUP, bunker)
        image = animation.next_image()
        position = bunker_body.get_position()
        self._video_service.draw_image(image, position)

    def destroy_bunker(self, cast, bunker, bunker_body, index):
        if index == 1:
            image = BUNKER_DESTROY5_IMAGE
            self.replace_image(cast, bunker, image, bunker_body)
            index += 1
        # elif index == 2:
        #     image = BUNKER_DESTROY2_IMAGE
        #     self.replace_image(cast, bunker, image, bunker_body)
        #     index += 1
        # elif index == 3:
        #     image = BUNKER_DESTROY3_IMAGE
        #     self.replace_image(cast, bunker, image, bunker_body)
        #     index += 1
        # elif index == 4:
        #     image = BUNKER_DESTROY4_IMAGE
        #     self.replace_image(cast, bunker, image, bunker_body)
        #     index += 1
        else:
            cast.remove_actor(BUNKER_GROUP, bunker)
            index = 1
        return index

    
                    
                