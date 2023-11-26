"""Tests all function in src.pf_example.Speed."""
import unittest

from src.pf_example.speed import (
    Speed,
)


class TestSpeed(unittest.TestCase):

    """Class to test the code in src.pf_example.speed."""

    def test_can_create_speed(self):
        """#28: Can construct a Speed."""
        Speed()
