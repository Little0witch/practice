import sys
from PySide6.QtWidgets import QApplication, QDialog
from gui.class_main_window import MyMainWindow
from gui.class_promt_window import promtWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    promt_win = promtWindow()
    if promt_win.exec() == QDialog.Accepted:
        window = MyMainWindow()
        sys.exit(app.exec())