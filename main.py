import resources
from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('notes.ui', self)  # Load the .ui file
        self.show()  # Show the GUI


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    windows = Ui()
    app.exec_()