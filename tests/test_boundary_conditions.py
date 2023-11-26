"""Tests all function in src.pf_example.position."""
import unittest

from src.pf_example.boundary_conditions import (
    BoundaryConditions,
)


class TestBoundaryConditions(unittest.TestCase):

    """Class to test the code in src.pf_example.boundary_conditions."""

    def test_can_create_params(self):
        """#47: Can construct a BoundaryConditions."""
        BoundaryConditions()
