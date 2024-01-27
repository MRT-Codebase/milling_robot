from PySide6.QtWidgets import QApplication, QMainWindow
from .ui_file import Ui_MainWindow

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

        self.current_joint_state = {
            "q1": 0.0,
            "q2": 0.0,
            "q3": 0.0,
            "d4": 0.0
        }

        self.current_cartesian_state = {
            "x": 0.0,
            "y": 0.0,
            "z": 0.0
        }

        rclpy.init()
        self.node = Node("control_panel_node")

        self.joint_state_pub = self.node.create_publisher(JointState, 'joint_states', 10)

        self.ros_thread = threading.Thread(target=self.run_ros_node)
        self.ros_thread.daemon = True
        self.ros_thread.start()

    def run_ros_node(self):
        try:
            while rclpy.ok():
                rclpy.spin_once(self.node, timeout_sec=0.1)
        except KeyboardInterrupt:
            pass

    def generate_joint_state(self, delta):
        msg = JointState()
        msg.header.stamp = self.node.get_clock().now().to_msg()
        for i, (joint, val) in enumerate(self.current_joint_state.items()):
            new_val = val + delta[i]
            self.current_joint_state[joint] = new_val
            msg.name.append(joint)
            msg.position.append(new_val)
        return msg

    def q1_minus_click(self):
        print("q1 minus pressed")
        msg = self.generate_joint_state([-self.ui.q1_inc.value(), 0, 0, 0])
        self.joint_state_pub.publish(msg)

    def q1_plus_click(self):
        print("q1 plus pressed")
        msg = self.generate_joint_state([self.ui.q1_inc.value(), 0, 0, 0])
        self.joint_state_pub.publish(msg)

def main():
    app = QApplication([])
    window = ControlPanel()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
