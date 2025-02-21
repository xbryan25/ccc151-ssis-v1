from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QComboBox, QPushButton, \
     QLineEdit, QLabel, QFrame

from PyQt6.QtCore import Qt, QSortFilterProxyModel, QAbstractTableModel, QRegularExpression
from PyQt6.QtGui import QCursor, QFont

from utils.reset_sorting_state import ResetSortingState
from utils.get_information_codes import GetInformationCodes
from utils.custom_sort_filter_proxy_model import CustomSortFilterProxyModel
from utils.save_all_changes import SaveAllChanges
from utils.combobox_item_delegate import ComboboxItemDelegate
from utils.specific_buttons_enabler import SpecificButtonsEnabler

from students.students_page_design import Ui_MainWindow as StudentsPageUI
from students.add_student import AddStudentDialog
from students.edit_student import EditStudentDialog
from students.delete_student import DeleteStudentDialog

from helper_dialogs.input_prerequisite.input_prerequisite import InputPrerequisiteDialog
from helper_dialogs.save_item_state.confirm_save import ConfirmSaveDialog
from helper_dialogs.save_item_state.success_save_changes import SuccessSaveChangesDialog

import csv


class StudentsPage(QMainWindow, StudentsPageUI):
    def __init__(self, main_screen, students_table_model, programs_table_model, colleges_table_model):
        super().__init__()

        self.setupUi(self)

        self.set_external_stylesheet()

        self.main_screen = main_screen

        self.programs_table_model = programs_table_model
        self.colleges_table_model = colleges_table_model

        self.students_table_model = students_table_model
        self.sort_filter_proxy_model = CustomSortFilterProxyModel(self.students_table_model)

        self.students_table_view.setSortingEnabled(True)
        self.students_table_view.setModel(self.sort_filter_proxy_model)

        self.students_table_view.setAlternatingRowColors(True)

        self.horizontal_header = self.students_table_view.horizontalHeader()

        self.reset_sorting_state = ResetSortingState(self.sort_filter_proxy_model,
                                                     self.students_table_view,
                                                     "student")

        self.page_controls = self.get_page_controls()

        self.add_signals()

        SpecificButtonsEnabler.enable_delete_and_edit_buttons([self.page_controls["delete_student_button"],
                                                               self.page_controls["edit_student_button"]],
                                                              self.students_table_model)

        SpecificButtonsEnabler.enable_save_button(self.page_controls["save_changes_button"], self.students_table_model)


    def open_add_student_dialog(self):

        if self.programs_table_model.get_data()[0][0] != "":
            # Note: self.reset_item_delegates and force_reset_sort is a function

            self.add_student_dialog = AddStudentDialog(self.students_table_view, self.students_table_model,
                                                       self.programs_table_model,
                                                       self.colleges_table_model,
                                                       self.reset_item_delegates)
            self.add_student_dialog.exec()

            SpecificButtonsEnabler.enable_delete_and_edit_buttons([self.page_controls["delete_student_button"],
                                                                   self.page_controls["edit_student_button"]],
                                                                  self.students_table_model)

            SpecificButtonsEnabler.enable_save_button(self.page_controls["save_changes_button"],
                                                      self.students_table_model)

        else:
            self.input_programs_dialog = InputPrerequisiteDialog("programs")
            self.input_programs_dialog.exec()

    def open_edit_student_dialog(self):
        self.edit_student_dialog = EditStudentDialog(self.students_table_view, self.students_table_model,
                                                     self.programs_table_model,
                                                     self.colleges_table_model,
                                                     self.reset_item_delegates)
        self.edit_student_dialog.exec()

        SpecificButtonsEnabler.enable_save_button(self.page_controls["save_changes_button"],
                                                  self.students_table_model)

    def open_delete_student_dialog(self):
        # Pass tableview here, and just import adjust horizontal header

        self.delete_student_dialog = DeleteStudentDialog(self.students_table_view, self.students_table_model,
                                                         self.reset_item_delegates, self.horizontal_header)
        self.delete_student_dialog.exec()

        SpecificButtonsEnabler.enable_delete_and_edit_buttons([self.page_controls["delete_student_button"],
                                                               self.page_controls["edit_student_button"]],
                                                              self.students_table_model)

        SpecificButtonsEnabler.enable_save_button(self.page_controls["save_changes_button"],
                                                  self.students_table_model)

    def open_confirm_save_dialog(self, save_type):
        self.confirm_save_dialog = ConfirmSaveDialog()
        self.confirm_save_dialog.exec()

        if self.confirm_save_dialog.get_confirm_edit_decision():
            self.save_all_changes = SaveAllChanges(save_type,
                                                   self.students_table_model,
                                                   self.programs_table_model,
                                                   self.colleges_table_model)

            self.save_all_changes.to_csv()

            SpecificButtonsEnabler.enable_save_button(self.page_controls["save_changes_button"],
                                                      self.students_table_model)

            self.success_save_changes = SuccessSaveChangesDialog()
            self.success_save_changes.exec()

    def return_to_main_screen(self):
        self.main_screen.show()

        self.setVisible(False)

    def search_student_using_lineedit(self):
        search_type = self.page_controls["search_type_combobox"].currentIndex()

        self.students_table_model.layoutAboutToBeChanged.emit()

        self.sort_filter_proxy_model.setFilterKeyColumn(search_type)

        self.sort_filter_proxy_model.setFilterRegularExpression(QRegularExpression('^' + self.search_input_lineedit.text(),
                                                                                   QRegularExpression.PatternOption.CaseInsensitiveOption))
        # self.sort_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

        self.students_table_model.layoutChanged.emit()

        self.reset_item_delegates()

    def change_search_lineedit_placeholder(self):
        self.page_controls["search_input_lineedit"].setPlaceholderText(f"Input "
                                                                       f"{self.search_type_combobox.currentText()}")

    def add_signals(self):
        self.page_controls["add_student_button"].clicked.connect(self.open_add_student_dialog)
        self.page_controls["edit_student_button"].clicked.connect(self.open_edit_student_dialog)
        self.page_controls["delete_student_button"].clicked.connect(self.open_delete_student_dialog)
        self.page_controls["save_changes_button"].clicked.connect(lambda: self.open_confirm_save_dialog("student"))
        self.page_controls["back_to_main_button"].clicked.connect(self.return_to_main_screen)

        self.horizontal_header.sectionClicked.connect(self.reset_sorting_state.reset_sorting_state)

        self.horizontal_header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        self.horizontal_header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.horizontal_header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.horizontal_header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        self.horizontal_header.setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)
        self.horizontal_header.setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)


        self.page_controls["search_input_lineedit"].textChanged.connect(self.search_student_using_lineedit)
        self.page_controls["search_type_combobox"].currentIndexChanged.connect(self.change_search_lineedit_placeholder)

    def get_program_codes(self):
        return GetInformationCodes.for_programs(self.programs_table_model.get_data())

    def load_item_delegates_year_and_gender(self):

        # Check if self.students_table_model is empty, if so, disable combobox item delegate

        if self.students_table_model.get_data()[0][3] != "" and self.students_table_model.get_data()[0][4] != "":
            # For Year Level
            self.students_table_view.setItemDelegateForColumn(3, ComboboxItemDelegate(self.students_table_view,
                                                                                      ["1st", "2nd", "3rd",
                                                                                       "4th", "5th"]))
            for row in range(0, self.sort_filter_proxy_model.rowCount()):
                self.students_table_view.openPersistentEditor(self.sort_filter_proxy_model.index(row, 3))

            # For Gender
            self.students_table_view.setItemDelegateForColumn(4, ComboboxItemDelegate(self.students_table_view,
                                                                                      ["Male", "Female", "Others",
                                                                                             "Prefer not to say"]))

            for row in range(0, self.sort_filter_proxy_model.rowCount()):
                self.students_table_view.openPersistentEditor(self.sort_filter_proxy_model.index(row, 4))

    def load_item_delegates_program_codes(self):
        # Check if self.students_table_model is empty, if so, disable combobox item delegate

        if self.students_table_model.get_data()[0][5] != "":
            # For Program Codes

            combobox_item_delegate = ComboboxItemDelegate(self.students_table_view, self.get_program_codes())
            # combobox_item_delegate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

            self.students_table_view.setItemDelegateForColumn(5, combobox_item_delegate)

            for row in range(0, self.sort_filter_proxy_model.rowCount()):
                self.students_table_view.openPersistentEditor(self.sort_filter_proxy_model.index(row, 5))

    # Dynamic change of combobox
    # https://www.pythonguis.com/faq/how-to-clear-remove-combobox-delegate-data-from-qtableview/

    def reset_item_delegates(self, state=None):

        if state:
            self.reset_sorting_state.force_reset_sort()

        self.sort_filter_proxy_model.beginResetModel()
        self.sort_filter_proxy_model.endResetModel()

        self.load_item_delegates_program_codes()
        self.load_item_delegates_year_and_gender()

    def set_external_stylesheet(self):
        with open("../assets/qss_files/entity_page_style.qss", "r") as file:
            self.setStyleSheet(file.read())

    def get_page_controls(self):
        back_to_main_button = (self.back_and_search_frame.findChild(QFrame, "back_frame").
                               findChild(QPushButton, "back_to_main_button"))

        search_input_lineedit = (self.back_and_search_frame.findChild(QFrame, "search_frame").
                                 findChild(QLineEdit, "search_input_lineedit"))

        search_type_combobox = (self.back_and_search_frame.findChild(QFrame, "search_frame").
                                findChild(QComboBox, "search_type_combobox"))

        add_student_button = (self.buttons_frame.findChild(QPushButton, "add_student_button"))

        delete_student_button = (self.buttons_frame.findChild(QPushButton, "delete_student_button"))

        edit_student_button = (self.buttons_frame.findChild(QPushButton, "edit_student_button"))

        save_changes_button = (self.buttons_frame.findChild(QPushButton, "save_changes_button"))

        view_demographics_button = (self.buttons_frame.findChild(QPushButton, "view_demographics_button"))

        title_label = (self.header_frame.findChild(QLabel, "title_label"))

        type_label = (self.header_frame.findChild(QLabel, "type_label"))

        return {"back_to_main_button": back_to_main_button,
                "search_input_lineedit": search_input_lineedit,
                "search_type_combobox": search_type_combobox,
                "add_student_button": add_student_button,
                "delete_student_button": delete_student_button,
                "edit_student_button": edit_student_button,
                "save_changes_button": save_changes_button,
                "view_demographics_button": view_demographics_button,
                "title_label": title_label,
                "type_label": type_label}

    def closeEvent(self, event):
        if self.students_table_model.get_has_changes():
            self.open_confirm_save_dialog("student")

        event.accept()

    def resizeEvent(self, event):
        print(self.size())

        # TODO: Increase/decrease font of buttons when it is getting resized
        font = QFont()
        font.setFamily("Segoe UI Semibold")

        # 48 is an arbitrary number obtained from 534/11, 534 is the minimum width, 11 is the minimum font size
        font.setPointSize(int(self.height() / 48))

        font.setBold(True)
        font.setWeight(75)

        self.page_controls["back_to_main_button"].setFont(font)
        self.page_controls["add_student_button"].setFont(font)
        self.page_controls["delete_student_button"].setFont(font)
        self.page_controls["edit_student_button"].setFont(font)
        self.page_controls["save_changes_button"].setFont(font)
        self.page_controls["view_demographics_button"].setFont(font)
