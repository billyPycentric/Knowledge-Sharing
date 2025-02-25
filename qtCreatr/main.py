from PySide6.QtWidgets import QApplication
from guessingGame import RocWidget
import sys

app = QApplication(sys.argv)

window = RocWidget()
window.show()

app.exec()
