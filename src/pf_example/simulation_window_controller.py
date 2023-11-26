"""The GUI Controller of the Simulation."""

import atexit

import pygame


class SimulationWindowController:

    """SimulationController that uses a window."""

    def __init__(self):
        """Construct a SimulationWindowController."""
        pygame.init()
        self._screen = pygame.display.set_mode((1280, 720))
        self._clock = pygame.time.Clock()
        atexit.register(self.cleanup)

    def run(self):
        """Show the window until it is closed."""
        frames_per_sec = 60
        for _ in range(frames_per_sec): # Run for 1 second
            self._screen.fill("purple")
            pygame.display.flip()
            self._clock.tick(frames_per_sec)

    def cleanup(self):
        """Destroy a SimulationWindowController.

        I tried this destructor to be private,
        yet when I do, the tests never call it
        when measuring Codecov.
        Due to this, I call it manually in a test.
        """
        pygame.quit()
