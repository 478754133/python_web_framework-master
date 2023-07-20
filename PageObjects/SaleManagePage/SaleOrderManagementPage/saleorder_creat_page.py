from Locators.SaleManageLocators.SaleOrderManagementLocators.saleOrder_creat_locators import SaleOrderCreatLocators as loc
from Common.plugs.basepage import BasePage
import time
from selenium.webdriver.common.keys import Keys
from PageObjects.SaleContractManagementPage.salecontract_page import SaleConstractPage


class SaleOrderCreatPage(BasePage):

    def __init__(self,driver):
        self.driver = driver

    #从销售合同创建一个订单
    def creatsaleorder_1(self):
        SaleConstractPage.enterinterface(self)
        SaleConstractPage.generatesaleorder(self)
        time.sleep(2)
        self.input_element(loc.ordermonth_stat_loc,"2023-01",doc='订单月份开始日期')
        self.input_element(loc.ordermonth_stat_loc, Keys.ENTER, doc='订单月份开始日期确认')
        self.input_element(loc.ordermonth_end_loc, "2023-12",doc='订单月份结束日期')
        self.input_element(loc.ordermonth_end_loc, Keys.ENTER, doc='订单月份结束日期确认')
        self.input_element(loc.faildate_loc,"2023-12-30",doc='订单失效日期')
        self.input_element(loc.faildate_loc,Keys.ENTER, doc='订单失效日期确认')
        self.input_element(loc.deliverytolerance_loc,(Keys.CONTROL, 'a'), doc='交货允差')
        self.input_element(loc.deliverytolerance_loc,"0", doc='交货允差')
        # self.click_element(loc.createdepartment_loc, doc='创建部门选择')
        # self.click_element(loc.createdepartment_1_loc, doc='铜产品事业部')
        self.input_element(loc.quantity_loc, (Keys.CONTROL, 'a'), doc='数量20')
        self.input_element(loc.quantity_loc,"100",doc='数量100')
        # time.sleep(1)
        # self.click_element(loc.addmeterialinfo_loc, doc='新增产品信息')
        # self.click_element(loc.materialcode_loc, doc='物料选择')
        # self.click_element(loc.materialcode_table_loc, doc='物料选择阴极铜')
        # self.input_element(loc.materialcodesearch_loc, "402003165", doc='输入编码')
        # self.click_element(loc.materialcodesearchbtn_loc, doc='点击查询')
        # self.click_element(loc.materialcodesearchselected_loc, doc='圆点选择')
        # self.click_element(loc.materialcodesearchbtn_confirm_loc, doc='选择确定')
        # self.input_element(loc.quantity_loc, "100", doc='物料数量填写100')

    #保存销售订单
    def savesaleorder_1(self):
        self.creatsaleorder_1()
        self.click_element(loc.savebtn_loc, doc='保存')

    #提交审批销售订单
    def submitsaleorder_1(self):
        self.creatsaleorder_1()
        self.click_element(loc.submitbtn_loc,doc='提交')
        time.sleep(5)
        self.click_element(loc.auditinfo_submit_loc,doc='审批提交')








