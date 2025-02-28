# Form implementation generated from reading ui file 'delete_college.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 156)
        Dialog.setMinimumSize(QtCore.QSize(370, 156))
        Dialog.setMaximumSize(QtCore.QSize(370, 156))
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.college_code_label = QtWidgets.QLabel(parent=self.frame)
        self.college_code_label.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.college_code_label.setFont(font)
        self.college_code_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.college_code_label.setObjectName("college_code_label")
        self.horizontalLayout.addWidget(self.college_code_label)
        spacerItem = QtWidgets.QSpacerItem(10, 5, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.college_to_delete_combobox = QtWidgets.QComboBox(parent=self.frame)
        self.college_to_delete_combobox.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.college_to_delete_combobox.setFont(font)
        self.college_to_delete_combobox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.college_to_delete_combobox.setEditable(True)
        self.college_to_delete_combobox.setObjectName("college_to_delete_combobox")
        self.college_to_delete_combobox.addItem("")
        self.horizontalLayout.addWidget(self.college_to_delete_combobox)
        self.verticalLayout.addWidget(self.frame)
        self.delete_college_button = QtWidgets.QPushButton(parent=Dialog)
        self.delete_college_button.setEnabled(False)
        self.delete_college_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.delete_college_button.setFont(font)
        self.delete_college_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_college_button.setObjectName("delete_college_button")
        self.verticalLayout.addWidget(self.delete_college_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Delete a college"))
        self.header_label.setText(_translate("Dialog", "Select a college to delete"))
        self.college_code_label.setText(_translate("Dialog", "College Code"))
        self.college_to_delete_combobox.setItemText(0, _translate("Dialog", "--Select College Code--"))
        self.delete_college_button.setText(_translate("Dialog", "Delete college"))
