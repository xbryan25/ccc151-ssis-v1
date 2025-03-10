# Form implementation generated from reading ui file 'delete_program.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 195)
        Dialog.setMinimumSize(QtCore.QSize(370, 195))
        Dialog.setMaximumSize(QtCore.QSize(370, 195))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_label = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.header_label.setFont(font)
        self.header_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_label.setObjectName("header_label")
        self.verticalLayout.addWidget(self.header_label)
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)

        self.college_code_filter_combobox = QtWidgets.QComboBox(parent=self.frame)
        self.college_code_filter_combobox.setEnabled(True)
        self.college_code_filter_combobox.setMinimumSize(QtCore.QSize(155, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.college_code_filter_combobox.setFont(font)
        self.college_code_filter_combobox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.college_code_filter_combobox.setEditable(True)
        self.college_code_filter_combobox.setObjectName("college_code_filter_combobox")
        self.college_code_filter_combobox.addItem("")
        self.gridLayout.addWidget(self.college_code_filter_combobox, 1, 2, 1, 1)

        self.program_to_delete_combobox = QtWidgets.QComboBox(parent=self.frame)
        self.program_to_delete_combobox.setEnabled(True)
        self.program_to_delete_combobox.setMinimumSize(QtCore.QSize(155, 23))
        self.program_to_delete_combobox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.program_to_delete_combobox.setFont(font)
        self.program_to_delete_combobox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.program_to_delete_combobox.setEditable(True)
        self.program_to_delete_combobox.setObjectName("program_to_delete_combobox")
        self.program_to_delete_combobox.addItem("")
        self.gridLayout.addWidget(self.program_to_delete_combobox, 2, 2, 1, 1)

        self.program_code_label = QtWidgets.QLabel(parent=self.frame)
        self.program_code_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.program_code_label.setFont(font)
        self.program_code_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.program_code_label.setObjectName("program_code_label")
        self.gridLayout.addWidget(self.program_code_label, 2, 0, 1, 1)
        self.college_code_filter_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.college_code_filter_label.setFont(font)
        self.college_code_filter_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.college_code_filter_label.setObjectName("college_code_filter_label")
        self.gridLayout.addWidget(self.college_code_filter_label, 1, 0, 1, 1)

        self.verticalLayout.addWidget(self.frame)
        self.delete_program_button = QtWidgets.QPushButton(parent=Dialog)
        self.delete_program_button.setEnabled(False)
        self.delete_program_button.setMinimumSize(QtCore.QSize(352, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.delete_program_button.setFont(font)
        self.delete_program_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_program_button.setObjectName("delete_program_button")
        self.verticalLayout.addWidget(self.delete_program_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sequence | Delete a program"))
        self.header_label.setText(_translate("Dialog", "Select a program to delete"))
        self.program_to_delete_combobox.setItemText(0, _translate("Dialog", "--Select a program--"))
        self.program_code_label.setText(_translate("Dialog", "Program Code"))
        self.college_code_filter_label.setText(_translate("Dialog", "College Code Filter"))
        self.college_code_filter_combobox.setItemText(0, _translate("Dialog", "--Select a college--"))
        self.delete_program_button.setText(_translate("Dialog", "Delete program"))
