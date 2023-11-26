"""Tests all function in src.pf_example.position."""
import unittest

from src.pf_example.simulation_parameters import (
    SimulationParameters,
)


class TestSimulationParameters(unittest.TestCase):

    """Class to test the code in src.pf_example.simulation_parameters."""

    def test_can_create_params(self):
        """#14: Can construct a SimulationParameters."""
        SimulationParameters("irrelevant.txt")

    def test_a_parameter_has_interaction_parameters(self):
        """#45: a Parameters has InteractionParams."""
        p = SimulationParameters("irrelevant.txt")
        p._interaction_parameters # noqa: B018, SLF001
