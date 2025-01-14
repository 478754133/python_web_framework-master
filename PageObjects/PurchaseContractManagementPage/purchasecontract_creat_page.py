from Locators.PurchaseContractionManagementLocators.purchaseContract_creat_locators import PurchaseContractCreatLocators as loc
from Common.plugs.basepage import BasePage
from Locators.IndexLocators.index_locators import IndexLocator
from Locators.PurchaseContractionManagementLocators.purchaseContractManagement_locators import PurchaseContractManagementLocators
import pytest
import time
import json
import datetime
import sys,os
from TestDatas.GobalDatas import gobal_datas as GD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Common.plugs.get_log import Log
from Common.plugs.get_config import r_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(BASE_DIR)
if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')
log_dir = r_config(conf_dir, "log", "log_path")
logger = Log(log_dir)


#新建采购合同界面对象操作方法及业务
class PurchaseConstractCreatPage(BasePage):

    now_time = str(time.strftime("%Y%m%d_%H%M%S"))

    def __init__(self,driver):
        self.driver = driver


    def addcustominfo(self):
        doc='新建客户信息'
        self.click_element(loc.addcustominfo_loc,doc)

    def addproductioninfo(self):
        doc='新增产品信息'
        self.click_element(loc.addproductioninfo_loc, doc)

    def auditapprove(self):
        doc='审批通过'
        self.click_element(loc.approvebtn_loc,doc)

    def cancel(self):
        doc='取消'
        self.click_element(loc.cancelbtn_loc,doc)

    #填写非标准合同业务可以手动维护
    def creatpurchaseconstract_1(self):
        purchasename = "测试_{0}".format(self.now_time)
        constractno = "WF{0}".format(self.now_time)
        time.sleep(3)
        self.get("http://yantaitrade.jxcc.com/contract/contract-manange/purchase-list")
        # self.click_element(IndexLocator.constractmanagement_tag,doc='合同管理')
        # self.click_element(IndexLocator.constractmanagement_purchaseconstract_tag,doc='销售合同')
        # self.click_element(IndexLocator.constractmanagement_purchaseconstract_sub1_tag,doc='销售合同管理')
        time.sleep(2)
        self.click_element(PurchaseContractManagementLocators.newbuilt_loc, doc='点击新建')
        time.sleep(2)
        self.input_element(loc.constractname_loc,purchasename,doc='填写合同名称')
        self.input_element(loc.constractyear_end_loc, "2024", doc='填写合同年份')
        self.select_listcontent(loc.businesstype_loc,loc.businesstypelist_loc,"一般国内贸易",doc='一般国内贸易')
        self.select_listcontent(loc.ordertype_loc,loc.ordertypelist_loc,"贸易成品采购",doc='订单类型')
        self.select_listcontent(loc.currency_loc,loc.currencylist_loc,"人民币元",doc="人民币")
        self.input_element(loc.constractduration_start_loc,"2023-01-01",doc='合同有效期开始时间')
        self.input_element(loc.constractduration_start_loc, Keys.ENTER, doc='合同有效期开始时间确定')
        self.input_element(loc.constractduration_end_loc, "2023-12-30", doc='合同有效期结束时间')
        self.input_element(loc.constractduration_end_loc, Keys.ENTER, doc='合同有效期结束时间确定')

        self.select_listcontent(loc.collectionterms_loc,loc.collectiontermslist_loc, "货到付款", doc='付款条件选择货到付款')

        self.select_listcontent(loc.paymentmethod_loc,loc.paymentmethodlist_loc,"支票","收款方式选择支票")

        self.select_listcontent(loc.productiontype_loc,loc.productiontypelist_loc,"国内原料",doc='产品类型选择国内原料')
        time.sleep(1)
        self.select_listcontent(loc.receivinglocation_loc,loc.receivinglocationlist_loc,"铜精矿",doc='收单地点选择铜精矿')
        time.sleep(1)

        self.select_listcontent(loc.constracttype_loc,loc.constracttypelist_loc,"零单合同",doc="合同类型选择零单合同")

        self.select_listcontent(loc.standardtype_loc, loc.standardtypelist_loc, "非标准合同", doc='标准类型选择')

        self.input_element(loc.contractnumberother_loc, constractno, doc='填写我方合同号')
        time.sleep(1)
        self.select_listcontent(loc.supply_loc,loc.supplylist_loc,"上海五锐金属集团有限公司",doc='供应商选择')
        time.sleep(1)
        self.click_element(loc.addproductioninfo_loc, doc='新增产品信息')
        self.click_element(loc.materialcode_loc,doc='物料选择')
        self.click_element(loc.materialcode_table_loc, doc='物料选择阴极铜')
        self.input_element(loc.materialcodesearch_loc,"400000077",doc='输入编码')
        self.click_element(loc.materialcodesearchbtn_loc, doc='点击查询')
        self.click_element(loc.materialcodesearchselected_loc, doc='圆点选择')
        self.click_element(loc.materialcodesearchbtn_confirm_loc, doc='选择确定')
        self.input_element(loc.quantity_loc,"100",doc='产品数量填写100')
        self.click_element(loc.uploadconstractbtn_loc,doc='合同文件点击上传')
        self.upload_file(GD.constract_path)



        # self.click_element(loc.selecttemplate_loc, doc='选择模板')
        # self.click_element(loc.selecttemplate_selected_1_loc, doc='选择被选圆点')
        # self.click_element(loc.selecttemplate_confirm_loc, doc='选择模板确定')
        #
        # self.click_element(loc.approvebtn_loc,doc='审批通过')
        #
        # self.click_element(loc.preview_loc,doc='预览合同')
        # self.click_element(loc.promptbtn_cancel_loc,doc='取消提示')

    #保存非标准合同业务(阴极铜)
    def savepurchaseconstract(self):
        self.creatpurchaseconstract_1()
        time.sleep(1)
        self.click_element(loc.savebtn_loc, doc='保存')

    #提交合同审批通过(测试用)
    def approvepurchaseconstract_1(self):
        self.creatpurchaseconstract_1()
        self.click_element(loc.approvebtn_loc,doc='审批通过')
























