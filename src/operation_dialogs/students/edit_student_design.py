# Form implementation generated from reading ui file 'edit_student.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 484)
        Dialog.setMinimumSize(QtCore.QSize(450, 484))
        Dialog.setMaximumSize(QtCore.QSize(450, 484))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.line_1 = QtWidgets.QFrame(parent=Dialog)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_1.setLineWidth(2)
        self.line_1.setMidLineWidth(2)
        self.line_1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_1.setObjectName("line_1")
        self.gridLayout.addWidget(self.line_1, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.header_label = QtWidgets.QLabel(parent=Dialog)
        self.header_label.setMinimumSize(QtCore.QSize(200, 50))
        self.header_label.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.header_label.setFont(font)
        self.header_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_label.setObjectName("header_label")
        self.gridLayout.addWidget(self.header_label, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=Dialog)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 2, 1, 1)
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.new_program_code_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_program_code_label.setFont(font)
        self.new_program_code_label.setObjectName("new_program_code_label")
        self.gridLayout_2.addWidget(self.new_program_code_label, 9, 1, 1, 1)
        self.new_gender_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_gender_label.setFont(font)
        self.new_gender_label.setObjectName("new_gender_label")
        self.gridLayout_2.addWidget(self.new_gender_label, 6, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 3)

        self.new_first_name_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_first_name_label.setFont(font)
        self.new_first_name_label.setObjectName("new_first_name_label")
        self.gridLayout_2.addWidget(self.new_first_name_label, 3, 1, 1, 1)
        self.new_year_level_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_year_level_label.setFont(font)
        self.new_year_level_label.setObjectName("new_year_level_label")
        self.gridLayout_2.addWidget(self.new_year_level_label, 5, 1, 1, 1)

        self.new_last_name_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_last_name_label.setFont(font)
        self.new_last_name_label.setObjectName("new_last_name_label")
        self.gridLayout_2.addWidget(self.new_last_name_label, 4, 1, 1, 1)

        self.new_id_number_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_id_number_label.setFont(font)
        self.new_id_number_label.setObjectName("new_id_number_label")
        self.gridLayout_2.addWidget(self.new_id_number_label, 2, 1, 1, 1)

        self.student_to_edit_combobox = QtWidgets.QComboBox(parent=self.frame)
        self.student_to_edit_combobox.setMinimumSize(QtCore.QSize(236, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.student_to_edit_combobox.setFont(font)
        self.student_to_edit_combobox.setEditable(True)
        self.student_to_edit_combobox.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.student_to_edit_combobox.setObjectName("student_to_edit_combobox")
        self.student_to_edit_combobox.addItem("")
        self.gridLayout_2.addWidget(self.student_to_edit_combobox, 0, 3, 1, 1)

        self.new_id_number_lineedit = QtWidgets.QLineEdit(parent=self.frame)
        self.new_id_number_lineedit.setEnabled(False)
        self.new_id_number_lineedit.setMinimumSize(QtCore.QSize(236, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.new_id_number_lineedit.setFont(font)
        self.new_id_number_lineedit.setObjectName("new_id_number_lineedit")
        self.gridLayout_2.addWidget(self.new_id_number_lineedit, 2, 3, 1, 1)

        self.new_first_name_lineedit = QtWidgets.QLineEdit(parent=self.frame)
        self.new_first_name_lineedit.setEnabled(False)
        self.new_first_name_lineedit.setMinimumSize(QtCore.QSize(236, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.new_first_name_lineedit.setFont(font)
        self.new_first_name_lineedit.setObjectName("new_first_name_lineedit")
        self.gridLayout_2.addWidget(self.new_first_name_lineedit, 3, 3, 1, 1)

        self.new_last_name_lineedit = QtWidgets.QLineEdit(parent=self.frame)
        self.new_last_name_lineedit.setEnabled(False)
        self.new_last_name_lineedit.setMinimumSize(QtCore.QSize(236, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.new_last_name_lineedit.setFont(font)
        self.new_last_name_lineedit.setObjectName("new_last_name_lineedit")
        self.gridLayout_2.addWidget(self.new_last_name_lineedit, 4, 3, 1, 1)

        self.new_year_level_combobox = QtWidgets.QComboBox(parent=self.frame)
        self.new_year_level_combobox.setEnabled(False)
        self.new_year_level_combobox.setMinimumSize(QtCore.QSize(236, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_year_level_combobox.setFont(font)
        self.new_year_level_combobox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.new_year_level_combobox.setObjectName("new_year_level_combobox")
        self.new_year_level_combobox.addItem("")
        self.new_year_level_combobox.setItemText(0, "")
        self.new_year_level_combobox.addItem("")
        self.new_year_level_combobox.addItem("")
        self.new_year_level_combobox.addItem("")
        self.new_year_level_combobox.addItem("")
        self.new_year_level_combobox.addItem("")
        self.gridLayout_2.addWidget(self.new_year_level_combobox, 5, 3, 1, 1)

        self.new_gender_combobox = QtWidgets.QComboBox(parent=self.frame)
        self.new_gender_combobox.setEnabled(False)
        self.new_gender_combobox.setMinimumSize(QtCore.QSize(236, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_gender_combobox.setFont(font)
        self.new_gender_combobox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.new_gender_combobox.setObjectName("new_gender_combobox")
        self.new_gender_combobox.addItem("")
        self.new_gender_combobox.setItemText(0, "")
        self.new_gender_combobox.addItem("")
        self.new_gender_combobox.addItem("")
        self.new_gender_combobox.addItem("")
        self.new_gender_combobox.addItem("")
        self.gridLayout_2.addWidget(self.new_gender_combobox, 6, 3, 1, 1)

        self.college_code_combobox = QtWidgets.QComboBox(parent=self.frame)
        self.college_code_combobox.setEnabled(False)
        self.college_code_combobox.setMinimumSize(QtCore.QSize(236, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.college_code_combobox.setFont(font)
        self.college_code_combobox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.college_code_combobox.setEditable(True)
        self.college_code_combobox.setObjectName("college_code_combobox")
        self.college_code_combobox.addItem("")
        self.college_code_combobox.setItemText(0, "")
        self.gridLayout_2.addWidget(self.college_code_combobox, 8, 3, 1, 1)

        self.new_program_code_combobox = QtWidgets.QComboBox(parent=self.frame)
        self.new_program_code_combobox.setEnabled(False)
        self.new_program_code_combobox.setMinimumSize(QtCore.QSize(236, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_program_code_combobox.setFont(font)
        self.new_program_code_combobox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.new_program_code_combobox.setEditable(True)
        self.new_program_code_combobox.setFrame(True)
        self.new_program_code_combobox.setObjectName("new_program_code_combobox")
        self.new_program_code_combobox.addItem("")
        self.new_program_code_combobox.setItemText(0, "")
        self.gridLayout_2.addWidget(self.new_program_code_combobox, 9, 3, 1, 1)

        self.student_to_edit_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.student_to_edit_label.setFont(font)
        self.student_to_edit_label.setObjectName("student_to_edit_label")
        self.gridLayout_2.addWidget(self.student_to_edit_label, 0, 1, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 2, 5, 1)
        spacerItem4 = QtWidgets.QSpacerItem(15, 15, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 0, 5, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 4, 5, 1)

        self.college_code_filter_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.college_code_filter_label.setFont(font)
        self.college_code_filter_label.setObjectName("college_code_filter_label")
        self.gridLayout_2.addWidget(self.college_code_filter_label, 8, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem6, 7, 1, 1, 3)

        self.gridLayout.addWidget(self.frame, 2, 0, 1, 3)
        self.edit_student_button = QtWidgets.QPushButton(parent=Dialog)
        self.edit_student_button.setEnabled(False)
        self.edit_student_button.setMinimumSize(QtCore.QSize(432, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.edit_student_button.setFont(font)
        self.edit_student_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.edit_student_button.setObjectName("edit_student_button")
        self.gridLayout.addWidget(self.edit_student_button, 4, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sequence | Edit a student"))
        self.header_label.setText(_translate("Dialog", "Edit information"))
        self.new_program_code_label.setText(_translate("Dialog", "New Program Code"))
        self.new_gender_label.setText(_translate("Dialog", "New Gender"))
        self.student_to_edit_combobox.setItemText(0, _translate("Dialog", "--Select ID Number--"))
        self.new_year_level_combobox.setItemText(1, _translate("Dialog", "1st"))
        self.new_year_level_combobox.setItemText(2, _translate("Dialog", "2nd"))
        self.new_year_level_combobox.setItemText(3, _translate("Dialog", "3rd"))
        self.new_year_level_combobox.setItemText(4, _translate("Dialog", "4th"))
        self.new_year_level_combobox.setItemText(5, _translate("Dialog", "5th"))
        self.new_first_name_label.setText(_translate("Dialog", "New First Name"))
        self.new_year_level_label.setText(_translate("Dialog", "New Year Level"))
        self.new_gender_combobox.setItemText(1, _translate("Dialog", "Male"))
        self.new_gender_combobox.setItemText(2, _translate("Dialog", "Female"))
        self.new_gender_combobox.setItemText(3, _translate("Dialog", "Others"))
        self.new_gender_combobox.setItemText(4, _translate("Dialog", "Prefer not to say"))
        self.new_id_number_label.setText(_translate("Dialog", "New ID Number"))
        self.new_last_name_label.setText(_translate("Dialog", "New Last Name"))
        self.student_to_edit_label.setText(_translate("Dialog", "Student To Edit"))
        self.college_code_filter_label.setText(_translate("Dialog", "College Code Filter"))
        self.edit_student_button.setText(_translate("Dialog", "Edit student"))
