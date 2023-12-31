"""Tests all function in src.pf_example.simulation_terminal_controller."""
import unittest

from src.pf_example.simulation_terminal_controller import (
    SimulationTerminalController,
)


class TestSimulationTerminalController(unittest.TestCase):

    """Class to test the code in src.pf_example.simulation_terminal_controller."""

    def test_can_create_terminal_controller(self):
        """#7: Can construct a SimulationTerminalController."""
        SimulationTerminalController()
        self.assertTrue(1 + 2 == 2 + 1)

    def test_can_create_simulation_terminal_controller(self):
        """#27: Can construct a SimulationTerminalController."""
        SimulationTerminalController()
