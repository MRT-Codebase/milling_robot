from PySide6.QtWidgets import QApplication, QMainWindow
from .ui_file import Ui_MainWindow
from .kinematic_model import KinematicModel

import math
import threading
import numpy as np

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from nav_msgs.msg import Path
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped
from trajectory_msgs.msg import JointTrajectoryPoint
from milling_robot_interfaces.action import JointTraj

class ControlPanel(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.robot = KinematicModel(45, 42, 25, [0, 0, 0, 0, 0, 0])

        self.ui.q1_minus.clicked.connect(self.q1_minus_click)
        self.ui.q1_plus.clicked.connect(self.q1_plus_click)
        self.ui.q2_minus.clicked.connect(self.q2_minus_click)
        self.ui.q2_plus.clicked.connect(self.q2_plus_click)
        self.ui.q3_minus.clicked.connect(self.q3_minus_click)
        self.ui.q3_plus.clicked.connect(self.q3_plus_click)
        self.ui.d4_minus.clicked.connect(self.d4_minus_click)
        self.ui.d4_plus.clicked.connect(self.d4_plus_click)
        self.ui.x_minus.clicked.connect(self.x_minus_click)
        self.ui.x_plus.clicked.connect(self.x_plus_click)
        self.ui.y_minus.clicked.connect(self.y_minus_click)
        self.ui.y_plus.clicked.connect(self.y_plus_click)
        self.ui.z_minus.clicked.connect(self.z_minus_click)
        self.ui.z_plus.clicked.connect(self.z_plus_click)
        self.ui.add_waypoint.clicked.connect(self.add_waypoint_click)
        self.ui.reset_waypoints.clicked.connect(self.reset_waypoints_click)
        self.ui.play.clicked.connect(self.play_click)

        self.update_state()

        rclpy.init()
        self.node = Node("control_panel_node")

        self.timer = self.node.create_timer(0.1, self.timer_callback)
        
        self.joint_state_pub = self.node.create_publisher(JointState, 'joint_states', 10)
        
        self.trajectory_pub = self.node.create_publisher(Path, 'trajectory', 10)
        self.trajectory = Path()
        self.trajectory.header.frame_id = "trajectory"
        self.trajectory_running = False
        self.trajectory_client = ActionClient(self, JointTraj, 'joint_traj')

        self.ros_thread = threading.Thread(target=self.run_ros_node)
        self.ros_thread.daemon = True
        self.ros_thread.start()

    def run_ros_node(self):
        try:
            while rclpy.ok():
                rclpy.spin_once(self.node, timeout_sec=0.1)
        except KeyboardInterrupt:
            pass

    def timer_callback(self):
        if not self.trajectory_running:
            msg = JointState()
            msg.header.stamp = self.node.get_clock().now().to_msg()
            for joint, val in self.robot.current_joint_state.items():
                msg.name.append(joint)
                if (joint == 'D4' or joint == 'G1' or joint == 'G2'):
                    msg.position.append(val/1000.0)
                else:
                    msg.position.append(math.radians(val))
            self.joint_state_pub.publish(msg)
        self.trajectory_pub.publish(self.trajectory)

    def update_state(self):
        self.ui.q1_val.setText(f"{self.robot.current_joint_state['Q1']:.2f}")
        self.ui.q2_val.setText(f"{self.robot.current_joint_state['Q2']:.2f}")
        self.ui.q3_val.setText(f"{self.robot.current_joint_state['Q3']:.2f}")
        self.ui.d4_val.setText(f"{self.robot.current_joint_state['D4']:.2f}")
        self.ui.x_val.setText(f"{self.robot.current_cartesian_state['X']:.2f}")
        self.ui.y_val.setText(f"{self.robot.current_cartesian_state['Y']:.2f}")
        self.ui.z_val.setText(f"{self.robot.current_cartesian_state['Z']:.2f}")

    def interpolate(self, resolution=100):
        interpolated_points = []

        for i in range(len(self.trajectory.poses)-1):

            point1 = np.array([-self.trajectory.poses[i].pose.position.x*1000, -self.trajectory.poses[i].pose.position.y*1000, self.trajectory.poses[i].pose.position.z*1000])
            point2 = np.array([-self.trajectory.poses[i+1].pose.position.x*1000, -self.trajectory.poses[i+1].pose.position.y*1000, self.trajectory.poses[i+1].pose.position.z*1000])

            for i in range(resolution):
                alpha = i / (resolution - 1)
                interpolated_point = (1 - alpha) * point1 + alpha * point2
                interpolated_points.append(interpolated_point)

        return np.array(interpolated_points)

    def q1_minus_click(self):
        result =self.robot.movej_rel('Q1', -self.ui.q1_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def q1_plus_click(self):
        result = self.robot.movej_rel('Q1', self.ui.q1_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def q2_minus_click(self):
        result =self.robot.movej_rel('Q2', -self.ui.q2_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def q2_plus_click(self):
        result = self.robot.movej_rel('Q2', self.ui.q2_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def q3_minus_click(self):
        result =self.robot.movej_rel('Q3', -self.ui.q3_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def q3_plus_click(self):
        result = self.robot.movej_rel('Q3', self.ui.q3_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def d4_minus_click(self):
        result =self.robot.movej_rel('D4', -self.ui.d4_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def d4_plus_click(self):
        result = self.robot.movej_rel('D4', self.ui.d4_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def x_minus_click(self):
        result =  self.robot.movel_rel('X', -self.ui.x_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def x_plus_click(self):
        result =   self.robot.movel_rel('X', self.ui.x_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def y_minus_click(self):
        result =  self.robot.movel_rel('Y', -self.ui.y_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def y_plus_click(self):
        result =   self.robot.movel_rel('Y', self.ui.y_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def z_minus_click(self):
        result =  self.robot.movel_rel('Z', -self.ui.z_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def z_plus_click(self):
        result =   self.robot.movel_rel('Z', self.ui.z_inc.value())
        self.ui.statusbar.showMessage(result)
        self.update_state()

    def add_waypoint_click(self):
        self.trajectory.header.stamp = self.node.get_clock().now().to_msg()
        new_point = PoseStamped()
        new_point.pose.position.x = -(self.robot.current_cartesian_state['X'] / 1000.0)
        new_point.pose.position.y = -(self.robot.current_cartesian_state['Y'] / 1000.0)
        new_point.pose.position.z = self.robot.current_cartesian_state['Z'] / 1000.0
        self.trajectory.poses.append(new_point)

    def reset_waypoints_click(self):
        self.trajectory.poses.clear()

    def play_click(self):
        self.trajectory_running = True
        joint_limit_error = False
        joints = []
        inter_points = self.interpolate()
        for point in inter_points:
            j = self.robot.IKM(point[0], point[1], point[2])
            result = self.robot.check_limits(j[0], j[1], j[2])
            if result:
                joints.append(j)
            else:
                joint_limit_error = True
                break
        if joint_limit_error:
            self.ui.statusbar.showMessage("Trajectory contains points where joint limit exceeds")
        else:
            self.ui.statusbar.showMessage("Running trajectory")
            self.send_goal(joints)

    def send_goal(self, joints):
        goal_msg = JointTraj.Goal()
        for joint in joints:
            joint_point_msg = JointTrajectoryPoint()
            joint_point_msg.positions = joint
            goal_msg.joint_traj.points.append(joint_point_msg)

        self.trajectory_client.wait_for_server()

        self._send_goal_future = self.trajectory_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            self.trajectory_running = False
            return

        self.get_logger().info('Goal accepted :)')
        self.trajectory_running = False
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.success))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.percent))


def main():
    app = QApplication([])
    window = ControlPanel()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
