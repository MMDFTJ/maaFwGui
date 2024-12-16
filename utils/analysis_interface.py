"""
用来解析interface文件
"""
import json
from public.maaConfig import maaConfig


class AnalysisInterface:

    def __init__(self,
                 interface_path=r'F:\资料\python\Pycharm Project\pythonProject\maaFwGui\resource\interface3.json'):
        self.interface_data = None
        self.interface_path = interface_path

    def load_interface(self):
        """
        加载interface文件
        """
        with open(self.interface_path, encoding='utf-8') as file:
            self.interface_data = json.load(file)
            print(self.interface_data)

    def get_interface_controller(self):
        return self.interface_data['controller']

    def get_interface_resource(self):
        return self.interface_data['resource']

    def get_interface_task(self):
        """
        获取task任务
        """
        return self.interface_data['task']

    def get_interface_option(self):
        """
        获取option任务
        """
        pass


analysisInterface = AnalysisInterface()
analysisInterface.load_interface()
analysisInterface.get_interface_controller()
# maaConfig.interface_config = data

# for key, value in data.items():
#     print(f'{key} : {value}')
#     if key == 'controller':
#         maaConfig.interface_config[key] = value[0]
#     if key == 'resource':
#         for i in value:
#             maaConfig.interface_config['resource'] = value
#
# print('*'*10)
# for x, y in maaConfig.interface_config.items():
#     print(f'{x}:{y}')
