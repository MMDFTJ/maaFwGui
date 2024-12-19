from PySide6.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QWidget
from qfluentwidgets import PushButton, CheckBox
from qfluentwidgets import FluentIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt-Fluent-Widgets Example")

        # 中央小部件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 布局
        self.layout = QVBoxLayout(self.central_widget)

        # 按钮
        self.add_button = PushButton("Add CheckBox", self)
        self.add_button.clicked.connect(self.add_checkbox)
        self.layout.addWidget(self.add_button)

    def add_checkbox(self):
        checkbox = CheckBox()
        self.layout.addWidget(checkbox)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyle("Fluent")  # 设置 Fluent 样式
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
