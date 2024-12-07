import asyncio

from utils.maafw import maafw


class TestMaaFw:
    async def start_maafw(self):
        print(await maafw.find_adb_devices())



t = TestMaaFw()
asyncio.run(t.start_maafw())
