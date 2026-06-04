from glob import glob
import os


def test_entry_point_file_exists():
    pkg_dir = os.path.dirname(__file__)
    root = os.path.abspath(os.path.join(pkg_dir, '..'))
    matches = glob(os.path.join(root, 'turtlesim_control_roscon_2026', 'draw_square.py'))
    assert len(matches) == 1
