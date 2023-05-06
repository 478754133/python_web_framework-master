import time
from Common.plugs.basepage import BasePage
from Locators.IndexLocators.index_locators import IndexLocator
from Locators.SaleManageLocators.SaleOrderManagementLocators.saleOrderManagement_locators import SaleOrderManagementLocators as loc
from Locators.SaleManageLocators.SaleOrderManagementLocators.saleOrder_creat_locators import SaleOrderCreatLocators


class SaleOrderPage(BasePage):

    #进入销售订单管理界面
    def enterinterface(self):
        time.sleep(3)
        self.click_element(IndexLocator.salemanagement_tag, doc='销售管理')
        self.click_element(IndexLocator.saleordermanagement_tag, doc='销售订单管理')
        return self.get_element_text(loc.firstordercode_loc,doc='返回订单号'),self.get_element_text(loc.firstcutomname_loc,doc='返回客户名称')

        time.sleep(2)


    # 新建销售订单
    def creatsaleorder(self):
        doc = '点击新建销售订单按钮'
        self.click_element(loc.newbuilt_loc, doc)

    # 批量删除销售订单
    def deletesaleorder(self):
        self.click_element(loc.list_checkbox_loc_1, doc='选择第一个复选框')
        self.click_element(loc.batchdeletebtn_loc, doc='点击批量删除')
        self.click_element(loc.promptdelete_loc, doc='确认删除')

    # 批量作废销售订单
    def cancelconstract(self):
        time.sleep(3)
        self.click_element(loc.list_checkbox_loc_1, doc='选择第一个复选框')
        self.click_element(loc.batchcancelbtn_loc, doc='点击作废')
        self.input_element(loc.prompcancelinfotext_loc, "测试作废", doc='填写作废信息')
        self.click_element(loc.prompcancelconfirm_loc, doc='作废确认')

    # 从第一个销售订单生成发货通知
    def generatesaleship(self):
        time.sleep(3)
        self.click_element(loc.list_checkbox_loc_1, doc='选择第一个复选框')
        self.click_element(loc.shipnotice_loc, doc='点击发货通知')

    #从第一个销售订单操作编辑
    def editsaleorder(self):
        time.sleep(3)
        self.click_element(loc.operatoreditbtn_loc,doc='操作编辑')

    #从第一个销售订单操作提交
    def submitsaleorder(self):
        time.sleep(3)
        self.click_element(loc.operatorsubmitbtn_loc,doc='操作提交')
        self.click_element(loc.prompcancelconfirm_loc,doc='确认提交')

    #从第一个销售订单操作审批
    def auditsaleorder(self):
        time.sleep(2)
        self.click_element(loc.operatorauditbtn_loc,doc='操作审批')
        time.sleep(5)
        self.click_element(SaleOrderCreatLocators.submitbtn_loc,doc='详情页点击提交')

    # 从第一个销售订单操作删除
    def deletesaleorder(self):
        time.sleep(3)
        self.click_element(loc.operatordeltebtn_loc, doc='操作删除')
