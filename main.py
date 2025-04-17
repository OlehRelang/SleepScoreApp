import sys
import platform
import json
import requests
import numpy as np

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

from ui_main import Ui_MainWindow


class SleepScoreApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.text_fields = [
            self.ui.lineEdit_calories,
            self.ui.lineEdit_distance,
            self.ui.lineEdit_max_hr,
            self.ui.lineEdit_light_act,
            self.ui.lineEdit_mod_act,
            self.ui.lineEdit_rest_hr,
            self.ui.lineEdit_seden,
            self.ui.lineEdit_asleep,  # 7.4
            self.ui.lineEdit_awake,   # 8
            # self.ui.lineEdit_deep_sleep,  # 9
            self.ui.lineEdit_restl,
            self.ui.lineEdit_dz0,
            self.ui.lineEdit_dz1,
            self.ui.lineEdit_dz2,
            self.ui.lineEdit_dz3,
            self.ui.lineEdit_very_act,
            self.ui.lineEdit_fluid,
            self.ui.lineEdit_alco
        ]

        self.check_fields = [
            self.ui.checkBox_Breakfast,
            self.ui.checkBox_Dinner,
            self.ui.checkBox_Evening,
            self.ui.checkBox_Lunch,
            self.ui.checkBox_Aerobic,
            self.ui.checkBox_Cardio,
            self.ui.checkBox_Sport,
            self.ui.checkBox_Strength
        ]
        # self.progressBarValue(100)

        self.b = []

        self.ui.pushButton_input.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_eval.clicked.connect(self.evaluate_score)
        self.ui.pushButton_clear.clicked.connect(self.clear)
        self.ui.pushButton_load.clicked.connect(self.load_from_json)
        self.ui.pushButton_load_2.clicked.connect(self.load_from_json)
        self.ui.pushButton_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        self.show()

    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """
        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        if value >= 90:
            self.ui.label_result.setText("Excellent")
            color = "rgba(76, 175, 80, 255)"
            self.ui.label_result.setStyleSheet(f"color: {color}")
        elif 80 <= value < 90:
            self.ui.label_result.setText("Good")
            color = "rgba(255, 235, 59, 255)"
            self.ui.label_result.setStyleSheet(f"color: {color}")
        elif 60 <= value < 80:
            self.ui.label_result.setText("Fair")
            color = "rgba(255, 183, 77, 255)"
            self.ui.label_result.setStyleSheet(f"color: {color}")
        else:
            self.ui.label_result.setText("Awful")
            color = "rgba(211, 47, 47, 255)"
            self.ui.label_result.setStyleSheet(f"color: {color}")

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)
        self.ui.label_score.setStyleSheet(f"color: {color}")
        self.ui.label_score.setText(str(value))

    def evaluate_score(self):
        X = []

        for field in self.text_fields[:7]:
            X.append(float(field.text()))

        for field in self.b:
            X.append(float(field))

        for field in self.text_fields[9:-1]:
            X.append(float(field.text()))

        X.append(1 if self.text_fields[-1].text().lower() == "yes" else 0)

        for field in self.check_fields:
            X.append(1 if field.isChecked() else 0)

        print(np.array(X))

        url = 'http://127.0.0.1:5000/model'
        requested_data = json.dumps({'data': X})
        response = requests.post(url, requested_data)
        score = round(float(response.text[2:-3]))
        self.progressBarValue(score)
        self.ui.stackedWidget.setCurrentIndex(2)

    def clear(self):
        for field in self.text_fields:
            field.setText("")

        for field in self.check_fields:
            field.setChecked(False)

        self.b = []

    def load_from_json(self):
        self.clear()
        dialog = QFileDialog()
        dialog.exec()

        files = dialog.selectedFiles()
        # Open and read the JSON file
        with open(files[0], 'r') as file:
            data = json.load(file)
            data = list(data.values())

            for key, value in zip(self.text_fields, data[:-11]):
                key.setText(str(value))

            for key, value in zip(self.check_fields, data[-11:-3]):
                key.setChecked(bool(value))

            for value in data[-3:]:
                self.b.append(value)

        self.ui.stackedWidget.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SleepScoreApp()
    sys.exit(app.exec())
