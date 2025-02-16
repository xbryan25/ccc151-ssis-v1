from PyQt6.QtWidgets import QItemDelegate, QComboBox
from PyQt6.QtCore import Qt

# https://stackoverflow.com/questions/51945016/pyqt-qcombobox-in-qtableview

class ComboboxItemDelegate(QItemDelegate):

    def __init__(self, parent, items):
        self.items = items
        QItemDelegate.__init__(self, parent)

    # def edit_editor_choices(self):
    #     combobox = QComboBox(self.parent)
    #     choices = []
    #     for item in self.items:
    #         choices.append(item)
    #
    #     combobox.addItems(choices)
    #     combobox.currentIndexChanged.connect(self.change_combobox_value)

    def createEditor(self, parent, option, index):
        combobox = QComboBox(parent)
        choices = []
        for item in self.items:
            choices.append(item)

        combobox.addItems(choices)
        combobox.currentIndexChanged.connect(self.change_combobox_value)
        return combobox

    def setEditorData(self, editor, index):
        editor.blockSignals(True)

        text = index.model().data(index, Qt.ItemDataRole.DisplayRole)

        try:
            i = self.items.index(text)
        except ValueError:
            i = 0

        editor.setCurrentIndex(i)
        editor.blockSignals(False)

    def setModelData(self, editor, model, index):
        if model.data(index) != editor.currentText():
            model.setData(index, editor.currentText())

    def change_combobox_value(self):
        self.commitData.emit(self.sender())


