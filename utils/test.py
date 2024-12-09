import asyncio
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Slot
from qasync import QEventLoop, asyncSlot


from instance.maafwInstance import maafw
from testingTime import TestingTime
testingTime = TestingTime()


class AsyncButtonApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = None
        self.setWindowTitle("Async Buttons Example")
        self.resize(400, 300)

        # 创建主布局
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # 按钮1
        self.button1 = QPushButton("Button 1")
        self.button1.clicked.connect(self.on_button1_click)
        layout.addWidget(self.button1)

        # 按钮2
        self.button2 = QPushButton("Button 2")
        self.button2.clicked.connect(self.on_button2_click)
        layout.addWidget(self.button2)

        # 按钮3
        self.button3 = QPushButton("Button 3")
        self.button3.clicked.connect(self.on_button3_click)
        layout.addWidget(self.button3)

        self.setCentralWidget(central_widget)

    @asyncSlot()
    async def on_button1_click(self):
        print("Button 1 clicked!")
        # await asyncio.sleep(1)  # 模拟异步操作
        self.data = await maafw.find_adb_devices()
        print(self.data)
        print("Button 1 async task complete.")

    @asyncSlot()
    async def on_button2_click(self):
        print("Button 2 clicked!")
        await maafw.connect_adb(path=self.data[0].adb_path, address=self.data[0].address,
                                     config=self.data[0].config)
        print("Button 2 async task complete.")

    @asyncSlot()
    async def on_button3_click(self):
        print("Button 3 clicked!")
        await maafw.click(100,100)
        await testingTime.test_click_time()
        print("Button 3 async task complete.")


if __name__ == "__main__":
    app = QApplication([])

    # 使用 qasync 的事件循环
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = AsyncButtonApp()
    window.show()

    with loop:
        loop.run_forever()
