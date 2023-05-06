import time
from Common.plugs.basepage import BasePage
from Locators.IndexLocators.index_locators import IndexLocator
from Locators.SaleManageLocators.SaleOutboundOrdersLocators.saleOutboundOrders_locators import SaleOutboundOrdersLocators as loc
from Locators.SaleManageLocators.SaleShipManagementLocators.saleShipManagement_locators import SaleShipOrdersLocators
from selenium.webdriver.support import expected_conditions as EC
class SaleOutboundPage(BasePage):

    #进入出库单界面
    def enterinterface(self):
        time.sleep(3)
        self.click_element(IndexLocator.salemanagement_tag, doc='销售管理')
        self.click_element(IndexLocator.saleoutboundmanagement_tag, doc='出库单管理')
        self.click_element(IndexLocator.saleoutbound_tag, doc='出库单')
        time.sleep(2)



