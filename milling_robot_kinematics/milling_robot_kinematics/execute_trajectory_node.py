import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from milling_robot_interfaces.action import JointTraj
from sensor_msgs.msg import JointState

class ExecuteTrajectoryServer(Node):
    def __init__(self):
        super().__init__('execute_trajectory_node')
        self.control_server = ActionServer(self, JointTraj, 'joint_traj', self.execute_trajectory_callback)
        self.joint_state_pub = self.create_publisher(JointState, 'joint_states', 10)

    def execute_trajectory_callback(self, goal_handle):
        self.get_logger().info('Executing trajectory...')
        
        for point in goal_handle.request.joint_traj.points:
            print(point)

        feedback_msg = JointTraj.Feedback()
        feedback_msg.percent = 0

        goal_handle.succeed()

        result = JointTraj.Result()
        result.success = True
        return result


def main(args=None):
    rclpy.init(args=args)
    execute_trajectory_server = ExecuteTrajectoryServer()
    rclpy.spin(execute_trajectory_server)


if __name__ == '__main__':
    main()