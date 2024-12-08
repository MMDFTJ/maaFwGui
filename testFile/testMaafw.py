import asyncio

from utils.maafw import maafw


class TestMaaFw:
    def __init__(self):
        self.data = None

    async def start_maafw(self):
        self.data = await maafw.find_adb_devices()


    async def connect(self):
        await maafw.connect_adb(path=self.data[0].adb_path, address=self.data[0].address, config=self.data[0].config)

    async def click(self):
        await maafw.click(100, 100)


t = TestMaaFw()
asyncio.run(t.start_maafw())
asyncio.run(t.connect())
asyncio.run(t.click())
