"""Tests all function in src.pf_example.particles."""
import unittest

from src.pf_example.particles import (
    Particles,
)


class TestParticles(unittest.TestCase):

    """Class to test the code in src.pf_example.particles."""

    def test_can_create_particles(self):
        """#29: Can construct a Particles."""
        Particles()

    def test_particles_has_a_collection_of_particles(self):
        """#40: A Particles has a collection of particles."""
        p = Particles()
        p._particles # noqa: B018, SLF001
