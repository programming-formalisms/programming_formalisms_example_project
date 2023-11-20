"""SimulationControllers."""

import atexit

import pygame


class SimulationWindowController:

    """SimulationController that uses a window."""

    def __init__(self):
        """Construct a SimulationWindowController."""
        pygame.init()
        self._screen = pygame.display.set_mode((1280, 720))
        self._clock = pygame.time.Clock()
        atexit.register(self._cleanup)

    def run(self):
        """Show the window until it is closed."""
        frames_per_sec = 60
        for _ in range(0, frames_per_sec): # Run for 1 second
            self._screen.fill("purple")
            pygame.display.flip()
            self._clock.tick(frames_per_sec)

    def _cleanup(self):
        """Destroy a SimulationWindowController."""
        pygame.quit()


class SimulationTerminalController:

    """SimulationController that uses a terminal."""
