from TestDatas.GobalDatas import gobal_datas as GD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from getconfig import GetAuditInfo
import os,sys

test_url= GD.web_login_url

#程序延时
timeout = 6

class Auto_approve:

    def __init__(self):
        self.base_dir = os.path.dirname(__file__)
        self.conf_dir = ''
        if sys.platform == "win32":
            self.conf_dir = os.path.join(self.base_dir, 'config.xlsx').replace('/', '\\')
        else:
            self.conf_dir = os.path.join(self.base_dir, 'config.xlsx')
        print('配置文件路径:%s' % self.conf_dir)


    def loginCheck(self,username,password):

        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1200, 800)
        driver.implicitly_wait(10)

        driver.get(test_url)
        if username is not None:
            driver.find_element(By.CSS_SELECTOR, 'input[placeholder="账号"]').send_keys(username)
        if password is not None:
            driver.find_element(By.CSS_SELECTOR, 'input[placeholder="密码"]').send_keys(password)
        driver.find_element(By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--medium"]').click()
        # nowhandle = self.driver.current_window_handle
        # print(nowhandle)
        print("登录成功！")
        return driver

    def audit(self,driver):
        nowhandle = driver.current_window_handle
        print(nowhandle)
        driver.switch_to.window(nowhandle)
        driver.find_element(By.CSS_SELECTOR,'.el-col:nth-child(1) .card-list:nth-child(1) > .content-title').click()
        time.sleep(timeout)
        submit_btn=driver.find_element(By.XPATH,'//span[text()="提交"]')
        #self.driver.find_element(By.CSS_SELECTOR,'.operate>button[class="el-button el-button--primary el-button--mini"]').click()
        ActionChains(driver).move_to_element(submit_btn).click().perform()
        time.sleep(1)
        if not self.isExist_submit_btn():
            print('审批完成')
        else:
            print('Fail for this')

    #登录所有账号
    def autologin(self):
        acountList = pd.read_excel(self.conf_dir, dtype="string", usecols=[0, 1, 2]).values.tolist()
        for i in range(len(acountList)):
            print('当前账户为：', acountList[i][0])
            username = acountList[i][1]
            password = acountList[i][2]
            self.loginCheck(username, password)
            time.sleep(1)


    #销售订单审批流
    def saleorderauditflow(self):
        acountList = list = pd.read_excel(self.conf_dir, dtype="string", usecols=[0, 1, 2], nrows=3).values.tolist()
        for i in range(len(acountList)):
            print('当前账户为：', acountList[i][0])
            username = acountList[i][1]
            password = acountList[i][2]
            self.audit(self.loginCheck(username, password))
            time.sleep(1)

    #销售发货审批流
    def saleshipauditflow(self):
        acountList = pd.read_excel(self.conf_dir, dtype="string", usecols=[0, 1, 2], nrows=3).values.tolist()
        for i in range(len(acountList)):
            print('当前账户为：', acountList[i][0])
            username = acountList[i][1]
            password = acountList[i][2]
            self.audit(self.loginCheck(username, password))
            time.sleep(1)


    def isExist_submit_btn(self):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(By.XPATH,'//span[text()="提交"]'))
            return True
        except:
            return False




if __name__=='__main__':
    acountList=''
    select=int(input("选择功能:1.登录审批账号 2.审批流审批操作\n"))
    if select == 1:
        autoapprove = Auto_approve()
        autoapprove.autologin()


    elif select == 2:
        autoapprove =Auto_approve()
        autoapprove.saleorderauditflow()
    else:print("please input numbers!")