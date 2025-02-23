from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import QSize

from helper_dialogs.input_prerequisite.input_prerequisite_design import Ui_Dialog as InputPrerequisiteUI


class InputPrerequisiteDialog(QDialog, InputPrerequisiteUI):
    def __init__(self, prerequisite_type):
        super().__init__()

        self.setupUi(self)

        self.set_external_stylesheet()

        self.prerequisite_type = prerequisite_type

        self.proceed_button.clicked.connect(self.close_dialog)

        self.display_prerequisite_type()

    def display_prerequisite_type(self):
        if self.prerequisite_type == "college":
            self.message_label.setText("No colleges found, input colleges first.")
            self.setWindowTitle("No colleges found")

        elif self.prerequisite_type == "programs":
            self.message_label.setText("No programs found, input programs first.")
            self.setWindowTitle("No programs found")

        elif self.prerequisite_type == "students":
            self.message_label.setText("No students found, input students first.")
            self.setWindowTitle("No students found")

    def close_dialog(self):
        self.close()

    def set_external_stylesheet(self):

        with open("../assets/qss_files/dialog_style.qss", "r") as file:
            self.setStyleSheet(file.read())

