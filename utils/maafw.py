"""
这里是maaFw扫描、连接、加载resource、run_task、stop_task等
"""
import time
import os
from typing import List, Optional
from asyncify import asyncify
from PIL import Image
# python -m pip install maafw
# from maa.define import RectType
from pathlib import Path
from maa.resource import Resource
from maa.controller import AdbController, Win32Controller
from maa.tasker import Tasker
from maa.toolkit import Toolkit, AdbDevice
from maa.notification_handler import NotificationHandler, NotificationType
from maa.custom_action import CustomAction


class MaaFw:
    notification_handler: Optional[NotificationHandler]
    tasker: Tasker | None
    controller: AdbController | Win32Controller | None

    def __init__(self):
        Toolkit.init_option('./')
        Tasker.set_debug_mode(True)

        self.controller = None
        self.resource = None
        self.tasker = None

    @staticmethod
    @asyncify
    def find_adb_devices() -> List[AdbDevice]:
        """
        搜索adb连接
        :return:
        """
        return Toolkit.find_adb_devices()

    @asyncify
    def connect_adb(self, path: Path, address: str, config: dict):
        """
        用于连接adb端口
        :return:
        """
        self.controller = AdbController(path, address, config=config)
        connected = self.controller.post_connection().wait().succeeded()
        if not connected:
            print(f"Failed to connect {path} {address}")
            return False

        return True

    @asyncify
    def load_resource(self, dir: Path):
        """
        加载resource文件
        :return:
        """
        if not self.resource:
            self.resource = Resource()

        return self.resource.clear() and self.resource.post_path(dir).wait().succeeded()

    @asyncify
    def run_task(self, entry: str, pipeline_override: dict = {}):
        """
        执行run_task任务
        :return:
        """
        if not self.tasker:
            self.tasker = Tasker(notification_handler=self.notification_handler)

        if not self.resource or not self.controller:
            print("Resource or Controller not initialized")
            return False

        self.tasker.bind(self.resource, self.controller)
        if not self.tasker.inited:
            print("Failed to init MaaFramework instance")
            return False

        return self.tasker.post_pipeline(entry, pipeline_override).wait().succeeded()

    @asyncify
    def stop_task(self):
        """
        停止run_task
        :return:
        """
        if not self.tasker:
            return

        self.tasker.post_stop().wait()

    @asyncify
    def screen_cap(self, capture: bool = True) -> Optional[Image.Image]:
        if not self.controller:
            return None

        if capture:
            self.controller.post_screencap().wait()
        im = self.controller.cached_image
        if im is None:
            return None

        # return cvmat_to_image(im)

    @asyncify
    def click(self, x, y) -> bool:
        if not self.controller:
            return False

        return self.controller.post_click(x, y).wait().succeeded()

    def register_recognition(self):
        """
        注册
        :return:
        """
        pass

    def register_action(self):
        """
        注册
        :return:
        """
        pass


maafw = MaaFw()