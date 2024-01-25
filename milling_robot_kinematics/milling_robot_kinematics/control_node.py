import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from milling_robot_interfaces.action import JointTrajectory
from sensor_msgs.msg import JointState


class MillingRobotControlServer(Node):

    def __init__(self):
        super().__init__('milling_robot_control_server')
        self.control_server = ActionServer(self, JointTrajectory, 'trajectory', self.trajectory_callback)
        self.joint_state_pub = self.create_publisher(JointState, 'joint_states', 10)

    def trajectory_callback(self, goal_handle):
        self.get_logger().info('Executing trajectory...')
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['Q1', 'Q2', 'Q3', 'D4']
        msg.position = [0.0, 0.0, 0.0, 0.0]

        self.joint_state_pub.publish(msg)

        feedback_msg = JointTrajectory.Feedback()
        feedback_msg.percent = 0

        goal_handle.succeed()

        result = JointTrajectory.Result()
        result.success = True
        return result


def main(args=None):
    rclpy.init(args=args)
    control_server = MillingRobotControlServer()
    rclpy.spin(control_server)


if __name__ == '__main__':
    main()