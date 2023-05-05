import pymysql
import pytest

from utils.yaml_util import read_yaml


class MysqlUtil:
    sqlinfo = read_yaml('/common/mysql.yml')

    def __init__(self):
        self.host = MysqlUtil.sqlinfo['host']
        self.port = int(MysqlUtil.sqlinfo['port'])
        self.user = MysqlUtil.sqlinfo['user']
        self.password = MysqlUtil.sqlinfo['password']
        self.db = MysqlUtil.sqlinfo['db']

    def connect(self):
        # 1.建立连接：
        connect = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)
        return connect

    def create_cursor(self):
        # 2.创建游标：
        cursor = self.connect().cursor()
        return cursor

        # 3.执行SQL语句：

    def select_db_one(self, sql):
        cursor = self.create_cursor()
        connect = self.connect()
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            print("【%s】sql语句执行成功" % sql)
            print(result)
            return result
        except Exception as e:
            print("【%s】sql语句执行失败，请检查" % sql, "错误为【%s】" % e)
        cursor.close()
        connect.close()

    def select_db_all(self, sql):
        cursor = self.create_cursor()
        connect = self.connect()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            print("【%s】sql语句执行成功" % sql)
            print(result)
            return result
        except Exception as e:
            print("【%s】sql语句执行失败，请检查" % sql, "错误为【%s】" % e)
        cursor.close()
        connect.close()

    def delete_db(self, sql):
        cursor = self.create_cursor()
        connect = self.connect()
        try:
            cursor.execute(sql)
            connect.commit()
            result = cursor.fetchall()
            print("【%s】sql语句执行成功" % sql)
            print(result)
            return result
        except Exception as e:
            print("【%s】sql语句执行失败，请检查" % sql, "错误为【%s】" % e)
        cursor.close()
        connect.close()


if __name__ == '__main__':
    MysqlUtil().select_db_one(
        sql='select count(*) from (select * from gu_user_account where value!=0 and name="money") as t')
