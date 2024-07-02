# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
                               QSizePolicy, QWidget)


class Ui_Message(object):
    def setupUi(self, Message):
        if not Message.objectName():
            Message.setObjectName(u"Message")
        Message.resize(200, 150)
        Message.setMaximumSize(QSize(200, 150))
        Message.setStyleSheet(u"background-color: rgb(170, 0, 127);\n"
                              "color: rgb(170, 0, 127);")
        self.ok_button = QPushButton(Message)
        self.ok_button.setObjectName(u"ok_button")
        self.ok_button.setGeometry(QRect(60, 100, 75, 26))
        self.ok_button.setStyleSheet(u"QPushButton:hover {\n"
                                     "	background-color: rgb(252, 211, 255);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton {\n"
                                     "    background-color: rgb(244, 244, 244);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: rgb(244, 244, 244);\n"
                                     "}")
        self.information_label = QLabel(Message)
        self.information_label.setObjectName(u"information_label")
        self.information_label.setGeometry(QRect(10, 30, 181, 51))
        font = QFont()
        font.setPointSize(12)
        self.information_label.setFont(font)
        self.information_label.setStyleSheet(u"border-color: rgb(53, 53, 53);\n"
                                             "color: rgb(255, 255, 255);")
        self.information_label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Message)

        QMetaObject.connectSlotsByName(Message)

    # setupUi

    def retranslateUi(self, Message):
        Message.setWindowTitle(QCoreApplication.translate("Message", u"Dialog", None))
        self.ok_button.setText(QCoreApplication.translate("Message", u"Ok", None))
        self.information_label.setText(QCoreApplication.translate("Message",
                                                                  u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>",
                                                                  None))
    # retranslateUi
