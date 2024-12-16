"""
用来解析pipeline文件
"""
import json
from public.maaConfig import maaConfig


class AnalysisPipline:

    def __init__(self,
                 pipline_path=r'F:\资料\python\Pycharm Project\pythonProject\maaFwGui\resource\interface3.json'):
        self.pipline = None
        self.interface_path = pipline_path

    def load_interface(self):
        """
        加载pipline文件
        """
        pass

    def get_pipline_task(self):
        """
        获取task任务
        """
        pass
