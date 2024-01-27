from PySide6.QtWidgets import QApplication, QMainWindow
from .ui_file import Ui_MainWindow

import math
import threading

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import JointState
from milling_robot_interfaces.msg import Waypoint

class ControlPanel(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.q1_minus.clicked.connect(self.q1_minus_click)
        self.ui.q1_plus.clicked.connect(self.q1_plus_click)
        self.ui.q2_minus.clicked.connect(self.q2_minus_click)
        self.ui.q2_plus.clicked.connect(self.q2_plus_click)
        self.ui.q3_minus.clicked.connect(self.q3_minus_click)
        self.ui.q3_plus.clicked.connect(self.q3_plus_click)
        self.ui.d4_minus.clicked.connect(self.d4_minus_click)
        self.ui.d4_plus.clicked.connect(self.d4_plus_click)

        self.current_joint_state = {
            'Q1': 0.0,
            'Q2': 0.0,
            'Q3': 0.0,
            'D4': 0.0
        }

        self.current_cartesian_state = {
            'X': 0.0,
            'Y': 0.0,
            'Z': 0.0
        }

        rclpy.init()
        self.node = Node("control_panel_node")

        self.joint_state_pub = self.node.create_publisher(JointState, 'joint_states', 10)
        self.joint_state_timer = self.node.create_timer(0.1, self.joint_state_pub_callback)

        self.ros_thread = threading.Thread(target=self.run_ros_node)
        self.ros_thread.daemon = True
        self.ros_thread.start()

    def run_ros_node(self):
        try:
            while rclpy.ok():
                rclpy.spin_once(self.node, timeout_sec=0.1)
        except KeyboardInterrupt:
            pass

    def joint_state_pub_callback(self):
        msg = JointState()
        msg.header.stamp = self.node.get_clock().now().to_msg()
        for joint, val in self.current_joint_state.items():
            msg.name.append(joint)
            msg.position.append(val)
        self.joint_state_pub.publish(msg)

    def q1_minus_click(self):
        self.current_joint_state['Q1'] -= math.radians(self.ui.q1_inc.value())

    def q1_plus_click(self):
        self.current_joint_state['Q1'] += math.radians(self.ui.q1_inc.value())

    def q2_minus_click(self):
        self.current_joint_state['Q2'] -= math.radians(self.ui.q2_inc.value())

    def q2_plus_click(self):
        self.current_joint_state['Q2'] += math.radians(self.ui.q2_inc.value())

    def q3_minus_click(self):
        self.current_joint_state['Q3'] -= math.radians(self.ui.q3_inc.value())

    def q3_plus_click(self):
        self.current_joint_state['Q3'] += math.radians(self.ui.q3_inc.value())

    def d4_minus_click(self):
        self.current_joint_state['D4'] -= self.ui.d4_inc.value() / 1000.0

    def d4_plus_click(self):
        self.current_joint_state['D4'] += self.ui.d4_inc.value() / 1000.0

def main():
    app = QApplication([])
    window = ControlPanel()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
