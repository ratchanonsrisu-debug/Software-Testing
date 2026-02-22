import unittest
from logic import cat_and_mouse

class TestCatMouse(unittest.TestCase):
    def test_cat_a_wins(self):
        # Case: Cat A is closer
        self.assertEqual(cat_and_mouse(2, 5, 3), "Cat A")

    def test_cat_b_wins(self):
        # Case: Cat B is closer
        self.assertEqual(cat_and_mouse(1, 5, 4), "Cat B")

    def test_mouse_escapes(self):
        # Case: Both cats are at the same distance
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")