from constants import *
from game.scripting.action import Action


class ControlBombAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        bombs = cast.get_actors(BOMBS_GROUP)
        for bomb in bombs:
            if self._keyboard_service.is_key_down(SPACE):    
                bomb.release()
                
               
   
            
            
    
