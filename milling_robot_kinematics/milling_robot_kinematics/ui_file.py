# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'control_panel.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListView, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Title = QLabel(self.centralwidget)
        self.Title.setObjectName(u"Title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setTextFormat(Qt.AutoText)
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Title)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.control_layout = QHBoxLayout()
        self.control_layout.setObjectName(u"control_layout")
        self.joint_control_layout = QVBoxLayout()
        self.joint_control_layout.setObjectName(u"joint_control_layout")
        self.joint_control_title = QLabel(self.centralwidget)
        self.joint_control_title.setObjectName(u"joint_control_title")
        sizePolicy.setHeightForWidth(self.joint_control_title.sizePolicy().hasHeightForWidth())
        self.joint_control_title.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.joint_control_title.setFont(font1)
        self.joint_control_title.setAlignment(Qt.AlignCenter)

        self.joint_control_layout.addWidget(self.joint_control_title)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.joint_control_layout.addItem(self.verticalSpacer_2)

        self.joint_control_input_layout = QGridLayout()
        self.joint_control_input_layout.setObjectName(u"joint_control_input_layout")
        self.q3_minus = QPushButton(self.centralwidget)
        self.q3_minus.setObjectName(u"q3_minus")
        self.q3_minus.setAutoRepeat(True)

        self.joint_control_input_layout.addWidget(self.q3_minus, 2, 1, 1, 1)

        self.q3_val = QLabel(self.centralwidget)
        self.q3_val.setObjectName(u"q3_val")
        self.q3_val.setAlignment(Qt.AlignCenter)

        self.joint_control_input_layout.addWidget(self.q3_val, 2, 3, 1, 1)

        self.q3_plus = QPushButton(self.centralwidget)
        self.q3_plus.setObjectName(u"q3_plus")
        self.q3_plus.setAutoRepeat(True)

        self.joint_control_input_layout.addWidget(self.q3_plus, 2, 2, 1, 1)

        self.q2_inc = QDoubleSpinBox(self.centralwidget)
        self.q2_inc.setObjectName(u"q2_inc")
        self.q2_inc.setValue(5.000000000000000)

        self.joint_control_input_layout.addWidget(self.q2_inc, 1, 0, 1, 1)

        self.d4_plus = QPushButton(self.centralwidget)
        self.d4_plus.setObjectName(u"d4_plus")
        self.d4_plus.setAutoRepeat(True)

        self.joint_control_input_layout.addWidget(self.d4_plus, 3, 2, 1, 1)

        self.q1_plus = QPushButton(self.centralwidget)
        self.q1_plus.setObjectName(u"q1_plus")
        self.q1_plus.setAutoRepeat(True)

        self.joint_control_input_layout.addWidget(self.q1_plus, 0, 2, 1, 1)

        self.q1_inc = QDoubleSpinBox(self.centralwidget)
        self.q1_inc.setObjectName(u"q1_inc")
        self.q1_inc.setValue(5.000000000000000)

        self.joint_control_input_layout.addWidget(self.q1_inc, 0, 0, 1, 1)

        self.q2_plus = QPushButton(self.centralwidget)
        self.q2_plus.setObjectName(u"q2_plus")
        self.q2_plus.setAutoRepeat(True)

        self.joint_control_input_layout.addWidget(self.q2_plus, 1, 2, 1, 1)

        self.q1_val = QLabel(self.centralwidget)
        self.q1_val.setObjectName(u"q1_val")
        self.q1_val.setAlignment(Qt.AlignCenter)

        self.joint_control_input_layout.addWidget(self.q1_val, 0, 3, 1, 1)

        self.d4_minus = QPushButton(self.centralwidget)
        self.d4_minus.setObjectName(u"d4_minus")
        self.d4_minus.setAutoRepeat(True)

        self.joint_control_input_layout.addWidget(self.d4_minus, 3, 1, 1, 1)

        self.q1_minus = QPushButton(self.centralwidget)
        self.q1_minus.setObjectName(u"q1_minus")
        self.q1_minus.setAutoRepeat(True)

        self.joint_control_input_layout.addWidget(self.q1_minus, 0, 1, 1, 1)

        self.q2_minus = QPushButton(self.centralwidget)
        self.q2_minus.setObjectName(u"q2_minus")
        self.q2_minus.setAutoRepeat(True)

        self.joint_control_input_layout.addWidget(self.q2_minus, 1, 1, 1, 1)

        self.q3_inc = QDoubleSpinBox(self.centralwidget)
        self.q3_inc.setObjectName(u"q3_inc")
        self.q3_inc.setValue(5.000000000000000)

        self.joint_control_input_layout.addWidget(self.q3_inc, 2, 0, 1, 1)

        self.q2_val = QLabel(self.centralwidget)
        self.q2_val.setObjectName(u"q2_val")
        self.q2_val.setAlignment(Qt.AlignCenter)

        self.joint_control_input_layout.addWidget(self.q2_val, 1, 3, 1, 1)

        self.d4_inc = QDoubleSpinBox(self.centralwidget)
        self.d4_inc.setObjectName(u"d4_inc")
        self.d4_inc.setValue(2.000000000000000)

        self.joint_control_input_layout.addWidget(self.d4_inc, 3, 0, 1, 1)

        self.d4_val = QLabel(self.centralwidget)
        self.d4_val.setObjectName(u"d4_val")
        self.d4_val.setAlignment(Qt.AlignCenter)

        self.joint_control_input_layout.addWidget(self.d4_val, 3, 3, 1, 1)


        self.joint_control_layout.addLayout(self.joint_control_input_layout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.joint_control_layout.addItem(self.verticalSpacer)


        self.control_layout.addLayout(self.joint_control_layout)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.control_layout.addWidget(self.line_3)

        self.cartesian_control_layout = QVBoxLayout()
        self.cartesian_control_layout.setObjectName(u"cartesian_control_layout")
        self.cartesian_control_title = QLabel(self.centralwidget)
        self.cartesian_control_title.setObjectName(u"cartesian_control_title")
        sizePolicy.setHeightForWidth(self.cartesian_control_title.sizePolicy().hasHeightForWidth())
        self.cartesian_control_title.setSizePolicy(sizePolicy)
        self.cartesian_control_title.setFont(font1)
        self.cartesian_control_title.setAlignment(Qt.AlignCenter)

        self.cartesian_control_layout.addWidget(self.cartesian_control_title)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.cartesian_control_layout.addItem(self.verticalSpacer_3)

        self.cartesian_control_input_layout = QGridLayout()
        self.cartesian_control_input_layout.setObjectName(u"cartesian_control_input_layout")
        self.y_minus = QPushButton(self.centralwidget)
        self.y_minus.setObjectName(u"y_minus")
        self.y_minus.setAutoRepeat(True)

        self.cartesian_control_input_layout.addWidget(self.y_minus, 1, 1, 1, 1)

        self.y_inc = QDoubleSpinBox(self.centralwidget)
        self.y_inc.setObjectName(u"y_inc")
        self.y_inc.setValue(2.000000000000000)

        self.cartesian_control_input_layout.addWidget(self.y_inc, 1, 0, 1, 1)

        self.y_val = QLabel(self.centralwidget)
        self.y_val.setObjectName(u"y_val")
        self.y_val.setAlignment(Qt.AlignCenter)

        self.cartesian_control_input_layout.addWidget(self.y_val, 1, 3, 1, 1)

        self.x_plus = QPushButton(self.centralwidget)
        self.x_plus.setObjectName(u"x_plus")
        self.x_plus.setAutoRepeat(True)

        self.cartesian_control_input_layout.addWidget(self.x_plus, 0, 2, 1, 1)

        self.z_minus = QPushButton(self.centralwidget)
        self.z_minus.setObjectName(u"z_minus")
        self.z_minus.setAutoRepeat(True)

        self.cartesian_control_input_layout.addWidget(self.z_minus, 2, 1, 1, 1)

        self.z_val = QLabel(self.centralwidget)
        self.z_val.setObjectName(u"z_val")
        self.z_val.setAlignment(Qt.AlignCenter)

        self.cartesian_control_input_layout.addWidget(self.z_val, 2, 3, 1, 1)

        self.y_plus = QPushButton(self.centralwidget)
        self.y_plus.setObjectName(u"y_plus")
        self.y_plus.setAutoRepeat(True)

        self.cartesian_control_input_layout.addWidget(self.y_plus, 1, 2, 1, 1)

        self.z_plus = QPushButton(self.centralwidget)
        self.z_plus.setObjectName(u"z_plus")
        self.z_plus.setAutoRepeat(True)

        self.cartesian_control_input_layout.addWidget(self.z_plus, 2, 2, 1, 1)

        self.x_minus = QPushButton(self.centralwidget)
        self.x_minus.setObjectName(u"x_minus")
        self.x_minus.setAutoRepeat(True)

        self.cartesian_control_input_layout.addWidget(self.x_minus, 0, 1, 1, 1)

        self.z_inc = QDoubleSpinBox(self.centralwidget)
        self.z_inc.setObjectName(u"z_inc")
        self.z_inc.setValue(2.000000000000000)

        self.cartesian_control_input_layout.addWidget(self.z_inc, 2, 0, 1, 1)

        self.x_inc = QDoubleSpinBox(self.centralwidget)
        self.x_inc.setObjectName(u"x_inc")
        self.x_inc.setValue(2.000000000000000)

        self.cartesian_control_input_layout.addWidget(self.x_inc, 0, 0, 1, 1)

        self.x_val = QLabel(self.centralwidget)
        self.x_val.setObjectName(u"x_val")
        self.x_val.setAlignment(Qt.AlignCenter)

        self.cartesian_control_input_layout.addWidget(self.x_val, 0, 3, 1, 1)


        self.cartesian_control_layout.addLayout(self.cartesian_control_input_layout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.cartesian_control_layout.addItem(self.verticalSpacer_4)


        self.control_layout.addLayout(self.cartesian_control_layout)


        self.verticalLayout_2.addLayout(self.control_layout)

        self.trajectory_generation_layout = QVBoxLayout()
        self.trajectory_generation_layout.setObjectName(u"trajectory_generation_layout")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.trajectory_generation_layout.addWidget(self.line)

        self.trajectory_generation_title = QLabel(self.centralwidget)
        self.trajectory_generation_title.setObjectName(u"trajectory_generation_title")
        sizePolicy.setHeightForWidth(self.trajectory_generation_title.sizePolicy().hasHeightForWidth())
        self.trajectory_generation_title.setSizePolicy(sizePolicy)
        self.trajectory_generation_title.setFont(font1)
        self.trajectory_generation_title.setAlignment(Qt.AlignCenter)

        self.trajectory_generation_layout.addWidget(self.trajectory_generation_title)

        self.waypoint_management_layout = QHBoxLayout()
        self.waypoint_management_layout.setObjectName(u"waypoint_management_layout")
        self.waypoint_management_input_layout = QVBoxLayout()
        self.waypoint_management_input_layout.setObjectName(u"waypoint_management_input_layout")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.waypoint_management_input_layout.addItem(self.verticalSpacer_6)

        self.add_waypoint = QPushButton(self.centralwidget)
        self.add_waypoint.setObjectName(u"add_waypoint")

        self.waypoint_management_input_layout.addWidget(self.add_waypoint)

        self.delete_waypoint = QPushButton(self.centralwidget)
        self.delete_waypoint.setObjectName(u"delete_waypoint")

        self.waypoint_management_input_layout.addWidget(self.delete_waypoint)

        self.reset_trajectory = QPushButton(self.centralwidget)
        self.reset_trajectory.setObjectName(u"reset_trajectory")

        self.waypoint_management_input_layout.addWidget(self.reset_trajectory)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.waypoint_management_input_layout.addItem(self.verticalSpacer_5)


        self.waypoint_management_layout.addLayout(self.waypoint_management_input_layout)

        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy1)

        self.waypoint_management_layout.addWidget(self.listView)

        self.waypoint_management_layout.setStretch(0, 1)
        self.waypoint_management_layout.setStretch(1, 2)

        self.trajectory_generation_layout.addLayout(self.waypoint_management_layout)

        self.play_pause_layout = QHBoxLayout()
        self.play_pause_layout.setObjectName(u"play_pause_layout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.play_pause_layout.addItem(self.horizontalSpacer)

        self.play = QPushButton(self.centralwidget)
        self.play.setObjectName(u"play")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.play.sizePolicy().hasHeightForWidth())
        self.play.setSizePolicy(sizePolicy2)

        self.play_pause_layout.addWidget(self.play)

        self.pause = QPushButton(self.centralwidget)
        self.pause.setObjectName(u"pause")
        sizePolicy2.setHeightForWidth(self.pause.sizePolicy().hasHeightForWidth())
        self.pause.setSizePolicy(sizePolicy2)

        self.play_pause_layout.addWidget(self.pause)

        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        sizePolicy2.setHeightForWidth(self.stop.sizePolicy().hasHeightForWidth())
        self.stop.setSizePolicy(sizePolicy2)

        self.play_pause_layout.addWidget(self.stop)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.play_pause_layout.addItem(self.horizontalSpacer_2)


        self.trajectory_generation_layout.addLayout(self.play_pause_layout)


        self.verticalLayout_2.addLayout(self.trajectory_generation_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"Milling Robot Control Panel", None))
        self.joint_control_title.setText(QCoreApplication.translate("MainWindow", u"Joint Control", None))
        self.q3_minus.setText(QCoreApplication.translate("MainWindow", u"Q3-", None))
        self.q3_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.q3_plus.setText(QCoreApplication.translate("MainWindow", u"Q3+", None))
        self.d4_plus.setText(QCoreApplication.translate("MainWindow", u"D4+", None))
        self.q1_plus.setText(QCoreApplication.translate("MainWindow", u"Q1+", None))
        self.q2_plus.setText(QCoreApplication.translate("MainWindow", u"Q2+", None))
        self.q1_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.d4_minus.setText(QCoreApplication.translate("MainWindow", u"D4-", None))
        self.q1_minus.setText(QCoreApplication.translate("MainWindow", u"Q1-", None))
        self.q2_minus.setText(QCoreApplication.translate("MainWindow", u"Q2-", None))
        self.q2_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.d4_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cartesian_control_title.setText(QCoreApplication.translate("MainWindow", u"Cartesian Control", None))
        self.y_minus.setText(QCoreApplication.translate("MainWindow", u"Y-", None))
        self.y_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.x_plus.setText(QCoreApplication.translate("MainWindow", u"X+", None))
        self.z_minus.setText(QCoreApplication.translate("MainWindow", u"Z-", None))
        self.z_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.y_plus.setText(QCoreApplication.translate("MainWindow", u"Y+", None))
        self.z_plus.setText(QCoreApplication.translate("MainWindow", u"Z+", None))
        self.x_minus.setText(QCoreApplication.translate("MainWindow", u"X-", None))
        self.x_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.trajectory_generation_title.setText(QCoreApplication.translate("MainWindow", u"Trajectory Generation", None))
        self.add_waypoint.setText(QCoreApplication.translate("MainWindow", u"Add Waypoint", None))
        self.delete_waypoint.setText(QCoreApplication.translate("MainWindow", u"Delete Waypoint", None))
        self.reset_trajectory.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.pause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

