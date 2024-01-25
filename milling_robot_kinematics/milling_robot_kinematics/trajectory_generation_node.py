import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from milling_robot_interfaces.action import Waypoint

class TrajectoryGenerationServer(Node):
    def __init__(self):
        super().__init__('trajectory_generation_node')
        self.trajectory_generation_server = ActionServer(self, Waypoint, 'waypoint', self.generate_trajectory_callback)

    def generate_trajectory_callback(self, goal_handle):
        self.get_logger().info('Converting waypoints to trajectory...')
        
        for point in goal_handle.request.waypoint.waypoints:
            print(point)
            time.sleep(10)

        feedback_msg = Waypoint.Feedback()
        feedback_msg.percent = 0

        goal_handle.succeed()

        result = Waypoint.Result()
        return result


def main(args=None):
    rclpy.init(args=args)
    trajectory_generation_server = TrajectoryGenerationServer()
    rclpy.spin(trajectory_generation_server)


if __name__ == '__main__':
    main()