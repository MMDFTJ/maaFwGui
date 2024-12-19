import asyncio

from instance.maafwInstance import maafw
from instance.maafwInstance import maa_config
from utils.testingTime import TestingTime

testingTime = TestingTime()


class TestMaaFw:
    def __init__(self):
        self.data = None

    async def start_maafw(self):
        self.data = await maafw.find_adb_devices()

    async def connect(self):
        await maafw.connect_adb(path=self.data[0].adb_path, address=self.data[0].address, config=self.data[0].config)

    async def load_file(self):

        print(await maafw.load_resource(r"F:\资料\python\Pycharm Project\pythonProject\maaFwGui\resource\base"))

    async def click(self):
        await testingTime.run()
        await maafw.click(100, 100)

    async def run_pip(self):
        print(await maafw.run_task('ActivityEntry',
                                   pipeline_override={
                                       "name": "活动：地球上最后的夜晚 20 艰难",
                                       "pipeline_override": {
                                           "ActivityEnterTheShow": {
                                               "template": "Combat/Activity/TheLastEveningOnEarthEnterTheShow.png"
                                           },
                                           "TargetStageName": {
                                               "expected": "20"
                                           },
                                           "StageDifficulty": {
                                               "next": "ActivityStageDifficulty"
                                           }
                                       }
                                   }, ))


t = TestMaaFw()
asyncio.run(t.start_maafw())
asyncio.run(t.connect())
asyncio.run(t.load_file())
# asyncio.run(t.click())
# asyncio.run(t.run_pip())
