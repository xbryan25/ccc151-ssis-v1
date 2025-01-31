# Form implementation generated from reading ui file 'students_page.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 580)
        MainWindow.setMinimumSize(QtCore.QSize(880, 580))
        MainWindow.setMaximumSize(QtCore.QSize(880, 1000))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.delete_student_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delete_student_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.delete_student_button.setFont(font)
        self.delete_student_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_student_button.setObjectName("delete_student_button")
        self.gridLayout.addWidget(self.delete_student_button, 6, 2, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem2, 7, 5, 1, 1)
        self.edit_student_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.edit_student_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.edit_student_button.setFont(font)
        self.edit_student_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.edit_student_button.setObjectName("edit_student_button")
        self.gridLayout.addWidget(self.edit_student_button, 5, 3, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem3, 2, 4, 1, 1)
        self.add_student_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_student_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.add_student_button.setFont(font)
        self.add_student_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_student_button.setObjectName("add_student_button")
        self.gridLayout.addWidget(self.add_student_button, 5, 1, 1, 2)
        self.back_to_main_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_to_main_button.setMinimumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back_to_main_button.setFont(font)
        self.back_to_main_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back_to_main_button.setObjectName("back_to_main_button")
        self.gridLayout.addWidget(self.back_to_main_button, 1, 0, 1, 1)
        self.students_table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.students_table.setMaximumSize(QtCore.QSize(870, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.students_table.setFont(font)
        self.students_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.students_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.students_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.students_table.setObjectName("students_table")
        self.students_table.setColumnCount(7)
        self.students_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.students_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.students_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.students_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.students_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.students_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.students_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.students_table.setHorizontalHeaderItem(6, item)
        self.students_table.horizontalHeader().setVisible(True)
        self.students_table.horizontalHeader().setDefaultSectionSize(140)
        self.students_table.horizontalHeader().setMinimumSectionSize(90)
        self.students_table.horizontalHeader().setSortIndicatorShown(True)
        self.students_table.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.students_table, 3, 0, 1, 6)
        self.serach_label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.serach_label.setFont(font)
        self.serach_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.serach_label.setObjectName("serach_label")
        self.gridLayout.addWidget(self.serach_label, 1, 2, 1, 1)
        self.search_type_combobox = QtWidgets.QComboBox(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.search_type_combobox.setFont(font)
        self.search_type_combobox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.search_type_combobox.setEditable(False)
        self.search_type_combobox.setObjectName("search_type_combobox")
        self.search_type_combobox.addItem("")
        self.search_type_combobox.addItem("")
        self.search_type_combobox.addItem("")
        self.search_type_combobox.addItem("")
        self.search_type_combobox.addItem("")
        self.search_type_combobox.addItem("")
        self.gridLayout.addWidget(self.search_type_combobox, 1, 3, 1, 1)
        self.search_input_lineedit = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_input_lineedit.sizePolicy().hasHeightForWidth())
        self.search_input_lineedit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.search_input_lineedit.setFont(font)
        self.search_input_lineedit.setObjectName("search_input_lineedit")
        self.gridLayout.addWidget(self.search_input_lineedit, 1, 4, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.search_type_combobox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.delete_student_button.setText(_translate("MainWindow", "Delete student"))
        self.edit_student_button.setText(_translate("MainWindow", "Edit student"))
        self.add_student_button.setText(_translate("MainWindow", "Add student"))
        self.back_to_main_button.setText(_translate("MainWindow", "Go back to main screen"))
        item = self.students_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Order ID"))
        item = self.students_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID Number"))
        item = self.students_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.students_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.students_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Year Level"))
        item = self.students_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.students_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Program Code"))
        self.serach_label.setText(_translate("MainWindow", "Search by"))
        self.search_type_combobox.setItemText(0, _translate("MainWindow", "ID Number"))
        self.search_type_combobox.setItemText(1, _translate("MainWindow", "First Name"))
        self.search_type_combobox.setItemText(2, _translate("MainWindow", "Last Name"))
        self.search_type_combobox.setItemText(3, _translate("MainWindow", "Year Level"))
        self.search_type_combobox.setItemText(4, _translate("MainWindow", "Gender"))
        self.search_type_combobox.setItemText(5, _translate("MainWindow", "Program Code"))
        self.search_input_lineedit.setPlaceholderText(_translate("MainWindow", "Input ___"))
