# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainkQrssw.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 820)
        MainWindow.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0.15 rgba(142, 148, 242, 255), stop:0.85 rgba(182, 204, 254, 255));\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_2 = QVBoxLayout(self.page_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.home_frame = QFrame(self.page_home)
        self.home_frame.setObjectName(u"home_frame")
        self.home_frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.home_frame.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.home_frame)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(150, 50, 150, 100)
        self.label = QLabel(self.home_frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_load = QPushButton(self.home_frame)
        self.pushButton_load.setObjectName(u"pushButton_load")
        self.pushButton_load.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.pushButton_load.setFont(font1)
        self.pushButton_load.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_load.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_load.setStyleSheet(u"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"height: 100px;\n"
"width: 100px;\n"
"background-color: rgba(117, 123, 200, 70);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(141, 154, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(141, 158, 255);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_load)

        self.pushButton_input = QPushButton(self.home_frame)
        self.pushButton_input.setObjectName(u"pushButton_input")
        self.pushButton_input.setFont(font1)
        self.pushButton_input.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_input.setStyleSheet(u"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);;\n"
"border-radius: 20px;\n"
"height: 100px;\n"
"width: 100px;\n"
"background-color: rgba(117, 123, 200, 70);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(141, 154, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(141, 158, 255);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_input)

        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.home_frame)

        self.stackedWidget.addWidget(self.page_home)
        self.page_input = QWidget()
        self.page_input.setObjectName(u"page_input")
        self.verticalLayout_13 = QVBoxLayout(self.page_input)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_20 = QLabel(self.page_input)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_20)

        self.lineEdit_fluid = QLineEdit(self.page_input)
        self.lineEdit_fluid.setObjectName(u"lineEdit_fluid")
        self.lineEdit_fluid.setMinimumSize(QSize(180, 30))
        self.lineEdit_fluid.setFont(font1)
        self.lineEdit_fluid.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_6.addWidget(self.lineEdit_fluid)

        self.verticalSpacer_5 = QSpacerItem(20, 78, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)


        self.gridLayout.addLayout(self.verticalLayout_6, 2, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_10 = QLabel(self.page_input)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setKerning(True)
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_10)

        self.lineEdit_dz2 = QLineEdit(self.page_input)
        self.lineEdit_dz2.setObjectName(u"lineEdit_dz2")
        self.lineEdit_dz2.setMinimumSize(QSize(180, 30))
        self.lineEdit_dz2.setFont(font1)
        self.lineEdit_dz2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_8.addWidget(self.lineEdit_dz2)

        self.label_16 = QLabel(self.page_input)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_16)

        self.lineEdit_dz3 = QLineEdit(self.page_input)
        self.lineEdit_dz3.setObjectName(u"lineEdit_dz3")
        self.lineEdit_dz3.setMinimumSize(QSize(180, 30))
        self.lineEdit_dz3.setFont(font1)
        self.lineEdit_dz3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_8.addWidget(self.lineEdit_dz3)


        self.gridLayout.addLayout(self.verticalLayout_8, 2, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.page_input)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.lineEdit_calories = QLineEdit(self.page_input)
        self.lineEdit_calories.setObjectName(u"lineEdit_calories")
        self.lineEdit_calories.setMinimumSize(QSize(180, 30))
        self.lineEdit_calories.setFont(font1)
        self.lineEdit_calories.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_3.addWidget(self.lineEdit_calories)

        self.label_13 = QLabel(self.page_input)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_13)

        self.lineEdit_distance = QLineEdit(self.page_input)
        self.lineEdit_distance.setObjectName(u"lineEdit_distance")
        self.lineEdit_distance.setMinimumSize(QSize(180, 30))
        self.lineEdit_distance.setFont(font1)
        self.lineEdit_distance.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_3.addWidget(self.lineEdit_distance)

        self.label_19 = QLabel(self.page_input)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_19)

        self.lineEdit_max_hr = QLineEdit(self.page_input)
        self.lineEdit_max_hr.setObjectName(u"lineEdit_max_hr")
        self.lineEdit_max_hr.setMinimumSize(QSize(180, 30))
        self.lineEdit_max_hr.setFont(font1)
        self.lineEdit_max_hr.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_3.addWidget(self.lineEdit_max_hr)

        self.label_5 = QLabel(self.page_input)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.lineEdit_rest_hr = QLineEdit(self.page_input)
        self.lineEdit_rest_hr.setObjectName(u"lineEdit_rest_hr")
        self.lineEdit_rest_hr.setMinimumSize(QSize(180, 30))
        self.lineEdit_rest_hr.setFont(font1)
        self.lineEdit_rest_hr.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_3.addWidget(self.lineEdit_rest_hr)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_15 = QLabel(self.page_input)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_15)

        self.lineEdit_dz0 = QLineEdit(self.page_input)
        self.lineEdit_dz0.setObjectName(u"lineEdit_dz0")
        self.lineEdit_dz0.setMinimumSize(QSize(180, 30))
        self.lineEdit_dz0.setFont(font1)
        self.lineEdit_dz0.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_11.addWidget(self.lineEdit_dz0)

        self.label_7 = QLabel(self.page_input)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_7)

        self.lineEdit_dz1 = QLineEdit(self.page_input)
        self.lineEdit_dz1.setObjectName(u"lineEdit_dz1")
        self.lineEdit_dz1.setMinimumSize(QSize(180, 30))
        self.lineEdit_dz1.setFont(font1)
        self.lineEdit_dz1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_11.addWidget(self.lineEdit_dz1)


        self.gridLayout.addLayout(self.verticalLayout_11, 2, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_12 = QLabel(self.page_input)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_12)

        self.lineEdit_asleep = QLineEdit(self.page_input)
        self.lineEdit_asleep.setObjectName(u"lineEdit_asleep")
        self.lineEdit_asleep.setMinimumSize(QSize(180, 30))
        self.lineEdit_asleep.setFont(font1)
        self.lineEdit_asleep.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_5.addWidget(self.lineEdit_asleep)

        self.label_18 = QLabel(self.page_input)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_18)

        self.lineEdit_awake = QLineEdit(self.page_input)
        self.lineEdit_awake.setObjectName(u"lineEdit_awake")
        self.lineEdit_awake.setMinimumSize(QSize(180, 30))
        self.lineEdit_awake.setFont(font1)
        self.lineEdit_awake.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_5.addWidget(self.lineEdit_awake)

        self.label_9 = QLabel(self.page_input)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_9)

        self.lineEdit_restl = QLineEdit(self.page_input)
        self.lineEdit_restl.setObjectName(u"lineEdit_restl")
        self.lineEdit_restl.setMinimumSize(QSize(180, 30))
        self.lineEdit_restl.setFont(font1)
        self.lineEdit_restl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_5.addWidget(self.lineEdit_restl)

        self.label_17 = QLabel(self.page_input)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_17)

        self.lineEdit_alco = QLineEdit(self.page_input)
        self.lineEdit_alco.setObjectName(u"lineEdit_alco")
        self.lineEdit_alco.setMinimumSize(QSize(180, 30))
        self.lineEdit_alco.setFont(font1)
        self.lineEdit_alco.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_5.addWidget(self.lineEdit_alco)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.page_input)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.lineEdit_light_act = QLineEdit(self.page_input)
        self.lineEdit_light_act.setObjectName(u"lineEdit_light_act")
        self.lineEdit_light_act.setEnabled(True)
        self.lineEdit_light_act.setMinimumSize(QSize(180, 30))
        self.lineEdit_light_act.setFont(font1)
        self.lineEdit_light_act.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.lineEdit_light_act)

        self.label_8 = QLabel(self.page_input)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_8)

        self.lineEdit_mod_act = QLineEdit(self.page_input)
        self.lineEdit_mod_act.setObjectName(u"lineEdit_mod_act")
        self.lineEdit_mod_act.setMinimumSize(QSize(180, 30))
        self.lineEdit_mod_act.setFont(font1)
        self.lineEdit_mod_act.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.lineEdit_mod_act)

        self.label_11 = QLabel(self.page_input)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_11)

        self.lineEdit_very_act = QLineEdit(self.page_input)
        self.lineEdit_very_act.setObjectName(u"lineEdit_very_act")
        self.lineEdit_very_act.setMinimumSize(QSize(180, 30))
        self.lineEdit_very_act.setFont(font1)
        self.lineEdit_very_act.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.lineEdit_very_act)

        self.label_14 = QLabel(self.page_input)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_14)

        self.lineEdit_seden = QLineEdit(self.page_input)
        self.lineEdit_seden.setObjectName(u"lineEdit_seden")
        self.lineEdit_seden.setMinimumSize(QSize(180, 30))
        self.lineEdit_seden.setFont(font1)
        self.lineEdit_seden.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"background-color: rgba(157, 169, 247, 50);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.lineEdit_seden)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(180, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_8, 1, 1, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, -1, -1, -1)
        self.label_21 = QLabel(self.page_input)
        self.label_21.setObjectName(u"label_21")
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_21)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_Breakfast = QCheckBox(self.page_input)
        self.checkBox_Breakfast.setObjectName(u"checkBox_Breakfast")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.checkBox_Breakfast.setFont(font4)
        self.checkBox_Breakfast.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_Breakfast.setAutoFillBackground(False)
        self.checkBox_Breakfast.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}")
        self.checkBox_Breakfast.setTristate(False)

        self.horizontalLayout.addWidget(self.checkBox_Breakfast)

        self.checkBox_Dinner = QCheckBox(self.page_input)
        self.checkBox_Dinner.setObjectName(u"checkBox_Dinner")
        self.checkBox_Dinner.setFont(font4)
        self.checkBox_Dinner.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_Dinner.setAutoFillBackground(False)
        self.checkBox_Dinner.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}")
        self.checkBox_Dinner.setTristate(False)

        self.horizontalLayout.addWidget(self.checkBox_Dinner)

        self.checkBox_Lunch = QCheckBox(self.page_input)
        self.checkBox_Lunch.setObjectName(u"checkBox_Lunch")
        self.checkBox_Lunch.setFont(font4)
        self.checkBox_Lunch.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_Lunch.setAutoFillBackground(False)
        self.checkBox_Lunch.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}")
        self.checkBox_Lunch.setTristate(False)

        self.horizontalLayout.addWidget(self.checkBox_Lunch)

        self.checkBox_Evening = QCheckBox(self.page_input)
        self.checkBox_Evening.setObjectName(u"checkBox_Evening")
        self.checkBox_Evening.setFont(font4)
        self.checkBox_Evening.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_Evening.setAutoFillBackground(False)
        self.checkBox_Evening.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}")
        self.checkBox_Evening.setTristate(False)

        self.horizontalLayout.addWidget(self.checkBox_Evening)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_12)

        self.label_22 = QLabel(self.page_input)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_22)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_Aerobic = QCheckBox(self.page_input)
        self.checkBox_Aerobic.setObjectName(u"checkBox_Aerobic")
        self.checkBox_Aerobic.setFont(font4)
        self.checkBox_Aerobic.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_Aerobic.setAutoFillBackground(False)
        self.checkBox_Aerobic.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}")
        self.checkBox_Aerobic.setTristate(False)

        self.horizontalLayout_2.addWidget(self.checkBox_Aerobic)

        self.checkBox_Sport = QCheckBox(self.page_input)
        self.checkBox_Sport.setObjectName(u"checkBox_Sport")
        self.checkBox_Sport.setFont(font4)
        self.checkBox_Sport.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_Sport.setAutoFillBackground(False)
        self.checkBox_Sport.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}")
        self.checkBox_Sport.setTristate(False)

        self.horizontalLayout_2.addWidget(self.checkBox_Sport)

        self.checkBox_Cardio = QCheckBox(self.page_input)
        self.checkBox_Cardio.setObjectName(u"checkBox_Cardio")
        self.checkBox_Cardio.setFont(font4)
        self.checkBox_Cardio.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_Cardio.setAutoFillBackground(False)
        self.checkBox_Cardio.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}")
        self.checkBox_Cardio.setTristate(False)

        self.horizontalLayout_2.addWidget(self.checkBox_Cardio)

        self.checkBox_Strength = QCheckBox(self.page_input)
        self.checkBox_Strength.setObjectName(u"checkBox_Strength")
        self.checkBox_Strength.setFont(font4)
        self.checkBox_Strength.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_Strength.setAutoFillBackground(False)
        self.checkBox_Strength.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}")
        self.checkBox_Strength.setTristate(False)

        self.horizontalLayout_2.addWidget(self.checkBox_Strength)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)


        self.verticalLayout_13.addLayout(self.verticalLayout_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pushButton_clear = QPushButton(self.page_input)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMinimumSize(QSize(0, 0))
        self.pushButton_clear.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_clear.setFont(font1)
        self.pushButton_clear.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_clear.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_clear.setStyleSheet(u"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"height: 100px;\n"
"width: 100px;\n"
"background-color: rgba(117, 123, 200, 70);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(141, 154, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(141, 158, 255);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_clear)

        self.pushButton_load_2 = QPushButton(self.page_input)
        self.pushButton_load_2.setObjectName(u"pushButton_load_2")
        self.pushButton_load_2.setFont(font1)
        self.pushButton_load_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_load_2.setStyleSheet(u"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"height: 100px;\n"
"width: 100px;\n"
"background-color: rgba(117, 123, 200, 70);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(141, 154, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(141, 158, 255);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_load_2)

        self.pushButton_eval = QPushButton(self.page_input)
        self.pushButton_eval.setObjectName(u"pushButton_eval")
        self.pushButton_eval.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_eval.setFont(font1)
        self.pushButton_eval.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_eval.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_eval.setStyleSheet(u"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"height: 100px;\n"
"width: 100px;\n"
"background-color: rgba(117, 123, 200, 70);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(141, 154, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(141, 158, 255);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_eval)


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_input)
        self.page_results = QWidget()
        self.page_results.setObjectName(u"page_results")
        self.verticalLayout_7 = QVBoxLayout(self.page_results)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 15)
        self.resultWidget = QFrame(self.page_results)
        self.resultWidget.setObjectName(u"resultWidget")
        self.resultWidget.setStyleSheet(u"background-color: none;")
        self.verticalLayout_12 = QVBoxLayout(self.resultWidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_6 = QLabel(self.resultWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 100))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_6)

        self.verticalSpacer_10 = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_10)

        self.circluarResult = QFrame(self.resultWidget)
        self.circluarResult.setObjectName(u"circluarResult")
        self.circluarResult.setStyleSheet(u"background-color: none;")
        self.circluarResult.setFrameShape(QFrame.Shape.NoFrame)
        self.circluarResult.setFrameShadow(QFrame.Shadow.Raised)
        self.circularProgress = QFrame(self.circluarResult)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(130, 0, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame {\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.Shape.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Shadow.Raised)
        self.circularBG = QFrame(self.circluarResult)
        self.circularBG.setObjectName(u"circularBG")
        self.circularBG.setGeometry(QRect(130, 0, 300, 300))
        self.circularBG.setStyleSheet(u"QFrame {\n"
"	border-radius: 150px;\n"
"	background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBG.setFrameShape(QFrame.Shape.NoFrame)
        self.circularBG.setFrameShadow(QFrame.Shadow.Raised)
        self.container = QFrame(self.circluarResult)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(140, 10, 280, 280))
        self.container.setStyleSheet(u"QFrame {\n"
"	border-radius: 135px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QFrame.Shape.StyledPanel)
        self.container.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.container)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 40, 201, 201))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.label_score = QLabel(self.layoutWidget)
        self.label_score.setObjectName(u"label_score")
        self.label_score.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setPointSize(48)
        font5.setBold(True)
        self.label_score.setFont(font5)
        self.label_score.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_score.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_score)

        self.label_result = QLabel(self.layoutWidget)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setPointSize(20)
        font6.setBold(True)
        self.label_result.setFont(font6)
        self.label_result.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_result)

        self.circularBG.raise_()
        self.circularProgress.raise_()
        self.container.raise_()

        self.verticalLayout_12.addWidget(self.circluarResult)

        self.verticalSpacer_11 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(140, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.pushButton_back = QPushButton(self.resultWidget)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setMinimumSize(QSize(240, 0))
        self.pushButton_back.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_back.setFont(font1)
        self.pushButton_back.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_back.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_back.setStyleSheet(u"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"height: 100px;\n"
"width: 100px;\n"
"background-color: rgba(117, 123, 200, 70);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(141, 154, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(141, 158, 255);\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_back)

        self.horizontalSpacer_2 = QSpacerItem(140, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5)


        self.verticalLayout_7.addWidget(self.resultWidget)

        self.stackedWidget.addWidget(self.page_results)

        self.horizontalLayout_4.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SleepScoreApp", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SleepScoreApp", None))
        self.pushButton_load.setText(QCoreApplication.translate("MainWindow", u"Load from JSON", None))
        self.pushButton_input.setText(QCoreApplication.translate("MainWindow", u"Input manualy", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Glasses Of Fluid", None))
        self.lineEdit_fluid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"glasses", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Default Zone 2", None))
        self.lineEdit_dz2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minutes", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Default Zone 3", None))
        self.lineEdit_dz3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minutes", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Calories", None))
        self.lineEdit_calories.setText("")
        self.lineEdit_calories.setPlaceholderText(QCoreApplication.translate("MainWindow", u"kal", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.lineEdit_distance.setPlaceholderText(QCoreApplication.translate("MainWindow", u"meters", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Max Heart Rate", None))
        self.lineEdit_max_hr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"bpm", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Resting Heart Rate", None))
        self.lineEdit_rest_hr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"bpm", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Below Default Zone", None))
        self.lineEdit_dz0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minutes", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Default Zone 1", None))
        self.lineEdit_dz1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minutes", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Time Asleep", None))
        self.lineEdit_asleep.setText("")
        self.lineEdit_asleep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Time Awake", None))
        self.lineEdit_awake.setText("")
        self.lineEdit_awake.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Restlessness", None))
        self.lineEdit_restl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[0-1]", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Alcohol Consumed", None))
        self.lineEdit_alco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Yes/No", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Lightly Active", None))
        self.lineEdit_light_act.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minutes", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Moderately Active", None))
        self.lineEdit_mod_act.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minutes", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Very Active", None))
        self.lineEdit_very_act.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minutes", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Sedentary", None))
        self.lineEdit_seden.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minutes", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Meals", None))
        self.checkBox_Breakfast.setText(QCoreApplication.translate("MainWindow", u"Breakfast", None))
        self.checkBox_Dinner.setText(QCoreApplication.translate("MainWindow", u"Dinner", None))
        self.checkBox_Lunch.setText(QCoreApplication.translate("MainWindow", u"Lunch", None))
        self.checkBox_Evening.setText(QCoreApplication.translate("MainWindow", u"Evening", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Activites", None))
        self.checkBox_Aerobic.setText(QCoreApplication.translate("MainWindow", u"Aerobic", None))
        self.checkBox_Sport.setText(QCoreApplication.translate("MainWindow", u"Sport", None))
        self.checkBox_Cardio.setText(QCoreApplication.translate("MainWindow", u"Cardio", None))
        self.checkBox_Strength.setText(QCoreApplication.translate("MainWindow", u"Strength", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_load_2.setText(QCoreApplication.translate("MainWindow", u"Load JSON", None))
        self.pushButton_eval.setText(QCoreApplication.translate("MainWindow", u"Evaluate", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sleep Score", None))
        self.label_score.setText(QCoreApplication.translate("MainWindow", u"69", None))
        self.label_result.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.pushButton_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

