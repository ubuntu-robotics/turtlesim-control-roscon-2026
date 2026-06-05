import os
import unittest


class TestPackageLayout(unittest.TestCase):
    def test_entry_point_file_exists(self):
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        target = os.path.join(root, 'turtlesim_control_roscon_2026', 'draw_square.py')
        self.assertTrue(os.path.isfile(target), f'Missing node file: {target}')


if __name__ == '__main__':
    unittest.main()
