from Locators.SaleManageLocators.SaleOutboundOrdersLocators.saleOutbound_creat_locators import SaleOutboundCreatLocators as loc
from Common.plugs.basepage import BasePage
import time
from selenium.webdriver.common.keys import Keys
from PageObjects.SaleManagePage.SaleShipingManagementPage.saleship_page import SaleShipPage

class SaleOutboundCreatPage(BasePage):
    def __init__(self,driver):
        self.driver = driver

    def creatoutbound(self):
        SaleShipPage.enterinterface(self)
        SaleShipPage.saleoutbound(self)
        self.click_element(loc.radio_selected1_loc,doc='选择第一个圆点客户')
        self.input_element(loc.outquantity_loc,(Keys.CONTROL, 'a'),doc='选中出货数量')
        self.input_element(loc.outquantity_loc,"2",doc='填写出货数量')
        self.click_element(loc.submitbtn_loc,doc='提交')
        self.click_element(loc.promptinfo_confirm,doc='点击确定')



