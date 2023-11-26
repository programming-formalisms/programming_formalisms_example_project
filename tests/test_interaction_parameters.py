"""Tests all function in src.pf_example.position."""
import unittest

from src.pf_example.interaction_parameters import (
    InteractionParameters,
)


class TestInteractionParameters(unittest.TestCase):

    """Class to test the code in src.pf_example.Interaction_parameters."""

    def test_can_create_params(self):
        """#46: Can construct a InteractionParameters."""
        InteractionParameters()
