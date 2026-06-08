#!/usr/bin/env python3

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
from turtlesim.msg import Pose

from turtlesim_control_roscon_2026.square_controller import SquareController


class DrawSquareNode(Node):
    def __init__(self) -> None:
        super().__init__('draw_square')

        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.timer = self.create_timer(0.001, self.control_loop)

        self.current_pose: Pose | None = None
        self.controller = SquareController(side_length=2.0)

        self.get_logger().info('Draw square node started')

    def pose_callback(self, msg: Pose) -> None:
        self.current_pose = msg

    def control_loop(self) -> None:
        if self.current_pose is None:
            return

        linear_x, angular_z = self.controller.update(
            self.current_pose.x,
            self.current_pose.y,
            self.current_pose.theta,
        )

        cmd = Twist()
        cmd.linear.x = linear_x
        cmd.angular.z = angular_z
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
