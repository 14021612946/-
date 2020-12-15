import unittest
from ddt import ddt
from ddt import unpack
from ddt import data
from entity import yinhang
from utils.DataRead import DataRead
from entity.yinhang import bank_addUser



data1 = DataRead("excel",filename="E:\\pythonProject1\\pythonProject2yinhang\\testcase\\yinhan.xlsx",sheetname="0").list
@ddt
class TestCalc(unittest.TestCase):
    @data(*data1)
    @unpack
    def testSaveUser(self,a,b,d,e,f,g,h,k):
        s =bank_addUser(username=a,password=b,country=d,province=e,street=f,door=g,money=h,)#实际
        self.assertEqual(s,k)
