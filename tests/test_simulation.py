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

    def test_a_simulation_has_particles(self):
        """#41: a Simulation has Particles."""
        s = Simulation()
        s._particles # noqa: B018, SLF001

    def test_a_simulation_has_parameters(self):
        """#42: a Simulation has parameters."""
        s = Simulation()
        s._parameters # noqa: B018, SLF001

