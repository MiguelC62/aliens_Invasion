from constants import *
from game.scripting.action import Action


class DrawBombAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        bomb = cast.get_first_actor(BOMBS_GROUP)
        body = bomb.get_body()

        if bomb.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
        
        image = bomb.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)

        
        