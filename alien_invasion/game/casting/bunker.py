from constants import *
from game.casting.actor import Actor



class Bunker(Actor):
       
    def __init__(self, body, animation, debug = False):
        """Constructs a new Bunker.
        
        Args:Args:
            body: A new instance of Body.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
    
    def get_animation(self):
        """Gets the bat's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation
     

    def get_body(self):
        """Gets the bunker's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    