from game.casting.actor import Actor


class Alien(Actor):
    """A solid,  object that can be broken."""

    def __init__(self, body, animation, points, debug = False):
        """Constructs a new Alien.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._points = points
        
    def get_animation(self):
        """Gets the alien's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the alien's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the alien's points.
        
        Returns:
            A number representing the brick's points.
        """
        return self._points