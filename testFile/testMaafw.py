import asyncio

from instance.maafwInstance import maafw
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
        await maafw.load_resource("")
    async def click(self):
        await testingTime.run()
        await maafw.click(100, 100)


t = TestMaaFw()
asyncio.run(t.start_maafw())
asyncio.run(t.connect())
asyncio.run(t.click())
