import pymysql

class MYsqlUtils:
    con = None
    cursor = None

    @classmethod
    def read(cls,host="localhost",user="root",database="学生数据库",password="",tablename="students"):
        cls.con = pymysql.connect(host=host,user=user,password=password,database=database,charset="utf8")
        cls.cursor = cls.con.cursor()
        sql= '''
            select * from {tablename}
        '''
        return cls.cursor.execute(sql.format(tablename=tablename))



u=MYsqlUtils.read()
print(u)
