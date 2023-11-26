"""Tests all function in src.pf_example.simulation_window."""
import unittest

from src.pf_example.simulation_window import (
    SimulationWindow,
)


class TestSimulationWindow(unittest.TestCase):

    """Class to test the code in src.pf_example.simulation_window."""

    def test_can_create_simulation_window(self):
        """#26: Can construct a SimulationWindow."""
        SimulationWindow()
