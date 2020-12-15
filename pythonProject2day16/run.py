import unittest
import os
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()

loader = unittest.defaultTestLoader

cases = loader.discover(os.getcwd()+"\\TestCalc.py",pattern="*.py")
suite.addTest(cases)
with open("银行开户测试.html","w+",encoding="utf-8") as f:
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f,
        verbosity=1,
        title="银行开户测试",
        description="这是第三次迭代测试"
    )
    runner.run(suite)
