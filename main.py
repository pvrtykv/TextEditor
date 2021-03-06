from PyQt5 import QtCore, QtGui, QtWidgets, uic
import resources
import pathlib


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('texteditor.ui', self) # Load the .ui file

        self.path = ""
        self.changed = False

        self.actionSave.triggered.connect(self.save_as)
        self.actionSave_as.triggered.connect(self.save_as)
        self.actionOpen.triggered.connect(self.open)
        self.actionCopy.triggered.connect(self.editor.copy)
        self.actionCut.triggered.connect(self.editor.cut)
        self.actionPaste.triggered.connect(self.editor.paste)
        self.actionUndo.triggered.connect(self.editor.undo)
        self.actionRedo.triggered.connect(self.editor.redo)
        self.editor.textChanged.connect(self.on_text_changed)

    def on_text_changed(self):
        self.changed = True
        self.update_title()

    def update_title(self):
        title = "TextEditor"
        if self.path != "":
            title += " - " + pathlib.Path(self.path).name
        if self.changed:
            title += "*"
        self.setWindowTitle(title)

    def open(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                            '', '')
        if fname[0]:
            self.path = fname[0]
            f = open(fname[0], 'r')
            data = f.read()
            self.editor.setPlainText(data)
            f.close()
            self.changed = False
            self.update_title()

    def save_as(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        if fname[0] != "":
            self.path = fname[0]
            f = open(fname[0], 'w')
            text = self.editor.toPlainText()
            f.write(text)
            f.close()
            self.changed = False
            self.update_title()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
