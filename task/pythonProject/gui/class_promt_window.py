from PySide6.QtWidgets import QDialog

from gui.promt_window import Ui_Dialog


class promtWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.start_button.clicked.connect(self.accept)

