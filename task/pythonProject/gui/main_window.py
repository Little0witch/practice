# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QListWidget,
                               QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 300)
        MainWindow.setMinimumSize(QSize(800, 300))
        MainWindow.setMaximumSize(QSize(800, 300))
        MainWindow.setStyleSheet(u"background-color: rgb(170, 0, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color: rgb(170, 0, 127);")
        self.add_dir_button = QPushButton(self.centralwidget)
        self.add_dir_button.setObjectName(u"add_dir_button")
        self.add_dir_button.setGeometry(QRect(10, 80, 141, 31))
        font = QFont()
        font.setPointSize(12)
        self.add_dir_button.setFont(font)
        self.add_dir_button.setStyleSheet(u"QPushButton:hover {\n"
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
        self.list_dir_widget = QListWidget(self.centralwidget)
        self.list_dir_widget.setObjectName(u"list_dir_widget")
        self.list_dir_widget.setGeometry(QRect(160, 30, 571, 192))
        self.list_dir_widget.setFont(font)
        self.list_dir_widget.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        self.label_over_list_dir = QLabel(self.centralwidget)
        self.label_over_list_dir.setObjectName(u"label_over_list_dir")
        self.label_over_list_dir.setGeometry(QRect(160, 10, 141, 18))
        self.label_over_list_dir.setFont(font)
        self.label_over_list_dir.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_over_list_dir.setTextFormat(Qt.TextFormat.AutoText)
        self.delete_dir_button = QPushButton(self.centralwidget)
        self.delete_dir_button.setObjectName(u"delete_dir_button")
        self.delete_dir_button.setGeometry(QRect(10, 130, 141, 31))
        self.delete_dir_button.setFont(font)
        self.delete_dir_button.setStyleSheet(u"QPushButton:hover {\n"
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
        self.search_dup_button = QPushButton(self.centralwidget)
        self.search_dup_button.setObjectName(u"search_dup_button")
        self.search_dup_button.setGeometry(QRect(580, 240, 151, 31))
        self.search_dup_button.setFont(font)
        self.search_dup_button.setStyleSheet(u"QPushButton:hover {\n"
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
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(160, 240, 321, 22))
        font1 = QFont()
        font1.setPointSize(11)
        self.checkBox.setFont(font1)
        self.checkBox.setStyleSheet(u"QCheckBox{\n"
                                    "background-color: rgb(170, 0, 127);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "QCheckBox:checked {\n"
                                    "	selection-color: rgb(0, 0, 0);\n"
                                    "}\n"
                                    "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Practice 2024", None))
        self.add_dir_button.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0430\u043f\u043a\u0443",
                                                               None))
        self.label_over_list_dir.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u043f\u0430\u043f\u043a\u0438",
                                                                    None))
        self.delete_dir_button.setText(QCoreApplication.translate("MainWindow",
                                                                  u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u0430\u043f\u043a\u0443",
                                                                  None))
        self.search_dup_button.setText(QCoreApplication.translate("MainWindow",
                                                                  u"\u041f\u043e\u0438\u0441\u043a \u0434\u0443\u0431\u043b\u0438\u043a\u0430\u0442\u043e\u0432",
                                                                  None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0434\u0443\u0431\u043b\u0438\u043a\u0430\u0442\u043e\u0432 \u0432 \"result.xlsx\"",
                                                         None))
    # retranslateUi
