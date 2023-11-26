"""Tests all function in src.pf_example.simulation_terminal."""
import unittest

from src.pf_example.simulation_terminal import (
    SimulationTerminal,
)


class TestSimulationTerminal(unittest.TestCase):

    """Class to test the code in src.pf_example.simulation_terminal."""

    def test_can_create_simulation_terminal(self):
        """#31: Can construct a SimulationTerminal."""
        SimulationTerminal()
