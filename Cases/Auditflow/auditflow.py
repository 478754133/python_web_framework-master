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
from PIL import Image
import pytesseract
import cv2
from aip import AipOcr
import requests
import base64
import urllib
import json


""" 你的 APPID AK SK """
APP_ID = '117032645'
API_KEY = 'c3zyXbbtrvh2rWX1Ef4DMTg6'
SECRET_KEY = 'g83CsuPwchhvBYBdOYlTjTEmJ0y5v99L'


def ocrcode(src_url):
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting?access_token=" + get_access_token()

    # image 可以通过 get_file_content_as_base64("C:\fakepath\code.png",True) 方法获取
    #payload= "image=" + get_file_content_as_base64(imagepath, True)
    payload = "image=" + src_url + '&detect_direction=false&probability=false&detect_alteration=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload.encode("utf-8"))
        response.raise_for_status()  # 检查HTTP响应状态码

        response_json = response.json()  # 解析JSON响应
        words = response_json['words_result'][0]['words']
        return words

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except json.JSONDecodeError as json_err:
        print(f"JSON decode error: {json_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))







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
        options.binary_location = "D:\\chrome-win64\\chrome.exe"  # 指定chrome位置
        #os.environ["webdriver.chrome.driver"] = "D:\\tools\\chromedriver.exe"  # 指定chromedriver驱动位置
        options.add_argument("disable-cache")  # 禁用缓存
        options.add_experimental_option("excludeSwitches",['enable-automation', 'enable-logging'])  # 隐藏“正由自动化软件控制”提示，不打印driver日志
        options.add_experimental_option("useAutomationExtension", False)  # 隐藏“正由自动化软件控制”提示

        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1200, 800)
        driver.implicitly_wait(10)

        # 循环登录，直到成功
        while True:
            driver.get(test_url)
            code_element= driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/form/div[3]/div[2]/img')
            img_src = code_element.get_attribute('src')
            # 找到 "base64," 的位置
            base64_index = img_src.find("base64,") + len("base64,")
            # 提取 Base64 编码的部分
            base64_data = img_src[base64_index:]
            src_url = urllib.parse.quote_plus(base64_data)
            code = ocrcode(src_url)
            vcode = str(code)

            if username is not None:
                driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入用户名"]').send_keys(username)
            if password is not None:
                driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入密码"]').send_keys(password)
            driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入验证码"]').send_keys(vcode)
            driver.find_element(By.CSS_SELECTOR,'button[class="el-button el-button--primary el-button--medium"]').click()

            if self.login_status_error(driver):
                print('验证码错误，请重新输入')
                driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入验证码"]').clear()
                continue
            else:
                print('登录成功')
                break
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
            if pd.isna(acountList[i][0]) or acountList[i][0] == '':
                print('用户名为空，退出循环')
                break
            username = acountList[i][1]
            password = acountList[i][2]

            self.loginCheck(username, password)
            time.sleep(1)


    #销售订单审批流
    def saleorderauditflow(self):
        acountList = list = pd.read_excel(self.conf_dir, dtype="string", usecols=[0, 1, 2], nrows=3).values.tolist()
        for i in range(len(acountList)):
            if pd.isna(username) or username == '':
                print('用户名为空，退出循环')
                break
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


    def isExist_submit_btn(self,driver):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(By.XPATH,'//span[text()="提交"]'))
            return True
        except:
            return False

    def login_status_error(self,driver):
        try:
            # 假设登录成功后会出现一个特定的元素
            success_element = driver.find_element(By.XPATH,'//p[text()="验证码错误，或已失效！"]')
            return True
        except:
            return False
        # try:
        #     WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(By.XPATH,'//p[text()="验证码错误，或已失效！"]'))
        #     return True
        # except:
        #     return False





if __name__=='__main__':
    # image_path = r'D:\code.png'
    # code=ocrcode(image_path)

    acountList=''
    select=int(input("选择功能:1.登录审批账号 2.审批流审批操作\n"))

    if select == 1:

        autoapprove = Auto_approve()
        autoapprove.autologin()


    elif select == 2:
        autoapprove =Auto_approve()
        autoapprove.saleorderauditflow()
    else:print("please input numbers!")
