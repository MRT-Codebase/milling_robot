from PySide6.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow  # Import the generated module

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.q1_minus.clicked.connect(self.q1_minus_click)

    def q1_minus_click(self):
        print("q1 minus pressed")
        print(self.ui.q1_inc.value())

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()
