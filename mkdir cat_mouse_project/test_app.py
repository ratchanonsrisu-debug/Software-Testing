import unittest
from app import cat_and_mouse

class TestCatMouse(unittest.TestCase):
    def test_cat_a_wins(self):
        # แมว A อยู่ใกล้กว่า (x=2, y=5, z=3 -> A ห่าง 1, B ห่าง 2)
        self.assertEqual(cat_and_mouse(2, 5, 3), "Cat A")

    def test_cat_b_wins(self):
        # แมว B อยู่ใกล้กว่า (x=1, y=3, z=2 -> A ห่าง 1, B ห่าง 1... ลอง x=1, y=5, z=4)
        self.assertEqual(cat_and_mouse(1, 5, 4), "Cat B")

    def test_mouse_escapes(self):
        # ระยะเท่ากัน (x=1, y=3, z=2)
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")
        