# Form implementation generated from reading ui file 'colleges_page.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 580)
        MainWindow.setMinimumSize(QtCore.QSize(720, 580))
        MainWindow.setMaximumSize(QtCore.QSize(720, 580))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.search_type_combobox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.search_type_combobox.setMinimumSize(QtCore.QSize(170, 25))
        self.search_type_combobox.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.search_type_combobox.setFont(font)
        self.search_type_combobox.setObjectName("search_type_combobox")
        self.search_type_combobox.addItem("")
        self.search_type_combobox.addItem("")
        self.gridLayout.addWidget(self.search_type_combobox, 1, 4, 1, 2)
        self.back_to_main_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_to_main_button.setMinimumSize(QtCore.QSize(170, 30))
        self.back_to_main_button.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back_to_main_button.setFont(font)
        self.back_to_main_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back_to_main_button.setObjectName("back_to_main_button")
        self.gridLayout.addWidget(self.back_to_main_button, 1, 0, 1, 2)
        self.search_input_lineedit = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_input_lineedit.sizePolicy().hasHeightForWidth())
        self.search_input_lineedit.setSizePolicy(sizePolicy)
        self.search_input_lineedit.setMinimumSize(QtCore.QSize(170, 25))
        self.search_input_lineedit.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.search_input_lineedit.setFont(font)
        self.search_input_lineedit.setText("")
        self.search_input_lineedit.setObjectName("search_input_lineedit")
        self.gridLayout.addWidget(self.search_input_lineedit, 1, 6, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem, 9, 6, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 6, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem2, 3, 7, 1, 1)
        self.edit_college_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.edit_college_button.setMinimumSize(QtCore.QSize(170, 30))
        self.edit_college_button.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.edit_college_button.setFont(font)
        self.edit_college_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.edit_college_button.setObjectName("edit_college_button")
        self.gridLayout.addWidget(self.edit_college_button, 6, 4, 1, 2)
        self.save_changes_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.save_changes_button.setMinimumSize(QtCore.QSize(170, 30))
        self.save_changes_button.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.save_changes_button.setFont(font)
        self.save_changes_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.save_changes_button.setObjectName("save_changes_button")
        self.gridLayout.addWidget(self.save_changes_button, 7, 4, 1, 2)
        self.add_college_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_college_button.setMinimumSize(QtCore.QSize(0, 30))
        self.add_college_button.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.add_college_button.setFont(font)
        self.add_college_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_college_button.setObjectName("add_college_button")
        self.gridLayout.addWidget(self.add_college_button, 6, 2, 1, 2)
        self.search_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.search_label.setMinimumSize(QtCore.QSize(170, 0))
        self.search_label.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.search_label.setFont(font)
        self.search_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.search_label.setObjectName("search_label")
        self.gridLayout.addWidget(self.search_label, 1, 2, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(170, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 2)
        self.delete_college_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delete_college_button.setMinimumSize(QtCore.QSize(170, 30))
        self.delete_college_button.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.delete_college_button.setFont(font)
        self.delete_college_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_college_button.setObjectName("delete_college_button")
        self.gridLayout.addWidget(self.delete_college_button, 7, 2, 1, 2)
        self.colleges_table_view = QtWidgets.QTableView(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.colleges_table_view.setFont(font)
        self.colleges_table_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.colleges_table_view.setObjectName("colleges_table_view")
        self.colleges_table_view.horizontalHeader().setMinimumSectionSize(100)
        self.colleges_table_view.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.colleges_table_view, 4, 0, 1, 8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sequence | College"))
        self.search_type_combobox.setItemText(0, _translate("MainWindow", "College Code"))
        self.search_type_combobox.setItemText(1, _translate("MainWindow", "College Name"))
        self.back_to_main_button.setText(_translate("MainWindow", "Go back to main screen"))
        self.search_input_lineedit.setPlaceholderText(_translate("MainWindow", "Input College Code"))
        self.edit_college_button.setText(_translate("MainWindow", "Edit college"))
        self.save_changes_button.setText(_translate("MainWindow", "Save changes to .csv"))
        self.add_college_button.setText(_translate("MainWindow", "Add college"))
        self.search_label.setText(_translate("MainWindow", "Search by"))
        self.delete_college_button.setText(_translate("MainWindow", "Delete college"))
