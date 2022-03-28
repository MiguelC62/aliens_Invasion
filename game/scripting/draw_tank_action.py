from constants import *
from game.scripting.action import Action


class DrawTankAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        tank = cast.get_first_actor(TANK_GROUP)
        body = tank.get_body()

        if tank.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = tank.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)