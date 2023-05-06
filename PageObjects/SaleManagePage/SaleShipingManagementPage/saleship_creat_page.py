from Common.plugs.basepage import BasePage
import time
from PageObjects.SaleManagePage.SaleOrderManagementPage.saleorder_page import SaleOrderPage
from Locators.SaleManageLocators.SaleShipManagementLocators.saleShip_creat_locators import SaleShipCreatLocators as loc


class SaleShipCreatPage(BasePage):

    def __init__(self,driver):
        self.driver = driver

    #从销售订单创建发货通知
    def creatsaleship(self):
        SaleOrderPage.enterinterface(self)
        SaleOrderPage.generatesaleship(self)
        time.sleep(3)
        self.click_element(loc.transportmode_loc,doc='选择运输方式')
        self.click_element(loc.transportmode_1_loc,doc='汽车')
        self.input_element(loc.baseprice, "69000", doc='基价填写')
        time.sleep(1)
        self.input_element(loc.planshipquantity,"10",doc='发货数量')
        self.click_element(loc.savebtn_loc,doc='保存')