import time

from Locators.PurchaseContractionManagementLocators.purchaseContractManagement_locators import PurchaseContractManagementLocators as loc
from Common.plugs.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from Locators.PurchaseContractionManagementLocators.purchaseContractManagement_locators import PurchaseContractManagementLocators
from selenium.webdriver.support.wait import WebDriverWait
from Locators.IndexLocators.index_locators import IndexLocator
class purchaseConstractPage(BasePage):

    #进入采购合同管理界面
    def enterinterface(self):
        time.sleep(3)
        self.get("http://yantaitrade.jxcc.com/contract/contract-manange/purchase-list")


    #新建采购哦合同
    def creatpurchaseconstract(self):
        doc='点击新建销售合同按钮'
        self.click_element(loc.newbuilt_loc,doc)
    #
    #
    #
    # #批量删除销售合同
    # def deleteconstract(self):
    #     self.click_element(loc.list_checkbox_loc_1,doc='选择第一个复选框')
    #     self.click_element(loc.batchdeletebtn_loc,doc='点击批量删除')
    #     self.click_element(loc.promptdelete_loc,doc='确认删除')
    #
    # #批量作废销售合同
    # def cancelconstract(self):
    #     time.sleep(4)
    #     self.click_element(loc.list_checkbox_loc_1, doc='选择第一个复选框')
    #     self.click_element(loc.batchcancelbtn_loc,doc='点击作废')
    #     self.input_element(loc.prompcancelinfotext_loc,"测试作废",doc='填写作废信息')
    #     self.click_element(loc.prompcancelconfirm_loc,doc='作废确认')
    #
    # #从第一个销售合同生成销售订单
    # def generatepurchaseorder(self):
    #     time.sleep(3)
    #     self.click_element(loc.list_checkbox_loc_1, doc='选择第一个复选框')
    #     self.click_element(loc.icon_arrowdown_loc,doc='第一个下拉选择')
    #     self.click_element(loc.generatepurchaseorder_loc,doc='点击创建订单')