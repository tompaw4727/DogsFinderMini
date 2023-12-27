from PySide6 import QtWidgets
import sys
from main_window import Main_window

app = QtWidgets.QApplication(sys.argv)

window = Main_window(app)
window.show()

app.exec()