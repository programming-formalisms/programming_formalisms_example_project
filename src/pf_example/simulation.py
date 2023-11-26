"""Simulation."""

from src.pf_example.particles import (
    Particles,
)
from src.pf_example.simulation_parameters import (
    SimulationParameters,
)


class Simulation:

    """Simulation manages the simulation."""

    def __init__(self):
        """Create a Simulation."""
        self._parameters = SimulationParameters(
            "filename",
        )
        self._particles = Particles()
