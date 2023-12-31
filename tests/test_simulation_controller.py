"""Tests all function in src.pf_example.simulation_controller."""
import unittest

from src.pf_example.simulation_controller import (
    SimulationController,
)


class TestSimulationController(unittest.TestCase):

    """Class to test the code in src.pf_example.simulation_controller."""

    def test_can_create_simulation_controller(self):
        """#33: Can construct a SimulationController."""
        SimulationController()

    def test_controller_has_a_simulation(self):
        """#43: a SimulationController has a Simulation."""
        c = SimulationController()
        c._simulation # noqa: B018, SLF001

    def test_controller_has_a_view(self):
        """#44: a SimulationController has a View."""
        c = SimulationController()
        c._view # noqa: B018, SLF001

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
