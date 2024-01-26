from PySide6.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow
import threading
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.q1_minus.clicked.connect(self.q1_minus_click)

        rclpy.init()
        self.node = Node("control_panel_node")
        self.test_pub = self.node.create_publisher(String, 'test', 10)

        self.ros_thread = threading.Thread(target=self.run_ros_node)
        self.ros_thread.start()

    def run_ros_node(self):
        try:
            while rclpy.ok():
                rclpy.spin_once(self.node, timeout_sec=0.1)
        except KeyboardInterrupt:
            pass

    def q1_minus_click(self):
        print("q1 minus pressed")
        msg = String()
        msg.data = str(self.ui.q1_inc.value())
        self.test_pub.publish(msg)

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()
