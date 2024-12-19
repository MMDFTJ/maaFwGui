from qfluentwidgets import CheckBox

from untitled import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow

class MyWindow2(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.PushButton_3.clicked.connect(self.add_checkbox)

    def add_checkbox(self):
        checkbox = CheckBox()
        checkbox2 = CheckBox()
        # self.gridLayout_5.addWidget(checkbox)
        self.gridLayout_7.addWidget(checkbox)
        self.gridLayout_s.addWidget(checkbox2)
        # self.gridLayout_8.addWidget(checkbox)
if __name__ == '__main__':
    app = QApplication()
    window = MyWindow2()
    window.show()
    app.exec()