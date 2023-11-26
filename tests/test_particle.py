"""Tests all function in src.pf_example.particle."""
import unittest

from src.pf_example.particle import (
    Particle,
)


class TestParticle(unittest.TestCase):

    """Class to test the code in src.pf_example.particle."""

    def test_can_create_particle(self):
        """#28: Can construct a Particle."""
        Particle()

    def test_particle_has_a_position(self):
        """#38: Can construct a Particle."""
        p = Particle()
        p._position # noqa(B108, SLF001)
