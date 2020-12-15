from utils.DBUtils import MYsqlUtils
from utils.ExcelUtils import ExcelUtils
import os
import pymysql


class DataRead:
    list = None
    def __init__(self,mode,filename="0",sheetname="0",user="",password="",tablename=""):
        if mode =="excel":
            if filename == "":
                raise Exception("文件名不能为空，别瞎弄")
            elif not os.path.isfile(filename):
                raise Exception("文件不存在，别瞎弄")
            else:
                DataRead.list= ExcelUtils.read(filename,sheetname)
        elif mode =="用户管理":
            DataRead.list = MYsqlUtils.read(host="host",database="database",user="user",password="",tablename=tablename)

        else:
             raise Exception("对不起，你的操作模式不对")
