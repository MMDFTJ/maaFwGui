import json
from public.maaConfig import maaConfig

path = r'F:\资料\python\Pycharm Project\pythonProject\maaFwGui\resource\interface3.json'

with open(path, encoding='utf-8') as file:
    data = json.load(file)

for key, value in data.items():
    print(f'{key} : {value}')
    if key == 'controller':
        maaConfig.interface_config[key] = value[0]
    if key == 'resource':
        for i in value:
            maaConfig.interface_config['resource'] = value

print('*'*10)
for x, y in maaConfig.interface_config.items():
    print(f'{x}:{y}')

