"""Simulation."""

from src.pf_example.particles import (
    Particles,
)


class Simulation:

    """Simulation manages the simulation."""

    def __init__(self):
        """Create a Simulation."""
        self._particles = Particles()
