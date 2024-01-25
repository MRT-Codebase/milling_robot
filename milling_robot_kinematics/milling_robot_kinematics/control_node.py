import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from milling_robot_interfaces.action import Waypoint
from geometry_msgs.msg import Point

class ControlClient(Node):
    def __init__(self):
        super().__init__('control_node')
        self.trajectory_generation_client = ActionClient(self, Waypoint, 'waypoint')

    def send_goal(self):
        goal_msg = Waypoint.Goal()
        for i in range(5):
            msg = Point()
            msg.x = 10.0
            msg.y = 20.0
            msg.z = 5.0
            goal_msg.waypoint.waypoints.append(msg)

        self.trajectory_generation_client.wait_for_server()

        self._send_goal_future = self.trajectory_generation_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.trajectory))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.percent))


def main(args=None):
    rclpy.init(args=args)
    control_client = ControlClient()
    control_client.send_goal()
    rclpy.spin(control_client)


if __name__ == '__main__':
    main()