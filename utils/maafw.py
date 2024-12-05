"""
这里是maaFw扫描、连接、加载resource、run_task、stop_task等
"""
import time
import os
from typing import List
from asyncify import asyncify
# python -m pip install maafw
# from maa.define import RectType
from pathlib import Path
from maa.resource import Resource
from maa.controller import AdbController
from maa.tasker import Tasker
from maa.toolkit import Toolkit, AdbDevice
from maa.notification_handler import NotificationHandler, NotificationType

from maa.custom_action import CustomAction


class MaaFw:
    def __init__(self):
        Toolkit.init_option('./')
        self.controller = None

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
    def load_resource(self):
        """
        加载resource文件
        :return:
        """

    @asyncify
    def run_task(self):
        """
        执行run_task任务
        :return:
        """

    @asyncify
    def stop_task(self):
        """
        停止run_task
        :return:
        """

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
print(maafw.find_adb_devices())
