# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_images.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGraphicsView, QPushButton,
                               QSizePolicy, QWidget, QGraphicsScene)


class view_images(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(787, 417)
        Dialog.setMinimumSize(QSize(787, 417))
        Dialog.setMaximumSize(QSize(787, 417))
        Dialog.setStyleSheet(u"background-color: rgb(170, 0, 127);")
        self.graphicsView = QGraphicsView(Dialog)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(25, 21, 741, 311))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 360, 111, 41))
        font = QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton:hover {\n"
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

    def display_images(self, image_paths):
        # Создаем сцену для отображения изображений
        scene = QGraphicsScene()

        # Начальная позиция для размещения изображений
        x_offset, y_offset = 0, 0
        max_width = self.graphicsView.width() - 20  # ширина доступного пространства
        padding = 10  # Отступ между изображениями

        # Максимальный размер изображения (чтобы не было слишком большим)
        max_image_size = 200  # пикселей

        # Высота самой большой строки для перехода на следующую строку
        max_row_height = 0

        # Загружаем и добавляем каждое изображение в сцену
        for image_path in image_paths:
            pixmap = QPixmap(image_path)

            # Масштабируем изображение, чтобы вписать его в максимальный размер
            if pixmap.width() > max_image_size or pixmap.height() > max_image_size:
                pixmap = pixmap.scaled(max_image_size, max_image_size, Qt.KeepAspectRatio)

            # Получаем размеры изображения после масштабирования
            scaled_width = pixmap.width()
            scaled_height = pixmap.height()

            # Проверяем, вмещается ли изображение по ширине, если нет — переносим на следующую строку
            if x_offset + scaled_width > max_width:
                x_offset = 0  # перенос на новую строку
                y_offset += max_row_height + padding  # обновляем y_offset для новой строки
                max_row_height = 0  # сброс высоты строки

            # Добавляем изображение на сцену с текущим x и y смещением
            pixmap_item = scene.addPixmap(pixmap)
            pixmap_item.setPos(x_offset, y_offset)

            # Обновляем координаты для следующего изображения
            x_offset += scaled_width + padding
            max_row_height = max(max_row_height, scaled_height)  # обновляем максимальную высоту строки

        # Устанавливаем сцену в QGraphicsView
        self.graphicsView.setScene(scene)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi
