"""Tests all function in src.pf_example.simulation_window_controller."""
import unittest

from src.pf_example.simulation_window_controller import (
    SimulationWindowController,
)


class TestSimulationWindowController(unittest.TestCase):

    """Class to test the code in src.pf_example.simulation_window_controller."""

    def test_can_create_simulation_window_controller(self):
        """#26: Can construct a SimulationWindowController."""
        SimulationWindowController()
