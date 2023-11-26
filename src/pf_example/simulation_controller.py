"""SimulationController."""

from src.pf_example.simulation import (
    Simulation,
)


class SimulationController:

    """SimulationController is a Controller for a Simulation."""

    def __init__(self):
        """Create a SimulationController."""
        self._simulation = Simulation()
