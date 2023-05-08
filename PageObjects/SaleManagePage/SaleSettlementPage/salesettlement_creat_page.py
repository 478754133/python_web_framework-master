from Locators.IndexLocators.index_locators import IndexLocator
from Locators.SaleManageLocators.SaleSettleLocators.saleNopointSettle_locators import SaleNopointSettleLocators as loc
from Common.plugs.basepage import BasePage
import time
from selenium.webdriver.common.by import By
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
        time.sleep(2)
        self.input_element(loc.customname_loc,customname,doc='选择公司')
        time.sleep(1)
        self.click_element((By.XPATH, "//ul/li/span[text()='{0}']".format(customname)),doc='选择确认')
        time.sleep(1)
        self.click_element(loc.saleordernumber_loc,doc='点击销售订单')
        self.input_element(loc.saleordernumberfind_4_loc,ordernumber,doc='输入订单号')
        self.click_element(loc.searchbtn_loc,doc='点击查询')
        self.click_element(loc.selectedfind_1_loc,doc='选择第一个')
        self.click_element(loc.confirmbtn_loc,doc='点击确认')
        self.click_element(loc.creatdepartment_loc,doc='创建人部门')
        self.click_element(loc.creatdepartment_selected_loc,doc='选择第一个')


    def savesalesettle(self):
        self.creatsalesettle()
        time.sleep(1)
        self.click_element(loc.savebtn_loc,doc='保存')
        time.sleep(1)
        self.click_element(loc.promptinfo_confirm,doc='确认')



