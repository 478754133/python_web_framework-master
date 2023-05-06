from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.IndexLocators.index_locators import IndexLocator as loc
from Locators.SaleConstractionManagementLocators.saleContractManagement_locators import SaleContractManagementLocators
from Locators.SaleConstractionManagementLocators.saleConstract_creat_locators import SaleContractCreatLocators


class IndexPage:

    def __init__(self, driver):
        self.driver = driver

    # 判断当前首页元素是否存在 存在返回True 否则返回false
    def isExist_homepage_tag(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.homepage_tag))
            return True
        except:
            return False

    #判断操作成功是否存在 存在返回True 否则返回false
    def isExist_operatesucess_prompt(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.sucessoperate_prompt))
            return True
        except:
            return False

    #判断删除成功是否存在 存在返回True 否则返回false
    def isExist_deletesucess_prompt(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.sucessdelete_prompt))
            return True
        except:
            return False

    # 判断作废成功是否存在 存在返回True 否则返回false
    def isExist_cancelsucess_prompt(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.sucesscancel_prompt))
            return True
        except:
            return False












