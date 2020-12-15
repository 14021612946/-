import unittest
import ddt
from ddt import unpack
from ddt import data
from entity.Calc import Calc
from utils.DataRead import DataRead



data1 = DataRead("database",user="user",password="",tablename="students")
@ddt
class TestCalc(unittest.TestCase):
    data(*data1)
    @ddt.unpack
    def testAdd(self,a,b,c):
        ca = Calc()
        s = ca.add(a,b)
        self.assertEqual(s,c)


