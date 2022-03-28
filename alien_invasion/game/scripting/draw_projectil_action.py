from constants import *
from game.scripting.action import Action


class DrawProjectilAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        projectil = cast.get_first_actor(PROJECTILS_GROUP)
        body = projectil.get_body()

        if projectil.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = projectil.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)


