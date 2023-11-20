"""Tests all function in src.pf_example.position."""
import unittest

from src.pf_example.position import (
    SimulationParameters,
)


class TestSimulationParameters(unittest.TestCase):

    """Class to test the code in src.pf_example.simulation_parameters."""

    def test_can_create_params(self):
        """#14: Can construct a SimulationParameters."""
        SimulationParameters()
