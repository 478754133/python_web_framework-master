from TestDatas.GobalDatas import gobal_datas as GD
from selenium import webdriver
from TestDatas.LoginDatas.login_datas import success_data as LD
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from Common.plugs.get_log import Log
from Common.plugs.get_config import r_config
import time
import Common.plugs.excel as excel
import constants as cs
import os,sys
import log
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(BASE_DIR)
if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')
log_dir = r_config(conf_dir, "log", "log_path")
logging = Log(log_dir)




module = '烟台'
filename = cs.FILE_NAME



def get_excel_sheet(path, module):
    """依据模块名获取sheet"""
    excel.open_excel(path)
    return excel.get_sheet(module)


class AutoPageCheck:


    def __init__(self):
        self.base_dir = os.path.dirname(__file__)
        self.conf_dir = ''
        if sys.platform == "win32":
            self.conf_dir = os.path.join(self.base_dir, 'sysinfo_url.xls').replace('/', '\\')
        else:
            self.conf_dir = os.path.join(self.base_dir, 'sysinfo_url.xls')
        print('配置文件路径:%s' % self.conf_dir)


    def loginCheck(self,username,password):

        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get(GD.web_login_url)
        vcode = str(input("请输入验证码:"))
        if username is not None:
            driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入用户名"]').send_keys(username)
        if password is not None:
            driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入密码"]').send_keys(password)
        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入验证码"]').send_keys(vcode)
        driver.find_element(By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--medium"]').click()
        print("登录成功！")
        return driver




    def run_test(self, driver,sheet):
        """执行测试用例"""
        rows = excel.get_rows(sheet)
        fail = 0
        for i in range(2, rows):
            #模块名称
            testName = excel.get_content(sheet, i, cs.CASE_NAME)
            #分页名称
            testPage = excel.get_content(sheet,i,cs.CASE_Page)
            #分页地址
            testUrl = excel.get_content(sheet, i, cs.CASE_URL)


            response = requests.get(testUrl)
            response.encoding = response.apparent_encoding
            result = response.text
            print(result)
            actualCode = str(response.status_code)

            expectCode = str(200)


            if actualCode != expectCode:
                logging.info("失败用例名称:{0}".format(testName))
                fail = fail + 1

            else:
                logging.info("模块名称:{0}".format(testName))
                logging.info("分页名称:{0}".format(testPage))
                logging.info("响应内容：{0}".format(result))
                logging.info("返回状态码：{0}".format(actualCode))
                logging.info("------------------")
        logging.info("失败次数:{0}".format(fail))



if __name__=='__main__':

    autopagecheck =AutoPageCheck()
    sheet = get_excel_sheet(filename, module)
    driver=autopagecheck.loginCheck(LD['username'], LD['password'])
    time.sleep(3)
    autopagecheck.run_test(driver,sheet)














