# Form implementation generated from reading ui file 'edit_program.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 330)
        Dialog.setMinimumSize(QtCore.QSize(450, 330))
        Dialog.setMaximumSize(QtCore.QSize(450, 330))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
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
        self.edit_program_button = QtWidgets.QPushButton(parent=Dialog)
        self.edit_program_button.setEnabled(False)
        self.edit_program_button.setMinimumSize(QtCore.QSize(432, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.edit_program_button.setFont(font)
        self.edit_program_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.edit_program_button.setObjectName("edit_program_button")
        self.gridLayout.addWidget(self.edit_program_button, 4, 0, 1, 3)
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 3)
        self.new_college_code_combobox = QtWidgets.QComboBox(parent=self.frame)
        self.new_college_code_combobox.setEnabled(False)
        self.new_college_code_combobox.setMinimumSize(QtCore.QSize(231, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.new_college_code_combobox.setFont(font)
        self.new_college_code_combobox.setEditable(True)
        self.new_college_code_combobox.setObjectName("new_college_code_combobox")
        self.gridLayout_2.addWidget(self.new_college_code_combobox, 4, 3, 1, 1)
        self.program_to_edit_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.program_to_edit_label.setFont(font)
        self.program_to_edit_label.setObjectName("program_to_edit_label")
        self.gridLayout_2.addWidget(self.program_to_edit_label, 0, 1, 1, 1)
        self.new_college_code_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_college_code_label.setFont(font)
        self.new_college_code_label.setObjectName("new_college_code_label")
        self.gridLayout_2.addWidget(self.new_college_code_label, 4, 1, 1, 1)
        self.program_to_edit_combobox = QtWidgets.QComboBox(parent=self.frame)
        self.program_to_edit_combobox.setMinimumSize(QtCore.QSize(231, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.program_to_edit_combobox.setFont(font)
        self.program_to_edit_combobox.setEditable(True)
        self.program_to_edit_combobox.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.program_to_edit_combobox.setObjectName("program_to_edit_combobox")
        self.program_to_edit_combobox.addItem("")
        self.gridLayout_2.addWidget(self.program_to_edit_combobox, 0, 3, 1, 1)
        self.new_program_name_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_program_name_label.setFont(font)
        self.new_program_name_label.setObjectName("new_program_name_label")
        self.gridLayout_2.addWidget(self.new_program_name_label, 3, 1, 1, 1)
        self.new_program_code_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_program_code_label.setFont(font)
        self.new_program_code_label.setObjectName("new_program_code_label")
        self.gridLayout_2.addWidget(self.new_program_code_label, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 4, 3, 1)
        spacerItem3 = QtWidgets.QSpacerItem(15, 15, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 3, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 2, 3, 1)
        self.new_program_name_lineedit = QtWidgets.QLineEdit(parent=self.frame)
        self.new_program_name_lineedit.setEnabled(False)
        self.new_program_name_lineedit.setMinimumSize(QtCore.QSize(231, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.new_program_name_lineedit.setFont(font)
        self.new_program_name_lineedit.setObjectName("new_program_name_lineedit")
        self.gridLayout_2.addWidget(self.new_program_name_lineedit, 3, 3, 1, 1)
        self.new_program_code_lineedit = QtWidgets.QLineEdit(parent=self.frame)
        self.new_program_code_lineedit.setEnabled(False)
        self.new_program_code_lineedit.setMinimumSize(QtCore.QSize(231, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.new_program_code_lineedit.setFont(font)
        self.new_program_code_lineedit.setObjectName("new_program_code_lineedit")
        self.gridLayout_2.addWidget(self.new_program_code_lineedit, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 3)
        self.line_1 = QtWidgets.QFrame(parent=Dialog)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_1.setLineWidth(2)
        self.line_1.setMidLineWidth(2)
        self.line_1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_1.setObjectName("line_1")
        self.gridLayout.addWidget(self.line_1, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=Dialog)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit program"))
        self.header_label.setText(_translate("Dialog", "Edit information"))
        self.edit_program_button.setText(_translate("Dialog", "Edit program"))
        self.program_to_edit_label.setText(_translate("Dialog", "Program to edit"))
        self.new_college_code_label.setText(_translate("Dialog", "New College Code"))
        self.program_to_edit_combobox.setItemText(0, _translate("Dialog", "--Select Program Code--"))
        self.new_program_name_label.setText(_translate("Dialog", "New Program Name"))
        self.new_program_code_label.setText(_translate("Dialog", "New Program Code"))
