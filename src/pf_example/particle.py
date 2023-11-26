"""Particle."""

from src.pf_example.position import (
    Position,
)
from src.pf_example.speed import (
    Speed,
)


class Particle:

    """Particle is a particle."""

    def __init__(self):
        """Create a particle."""
        self._position = Position()
        self._speed = Speed()
