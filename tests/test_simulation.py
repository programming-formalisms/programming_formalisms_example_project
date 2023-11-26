"""Tests all function in src.pf_example.simulation."""
import unittest

from src.pf_example.simulation import (
    Simulation,
)


class TestSimulation(unittest.TestCase):

    """Class to test the code in src.pf_example.simulation."""

    def test_can_create_params(self):
        """#26: Can construct a Simulation."""
        Simulation()
