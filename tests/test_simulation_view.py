"""Tests all function in src.pf_example.simulation_view."""
import unittest

from src.pf_example.simulation_view import (
    SimulationView,
)


class TestSimulationView(unittest.TestCase):

    """Class to test the code in src.pf_example.simulation_view."""

    def test_can_create_simulation_view(self):
        """#30: Can construct a SimulationView."""
        SimulationView()
