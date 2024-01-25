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
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.d4_plus = QPushButton(self.centralwidget)
        self.d4_plus.setObjectName(u"d4_plus")

        self.gridLayout_2.addWidget(self.d4_plus, 3, 2, 1, 1)

        self.q1_inc = QDoubleSpinBox(self.centralwidget)
        self.q1_inc.setObjectName(u"q1_inc")

        self.gridLayout_2.addWidget(self.q1_inc, 0, 0, 1, 1)

        self.d4_minus = QPushButton(self.centralwidget)
        self.d4_minus.setObjectName(u"d4_minus")

        self.gridLayout_2.addWidget(self.d4_minus, 3, 1, 1, 1)

        self.q3_val = QLabel(self.centralwidget)
        self.q3_val.setObjectName(u"q3_val")
        self.q3_val.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.q3_val, 2, 3, 1, 1)

        self.d4_val = QLabel(self.centralwidget)
        self.d4_val.setObjectName(u"d4_val")
        self.d4_val.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.d4_val, 3, 3, 1, 1)

        self.d4_inc = QDoubleSpinBox(self.centralwidget)
        self.d4_inc.setObjectName(u"d4_inc")

        self.gridLayout_2.addWidget(self.d4_inc, 3, 0, 1, 1)

        self.q1_minus = QPushButton(self.centralwidget)
        self.q1_minus.setObjectName(u"q1_minus")

        self.gridLayout_2.addWidget(self.q1_minus, 0, 1, 1, 1)

        self.q2_val = QLabel(self.centralwidget)
        self.q2_val.setObjectName(u"q2_val")
        self.q2_val.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.q2_val, 1, 3, 1, 1)

        self.q2_minus = QPushButton(self.centralwidget)
        self.q2_minus.setObjectName(u"q2_minus")

        self.gridLayout_2.addWidget(self.q2_minus, 1, 1, 1, 1)

        self.q2_plus = QPushButton(self.centralwidget)
        self.q2_plus.setObjectName(u"q2_plus")

        self.gridLayout_2.addWidget(self.q2_plus, 1, 2, 1, 1)

        self.q1_val = QLabel(self.centralwidget)
        self.q1_val.setObjectName(u"q1_val")
        self.q1_val.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.q1_val, 0, 3, 1, 1)

        self.q3_minus = QPushButton(self.centralwidget)
        self.q3_minus.setObjectName(u"q3_minus")

        self.gridLayout_2.addWidget(self.q3_minus, 2, 1, 1, 1)

        self.q3_plus = QPushButton(self.centralwidget)
        self.q3_plus.setObjectName(u"q3_plus")

        self.gridLayout_2.addWidget(self.q3_plus, 2, 2, 1, 1)

        self.q2_inc = QDoubleSpinBox(self.centralwidget)
        self.q2_inc.setObjectName(u"q2_inc")

        self.gridLayout_2.addWidget(self.q2_inc, 1, 0, 1, 1)

        self.q1_plus = QPushButton(self.centralwidget)
        self.q1_plus.setObjectName(u"q1_plus")

        self.gridLayout_2.addWidget(self.q1_plus, 0, 2, 1, 1)

        self.q3_inc = QDoubleSpinBox(self.centralwidget)
        self.q3_inc.setObjectName(u"q3_inc")

        self.gridLayout_2.addWidget(self.q3_inc, 2, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.y_inc = QDoubleSpinBox(self.centralwidget)
        self.y_inc.setObjectName(u"y_inc")

        self.gridLayout_3.addWidget(self.y_inc, 1, 0, 1, 1)

        self.z_minus = QPushButton(self.centralwidget)
        self.z_minus.setObjectName(u"z_minus")

        self.gridLayout_3.addWidget(self.z_minus, 2, 1, 1, 1)

        self.x_plus = QPushButton(self.centralwidget)
        self.x_plus.setObjectName(u"x_plus")

        self.gridLayout_3.addWidget(self.x_plus, 0, 2, 1, 1)

        self.z_plus = QPushButton(self.centralwidget)
        self.z_plus.setObjectName(u"z_plus")

        self.gridLayout_3.addWidget(self.z_plus, 2, 2, 1, 1)

        self.y_plus = QPushButton(self.centralwidget)
        self.y_plus.setObjectName(u"y_plus")

        self.gridLayout_3.addWidget(self.y_plus, 1, 2, 1, 1)

        self.z_val = QLabel(self.centralwidget)
        self.z_val.setObjectName(u"z_val")
        self.z_val.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.z_val, 2, 3, 1, 1)

        self.x_minus = QPushButton(self.centralwidget)
        self.x_minus.setObjectName(u"x_minus")

        self.gridLayout_3.addWidget(self.x_minus, 0, 1, 1, 1)

        self.y_minus = QPushButton(self.centralwidget)
        self.y_minus.setObjectName(u"y_minus")

        self.gridLayout_3.addWidget(self.y_minus, 1, 1, 1, 1)

        self.y_val = QLabel(self.centralwidget)
        self.y_val.setObjectName(u"y_val")
        self.y_val.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.y_val, 1, 3, 1, 1)

        self.x_inc = QDoubleSpinBox(self.centralwidget)
        self.x_inc.setObjectName(u"x_inc")

        self.gridLayout_3.addWidget(self.x_inc, 0, 0, 1, 1)

        self.x_val = QLabel(self.centralwidget)
        self.x_val.setObjectName(u"x_val")
        self.x_val.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.x_val, 0, 3, 1, 1)

        self.z_inc = QDoubleSpinBox(self.centralwidget)
        self.z_inc.setObjectName(u"z_inc")

        self.gridLayout_3.addWidget(self.z_inc, 2, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Milling Robot Control Panel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Joint Control", None))
        self.d4_plus.setText(QCoreApplication.translate("MainWindow", u"D4+", None))
        self.d4_minus.setText(QCoreApplication.translate("MainWindow", u"D4-", None))
        self.q3_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.d4_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.q1_minus.setText(QCoreApplication.translate("MainWindow", u"Q1-", None))
        self.q2_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.q2_minus.setText(QCoreApplication.translate("MainWindow", u"Q2-", None))
        self.q2_plus.setText(QCoreApplication.translate("MainWindow", u"Q2+", None))
        self.q1_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.q3_minus.setText(QCoreApplication.translate("MainWindow", u"Q3-", None))
        self.q3_plus.setText(QCoreApplication.translate("MainWindow", u"Q3+", None))
        self.q1_plus.setText(QCoreApplication.translate("MainWindow", u"Q1+", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cartesian Control", None))
        self.z_minus.setText(QCoreApplication.translate("MainWindow", u"Z-", None))
        self.x_plus.setText(QCoreApplication.translate("MainWindow", u"X+", None))
        self.z_plus.setText(QCoreApplication.translate("MainWindow", u"Z+", None))
        self.y_plus.setText(QCoreApplication.translate("MainWindow", u"Y+", None))
        self.z_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.x_minus.setText(QCoreApplication.translate("MainWindow", u"X-", None))
        self.y_minus.setText(QCoreApplication.translate("MainWindow", u"Y-", None))
        self.y_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.x_val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

