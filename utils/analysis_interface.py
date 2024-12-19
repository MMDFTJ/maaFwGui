"""
用来解析interface文件
"""
import json
from instance.maafwInstance import maa_config


class AnalysisInterface:
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        单例中的__new__优点
        控制实例化：可以拦截并控制对象创建过程。
        高效性：无需重复初始化实例，减少资源浪费。
        安全性：确保系统中只有一个全局实例，避免状态不一致问题。
        """
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.interface_data = None

    def load_interface(self, interface_path=r'F:\资料\python\Pycharm Project\pythonProject\maaFwGui\interface.json'):
        """
        加载interface文件
        """
        try:
            with open(interface_path, encoding='utf-8') as file:
                self.interface_data = json.load(file)
                print(self.interface_data)
        except FileNotFoundError:
            print(f'找不到interface_path文件，检查路径是否正确。当前路径{interface_path}')
        except json.JSONDecodeError:
            print('这不是个json文件')

    def get_interface_attribute(self, attribute_name):
        """
        获取interface的属性（attribute）并赋值给maaConfig
        """

        if hasattr(maa_config, f'interface_config_{attribute_name}'):
            setattr(maa_config, f"interface_config_{attribute_name}", self.interface_data[attribute_name])

        return self.interface_data[attribute_name]

    def get_interface_controller(self):

        return self.get_interface_attribute('controller')

    def get_interface_resource(self):

        return self.get_interface_attribute('resource')

    def get_interface_task(self):
        """
        获取task任务
        """
        return self.get_interface_attribute('task')

    def get_interface_option(self):
        """
        获取option任务
        """
        return self.get_interface_attribute('option')

    def start_analysis_interface(self):
        self.get_interface_controller()
        self.get_interface_resource()
        self.get_interface_task()
        self.get_interface_option()


if __name__ == '__main__':
    analysisInterface = AnalysisInterface()
    analysisInterface.load_interface()
    print(analysisInterface.get_interface_controller())
    print(analysisInterface.get_interface_resource())
    print(analysisInterface.get_interface_task())
    print(analysisInterface.get_interface_option())
