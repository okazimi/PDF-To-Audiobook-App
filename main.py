# IMPORT SYS
import sys
# IMPORT PYSIDE6 FOR GUI
from PySide6 import QtWidgets
# IMPORT CREATED WIDGET CLASS
from MyWidget import MyWidget

# MAIN THREAD
if __name__ == '__main__':

    # INITIALIZE APP
    app = QtWidgets.QApplication([])

    # INITIALIZE WIDGET
    widget = MyWidget()
    # WIDGET SIZE
    widget.resize(400, 200)
    # SHOW WIDGET
    widget.show()

    # SHOW WIDGET UNTIL WINDOW CLOSED
    sys.exit(app.exec())



