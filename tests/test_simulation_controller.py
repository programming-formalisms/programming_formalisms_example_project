"""Tests all function in src.pf_example.simulation_controller."""
import unittest

from src.pf_example.simulation_controller import (
    SimulationTerminalController,
    SimulationWindowController,
)


class TestSimulationTerminalController(unittest.TestCase):

    """Class to test the code in src.pf_example.simulation_terminal_controller."""

    def test_can_create_terminal_controller(self):
        """#7: Can construct a SimulationTerminalController."""
        SimulationTerminalController()
        self.assertTrue(1 + 2 == 2 + 1)

class TestSimulationWindowController(unittest.TestCase):

    """Class to test the code in src.pf_example.simulation_window_controller."""

    def test_can_create_terminal_controller(self):
        """#8: Can construct a SimulationTerminalController."""
        c = SimulationWindowController()
        c.run()

    """
    TODO
    def test_is_zero(self):
        '''Test 'is_zero'.'''
        self.assertIsNotNone(is_zero.__doc__)
        self.assertTrue(is_zero(0))
        self.assertTrue(is_zero(0.0))
        self.assertFalse(is_zero(1))
        self.assertRaises(TypeError, is_zero, {1, 2})
        self.assertRaises(TypeError, is_zero, "I am a string")
    """
