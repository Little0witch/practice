from PySide6.QtWidgets import QMainWindow, QFileDialog, QDialog
from gui.choose_delete_dir_window import Ui_Choose_var_delete
from gui.error_window import Ui_Error
from gui.main_window import Ui_MainWindow
from gui.message_window import Ui_Message
from core.functional import search_dupl, show_dupls, save_to_xlsx
from gui.show_images import view_images


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.selected_folders = []
        self.path_save_xlsx = ''

        self.add_dir_button.clicked.connect(self.browse_folder)
        self.checkBox.clicked.connect(self.is_save_data_to_file)
        self.delete_dir_button.clicked.connect(self.show_choose_delete_dir_window)
        self.search_dup_button.clicked.connect(self.clicked_search_dupl)


    # выбор папок для поиска изображений
    def browse_folder(self):
        directory = QFileDialog.getExistingDirectory(self, "Выберите папку для поиска дубликатов")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            if directory in self.selected_folders:
                self.show_error_window("Папка уже добавлена.")
            else:
                self.list_dir_widget.addItem(directory)
                self.add_selected_folder(directory)

    # добавление пути в список для дальнейшей обработки
    def add_selected_folder(self, directory):
        self.selected_folders.append(directory)

    # выполнение действий при нажатии checkbox (нажатие и отжатие)
    def is_save_data_to_file(self, state):
        if state:
            self.choose_path_save_xlsx()
        else:
            self.delete_path_save_xlsx()

    # выбор пути для сохранения файла с путями дубликатов
    def choose_path_save_xlsx(self):
        directory = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения файла")

        if directory:
            self.path_save_xlsx = directory
        else:
            self.checkBox.setChecked(False)
            self.delete_path_save_xlsx()

    # удаление пути для сохранения файда xlsx
    def delete_path_save_xlsx(self):
        self.path_save_xlsx = ''

    def choose_path_from_list(self):
        if self.list_dir_widget.count() and self.list_dir_widget.currentItem():
            return self.list_dir_widget.currentItem()
        else:
            return None

    def delete_all_dir(self):
        self.selected_folders.clear()

    def delete_this_dir(self, path):
        self.selected_folders.remove(path)

    # вызов окна ошибки
    def show_error_window(self, message):
        error_dialog = QDialog()
        error_ui = Ui_Error()
        error_ui.setupUi(error_dialog)

        error_ui.information_label.setText(message)
        error_ui.ok_button.clicked.connect(error_dialog.accept)
        error_dialog.exec()

    def show_information_window(self, message):
        message_dialog = QDialog()
        information_ui = Ui_Message()
        information_ui.setupUi(message_dialog)

        information_ui.information_label.setText(message)
        information_ui.ok_button.clicked.connect(message_dialog.accept)
        message_dialog.exec()

    def show_choose_delete_dir_window(self):
        if len(self.selected_folders) != 0:
            window_dialog = QDialog()
            choose_delete_dir_ui = Ui_Choose_var_delete()
            choose_delete_dir_ui.setupUi(window_dialog)

            current_item_Qlist = self.choose_path_from_list()
            if current_item_Qlist is None:
                choose_delete_dir_ui.path.setText("Папка для удаления не выбрана.")
                choose_path = None
            else:
                choose_path = current_item_Qlist.text()
                choose_delete_dir_ui.path.setText(choose_path)

            def delete_this_dir_and_close_window():
                if choose_path is None:
                    self.show_error_window("Папка для удаления не выбрана.")
                else:
                    self.delete_this_dir(choose_path)
                    self.list_dir_widget.takeItem(self.list_dir_widget.row(current_item_Qlist))

                    window_dialog.close()

            def delete_all_dir_and_close_window():
                self.delete_all_dir()
                self.list_dir_widget.clear()
                window_dialog.close()

            choose_delete_dir_ui.all_dir_del_button.clicked.connect(delete_all_dir_and_close_window)
            choose_delete_dir_ui.del_this_dir_button.clicked.connect(delete_this_dir_and_close_window)

            window_dialog.exec()
        else:
            self.show_error_window("Нет папок в списке.")


    def clicked_search_dupl(self):
        if len(self.selected_folders) != 0:
            flag_result, pd_result_search = search_dupl(self.selected_folders)

            if flag_result:
                self.show_image_display_window(pd_result_search)
                # show_dupls(pd_result_search)
                save_to_xlsx(pd_result_search, self.path_save_xlsx)
            else:
                self.show_information_window("Дубликаты не найдены.")

        else:
            self.show_error_window("Нет папок в списке.")

    def show_image_display_window(self, df_duplitation):
        image_paths = df_duplitation['File Path'].tolist()  # Получение списка путей к изображениям
        dialog = QDialog()
        image_display = view_images()
        image_display.setupUi(dialog)
        image_display.display_images(image_paths)
        image_display.pushButton.clicked.connect(dialog.accept)
        dialog.exec()