"""SimulationControllers."""

import atexit
import pygame

class SimulationWindowController:

    """SimulationController that uses a window."""

    def __init__(self):
        """Constructor"""
        pygame.init()
        self._screen = pygame.display.set_mode((1280, 720))
        self._clock = pygame.time.Clock()
        atexit.register(self.cleanup)

    def start(self):
        self._screen.fill("purple")
        pygame.display.flip()
        self._clock.tick(60) 

    def cleanup(self):
        """Destructor"""
        pygame.quit()


class SimulationTerminalController:

    """SimulationController that uses a terminal."""
