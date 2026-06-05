import math
import unittest

from turtlesim_control_roscon_2026.square_controller import SquareController


class TestSquareController(unittest.TestCase):
    def test_moves_forward_initially(self):
        c = SquareController(side_length=2.0)
        lin, ang = c.update(5.0, 5.0, 0.0)
        self.assertGreater(lin, 0.0)
        self.assertEqual(ang, 0.0)

    def test_turns_after_side_length(self):
        c = SquareController(side_length=2.0)
        c.update(5.0, 5.0, 0.0)
        lin, ang = c.update(7.1, 5.0, 0.0)
        self.assertEqual(lin, 0.0)
        self.assertEqual(ang, 0.0)
        lin, ang = c.update(7.1, 5.0, 0.0)
        self.assertEqual(lin, 0.0)
        self.assertGreater(ang, 0.0)

    def test_resume_move_after_quarter_turn(self):
        c = SquareController(side_length=2.0)
        c.update(5.0, 5.0, 0.0)
        c.update(7.1, 5.0, 0.0)
        c.update(7.1, 5.0, 0.0)
        lin, ang = c.update(7.1, 5.0, math.pi / 2.0)
        self.assertEqual(lin, 0.0)
        self.assertEqual(ang, 0.0)
        lin, ang = c.update(7.1, 5.0, math.pi / 2.0)
        self.assertGreater(lin, 0.0)
        self.assertEqual(ang, 0.0)


if __name__ == '__main__':
    unittest.main()
