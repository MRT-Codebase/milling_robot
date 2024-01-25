from PySide6.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow  # Import the generated module

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Your additional setup code goes here

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()
