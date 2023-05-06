import pandas as pd
import os
import sys

class GetAuditInfo:

    def __init__(self):
        self.base_dir = os.path.dirname(__file__)
        self.conf_dir = ''
        if sys.platform == "win32":
            self.conf_dir = os.path.join(self.base_dir, 'config.xlsx').replace('/', '\\')
        else:
            self.conf_dir = os.path.join(self.base_dir, 'config.xlsx')
        print('配置文件路径:%s' % self.conf_dir)

    def getSaleAudit(self):
        # usercols:应用sheet的第1，2，3列数据
        # nrows:应用sheet的第n行数据
        list = pd.read_excel(self.conf_dir, dtype="string", usecols=[0, 1, 2], nrows=3).values.tolist()
        return list

    def getLogin(self):
        # 应用sheet的第1，2，3列数据
        list = pd.read_excel(self.conf_dir, dtype="string", usecols=[0, 1, 2]).values.tolist()
        return list