#!/usr/bin/env python3

import math

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
from turtlesim.msg import Pose


class DrawSquareNode(Node):
    def __init__(self) -> None:
        super().__init__('draw_square')

        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.timer = self.create_timer(0.05, self.control_loop)

        self.side_length = 2.0
        self.linear_speed = 1.0
        self.angular_speed = 1.0

        self.current_pose = None
        self.state = 'move'  # move | turn
        self.segment_start_x = None
        self.segment_start_y = None
        self.turn_start_theta = None

        self.get_logger().info('Draw square node started')

    def pose_callback(self, msg: Pose) -> None:
        self.current_pose = msg

        if self.segment_start_x is None:
            self.segment_start_x = msg.x
            self.segment_start_y = msg.y

    def _normalize_angle(self, angle: float) -> float:
        return math.atan2(math.sin(angle), math.cos(angle))

    def _distance_from_segment_start(self) -> float:
        if self.current_pose is None or self.segment_start_x is None or self.segment_start_y is None:
            return 0.0
        dx = self.current_pose.x - self.segment_start_x
        dy = self.current_pose.y - self.segment_start_y
        return math.hypot(dx, dy)

    def control_loop(self) -> None:
        if self.current_pose is None:
            return

        cmd = Twist()

        if self.state == 'move':
            if self._distance_from_segment_start() < self.side_length:
                cmd.linear.x = self.linear_speed
                cmd.angular.z = 0.0
            else:
                self.state = 'turn'
                self.turn_start_theta = self.current_pose.theta
                cmd.linear.x = 0.0
                cmd.angular.z = 0.0

        elif self.state == 'turn':
            if self.turn_start_theta is None:
                self.turn_start_theta = self.current_pose.theta

            turned = abs(self._normalize_angle(self.current_pose.theta - self.turn_start_theta))
            if turned < (math.pi / 2.0):
                cmd.linear.x = 0.0
                cmd.angular.z = self.angular_speed
            else:
                self.state = 'move'
                self.segment_start_x = self.current_pose.x
                self.segment_start_y = self.current_pose.y
                self.turn_start_theta = None
                cmd.linear.x = 0.0
                cmd.angular.z = 0.0

        self.cmd_pub.publish(cmd)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = DrawSquareNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        stop = Twist()
        node.cmd_pub.publish(stop)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
