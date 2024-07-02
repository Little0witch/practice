# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choose_delete_dir_window.ui'
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


class Ui_Choose_var_delete(object):
    def setupUi(self, Choose_var_delete):
        if not Choose_var_delete.objectName():
            Choose_var_delete.setObjectName(u"Choose_var_delete")
        Choose_var_delete.resize(400, 246)
        Choose_var_delete.setMaximumSize(QSize(400, 246))
        font = QFont()
        font.setPointSize(12)
        Choose_var_delete.setFont(font)
        Choose_var_delete.setStyleSheet(u"background-color: rgb(170, 0, 127);\n"
                                        "color: rgb(170, 0, 127);")
        self.path = QLabel(Choose_var_delete)
        self.path.setObjectName(u"path")
        self.path.setGeometry(QRect(30, 40, 351, 61))
        self.path.setStyleSheet(u"border-color: rgb(53, 53, 53);\n"
                                "color: rgb(255, 255, 255);")
        self.del_this_dir_button = QPushButton(Choose_var_delete)
        self.del_this_dir_button.setObjectName(u"del_this_dir_button")
        self.del_this_dir_button.setGeometry(QRect(20, 150, 171, 61))
        self.del_this_dir_button.setFont(font)
        self.del_this_dir_button.setStyleSheet(u"QPushButton:hover {\n"
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
        self.all_dir_del_button = QPushButton(Choose_var_delete)
        self.all_dir_del_button.setObjectName(u"all_dir_del_button")
        self.all_dir_del_button.setGeometry(QRect(210, 150, 171, 61))
        self.all_dir_del_button.setFont(font)
        self.all_dir_del_button.setStyleSheet(u"QPushButton:hover {\n"
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

        self.retranslateUi(Choose_var_delete)

        QMetaObject.connectSlotsByName(Choose_var_delete)

    # setupUi

    def retranslateUi(self, Choose_var_delete):
        Choose_var_delete.setWindowTitle(QCoreApplication.translate("Choose_var_delete", u"Dialog", None))
        self.path.setText(QCoreApplication.translate("Choose_var_delete",
                                                     u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">TextLabel</span></p></body></html>",
                                                     None))
        self.del_this_dir_button.setText(QCoreApplication.translate("Choose_var_delete",
                                                                    u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u0443\u044e\n"
                                                                    "\u043f\u0430\u043f\u043a\u0443", None))
        self.all_dir_del_button.setText(QCoreApplication.translate("Choose_var_delete",
                                                                   u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u0441\u0435\n"
                                                                   "\u043f\u0430\u043f\u043a\u0438", None))
    # retranslateUi
