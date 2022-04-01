from constants import *
from game.scripting.action import Action


class DrawBunkerAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        bunkers = cast.get_actors(BUNKER_GROUP)

        for bunker in bunkers:
            body = bunker.get_body()

            if bunker.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
            
            animation = bunker.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
