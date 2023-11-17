"""Tests all function in src.pf_example.position."""
import unittest

from src.pf_example.position import (
    Position,
)


class TestPosition(unittest.TestCase):

    """Class to test the code in src.pf_example.position."""

    def test_can_create_position(self):
        """#15: Can construct a Position."""
        Position()
        self.assertTrue(1 + 2 == 2 + 1)

    def test_origin_created(self):
        """#16: A Position can its x and y read."""
        c = Position()
        self.assertEqual(c.get_x(), 0.0)
        self.assertEqual(c.get_y(), 0.0)
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
