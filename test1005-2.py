from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from play1005 import Ui_Dialog

app = QApplication(sys.argv)
t = QTranslator()
t.load("chi.qm")
app.installTranslator(t)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)
widget.show()
app.exec_()