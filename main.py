from PyQt5 import QtCore, QtGui, QtWidgets, uic
import resources

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('texteditor.ui', self) # Load the .ui file
        self.actionSave.triggered.connect(self.save_as)
        self.actionSave_as.triggered.connect(self.save_as)
        self.actionOpen.triggered.connect(self.open)

    def open(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                            '', '')
        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.plainTextEdit.setPlainText(data)

    def save_as(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        f = open(fname[0], 'w')
        text = self.plainTextEdit.toPlainText()
        f.write(text)
        f.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
