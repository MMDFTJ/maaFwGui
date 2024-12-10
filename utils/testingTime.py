"""
用来测试截图时间，点击时间
"""
import asyncio
import time
import numpy as np
from instance.maafwInstance import maafw


class TestingTime:
    """
    点击15次判断点击误差值
    click可以参考alas的点击延迟adb.py
    """
    TEST_TOTAL = 15
    TEST_BEST = int(TEST_TOTAL * 0.8)

    async def test_click_time(self):
        record = []

        for i in range(1, self.TEST_TOTAL + 1):
            start_time = time.time()
            await maafw.click(100, 100)
            cost = time.time() - start_time
            record.append(cost)
        average = float(np.mean(np.sort(record)[:self.TEST_BEST]))
        return average

    @staticmethod
    def evaluate_click(cost):
        """
        区分点击状态
        :param cost:
        :return:
        """
        if not isinstance(cost, (float, int)):
            return None

        if cost < 0.100:
            return 'Fast'
        if cost < 0.200:
            return 'Medium'
        if cost < 0.400:
            return 'Slow'
        return 'Very Slow'

    @staticmethod
    def show(data, evaluate_func):
        print(evaluate_func(data))

    async def run(self):
        data = await self.test_click_time()
        self.show(data, self.evaluate_click)



