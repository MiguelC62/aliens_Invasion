#import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Bombs(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Ball.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the ball's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
        
    def release(self):
        """Release the aliens projectile in a positions."""

        vy = BOMBS_VELOCITY
        vx = 0
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)
        

    def stop_moving(self):
        """Stops the bat from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)