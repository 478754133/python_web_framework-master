from Locators.IndexLocators.index_locators import IndexLocator
from Common.plugs.basepage import BasePage
import time
from selenium.webdriver.common.keys import Keys
from PageObjects.SaleManagePage.SaleOrderManagementPage.saleorder_page import SaleOrderPage

class SaleSettleCreatPage(BasePage):
    def __init__(self,driver):
        self.driver = driver


    def creatsalesettle(self):

        ordernumber = SaleOrderPage.enterinterface(self)[0]
        customname = SaleOrderPage.enterinterface(self)[1]
        time.sleep(3)
        self.click_element(IndexLocator.salemanagement_tag,doc='选择销售管理')
        self.click_element(IndexLocator.salesettlemanage_loc, doc='选择结算管理')
        self.click_element(IndexLocator.salesettleadd_loc, doc='选择结算单新增')
        self.click_element(IndexLocator.salesettleadd_2_loc, doc='选择无点价结算新增')
        print(ordernumber,customname)

