import math


class SquareController:
    def __init__(self, side_length: float = 2.0) -> None:
        self.side_length = side_length
        self.state = 'move'
        self.segment_start_x: float | None = None
        self.segment_start_y: float | None = None
        self.turn_start_theta: float | None = None

    @staticmethod
    def normalize_angle(angle: float) -> float:
        return math.atan2(math.sin(angle), math.cos(angle))

    def update(self, x: float, y: float, theta: float) -> tuple[float, float]:
        if self.segment_start_x is None:
            self.segment_start_x = x
            self.segment_start_y = y

        if self.state == 'move':
            dx = x - self.segment_start_x
            dy = y - self.segment_start_y
            if math.hypot(dx, dy) < self.side_length:
                return (1.0, 0.0)
            self.state = 'turn'
            self.turn_start_theta = theta
            return (0.0, 0.0)

        # turn state
        if self.turn_start_theta is None:
            self.turn_start_theta = theta

        turned = abs(self.normalize_angle(theta - self.turn_start_theta))
        if turned < (math.pi / 2.0):
            return (0.0, 1.0)

        self.state = 'move'
        self.segment_start_x = x
        self.segment_start_y = y
        self.turn_start_theta = None
        return (0.0, 0.0)
