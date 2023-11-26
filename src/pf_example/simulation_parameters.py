"""The parameters of the Simulation."""

from src.pf_example.interaction_parameters import (
    InteractionParameters,
)


class SimulationParameters:

    """The parameters of the Simulation."""

    def __init__(self, filename): # noqa: ARG002
        """Create the parameters from file."""
        self._interaction_parameters = InteractionParameters()

