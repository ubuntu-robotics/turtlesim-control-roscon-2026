# turtlesim-control-roscon-2026

Simple ROS 2 Jazzy Python package with one node that drives `turtlesim` in a square.

## Package

- `turtlesim_control_roscon_2026`
- One executable node: `draw_square`
- No launch file (intentional)

## Run

```bash
# Terminal 1
ros2 run turtlesim turtlesim_node

# Terminal 2
ros2 run turtlesim_control_roscon_2026 draw_square
```

The turtle will repeatedly draw a square.
