# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'promt_window.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(635, 442)
        font = QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"background-color: rgb(170, 0, 127);\n"
                             "color: rgb(170, 0, 127);")
        self.promt_text = QLabel(Dialog)
        self.promt_text.setObjectName(u"promt_text")
        self.promt_text.setGeometry(QRect(30, 30, 571, 321))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setWeight(QFont.Medium)
        font1.setKerning(False)
        font1.setHintingPreference(QFont.PreferVerticalHinting)
        self.promt_text.setFont(font1)
        self.promt_text.setStyleSheet(u"border-color: rgb(53, 53, 53);\n"
                                      "color: rgb(255, 255, 255);")
        self.promt_text.setTextFormat(Qt.TextFormat.AutoText)
        self.promt_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.promt_text.setWordWrap(True)
        self.start_button = QPushButton(Dialog)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(240, 370, 161, 51))
        font2 = QFont()
        font2.setPointSize(13)
        self.start_button.setFont(font2)
        self.start_button.setStyleSheet(u"QPushButton:hover {\n"
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

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.promt_text.setText(QCoreApplication.translate("Dialog",
                                                           u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\u041f\u0440\u0438\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e, \u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c!</span></p><p align=\"justify\"><span style=\" font-size:14pt;\">\u042d\u0442\u043e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u043e \u043f\u043e\u0438\u0441\u043a\u0443 \u0434\u0443\u0431\u043b\u0438\u043a\u0430\u0442\u043e\u0432 \u0432 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0445 \u043f\u0430\u043f\u043a\u0430\u0445. \u0415\u0441\u043b\u0438 \u0432 \u043f\u0430\u043f\u043a\u0435 \u0435\u0441\u0442\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438, \u0442\u043e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0432 \u043d\u0438\u0445 \u043d\u0435 \u0431\u0443\u0434\u0443\u0442 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u044b. \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0442\u044c \u043f\u0430\u043f\u043a\u0438 \u0441 \u043f\u043e\u043c"
                                                           "\u043e\u0449\u044c\u044e \u043a\u043d\u043e\u043f\u043a\u0438 &quot;\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0430\u043f\u043a\u0443&quot;. \u0414\u043b\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0439 \u043f\u0430\u043f\u043a\u0438 \u043d\u0443\u0436\u043d\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0435\u0435 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u044b\u0445 \u043f\u0430\u043f\u043e\u043a \u0438 \u043a\u043b\u0438\u043a\u043d\u0443\u0442\u044c \u043f\u043e \u043a\u043d\u043e\u043f\u043a\u0435 &quot;\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u0430\u043f\u043a\u0443&quot;, \u0430 \u0432 \u0441\u043f\u043e\u043c\u043e\u0433\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u043c \u043e\u043a\u043d\u0435 \u043d\u0430\u0436\u0430\u0442\u044c\u044c \u043a\u043d\u043e\u043f\u043a\u0443 &quot;\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d"
                                                           "\u0443\u044e \u043f\u0430\u043f\u043a\u0443&quot;. \u0415\u0441\u043b\u0438 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u0443\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u0441\u0435 \u043f\u0430\u043f\u043a\u0438, \u0442\u043e \u043f\u0440\u043e\u0441\u0442\u043e \u043d\u0430\u0436\u043c\u0438 &quot;\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u0441\u0435 \u043f\u0430\u043f\u043a\u0438&quot;. \u0414\u043b\u044f \u0443\u0434\u043e\u0431\u0441\u0442\u0432\u0430, \u043f\u0443\u0442\u0438 \u043a \u0434\u0443\u0431\u043b\u0438\u043a\u0430\u0442\u0430\u043c \u043c\u043e\u0436\u043d\u043e \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u0444\u0430\u0439\u043b result.xlsx.</span></p><p align=\"center\"><span style=\" font-size:14pt;\">\u041f\u0440\u0438\u044f\u0442\u043d\u043e\u0433\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044f! </span></p></body></html>",
                                                           None))
        self.start_button.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
    # retranslateUi
