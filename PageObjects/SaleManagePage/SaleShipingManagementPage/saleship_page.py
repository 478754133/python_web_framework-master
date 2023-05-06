import time
from Common.plugs.basepage import BasePage
from Locators.IndexLocators.index_locators import IndexLocator
from Locators.SaleManageLocators.SaleShipManagementLocators.saleShipManagement_locators import SaleShipOrdersLocators as loc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class SaleShipPage(BasePage):

    # 进入发货管理界面
    def enterinterface(self):
        time.sleep(4)
        self.click_element(IndexLocator.salemanagement_tag, doc='销售管理')
        self.click_element(IndexLocator.saleshipmanagement_tag, doc='发货单管理')

    # 是否存在发货单打印按钮
    def isExist_outboundbtn(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.shiporder_print_loc))
            return True
        except:
            return False

    # 从第一个发货单进行出库单创建
    def saleoutbound(self):
        time.sleep(2)
        self.click_element(loc.icon_arrowdown_loc, doc='第一个下拉')
        self.click_element(loc.generateoutbound_loc, doc='点击出库')
        time.sleep(2)





