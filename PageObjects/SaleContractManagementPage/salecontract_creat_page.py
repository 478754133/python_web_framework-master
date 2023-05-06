from Locators.SaleConstractionManagementLocators.saleConstract_creat_locators import SaleContractCreatLocators as loc
from Common.plugs.basepage import BasePage
from Locators.IndexLocators.index_locators import IndexLocator
from Locators.SaleConstractionManagementLocators.saleContractManagement_locators import SaleContractManagementLocators
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


#新建销售合同界面对象操作方法及业务
class SaleConstractCreatPage(BasePage):

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

    #填写非标准合同业务(阴极铜) 可以手动维护
    def creatsaleconstract_1(self):
        salename = "测试_{0}".format(self.now_time)
        time.sleep(5)
        self.click_element(IndexLocator.constractmanagement_tag,doc='合同管理')
        self.click_element(IndexLocator.constractmanagement_saleconstract_tag,doc='销售合同')
        self.click_element(IndexLocator.constractmanagement_saleconstract_sub1_tag,doc='销售合同管理')
        time.sleep(2)
        self.click_element(SaleContractManagementLocators.newbuilt_loc, doc='点击新建')
        time.sleep(2)
        self.input_element(loc.constractname_loc,salename,doc='填写合同名称')
        self.input_element(loc.constractyear_end_loc, "2024", doc='填写合同年份')
        self.click_element(loc.businesstype_loc,doc='下拉业务类型')
        self.click_element(loc.businesstype_1_loc,doc='一般国内贸易')
        self.click_element(loc.ordertype_loc,doc='下拉订单类型')
        self.click_element(loc.ordertype_1_loc, doc='产品销售')
        self.click_element(loc.currency_loc,doc='选择币种')
        self.click_element(loc.currency_1_loc,doc='RMB')
        self.input_element(loc.constractduration_start_loc,"2023-01-01",doc='合同有效期开始时间')
        self.input_element(loc.constractduration_start_loc, Keys.ENTER, doc='合同有效期开始时间确定')
        self.input_element(loc.constractduration_end_loc, "2023-12-30", doc='合同有效期结束时间')
        self.input_element(loc.constractduration_end_loc, Keys.ENTER, doc='合同有效期结束时间确定')
        self.click_element(loc.collectionterms_loc,doc='收款条件下拉')
        self.click_element(loc.collectionterms_1_loc,doc='货到付款')
        self.input_element(loc. collectiontermsexplain_loc,"收款条件测试",doc='填写收款说明')
        self.click_element(loc.paymentmethod_loc,doc='收款方式下拉')
        self.click_element(loc.paymentmethod_1_loc,doc='电汇')
        self.input_element(loc.contractnumberother_loc,"123456789",doc='填写对方合同号')
        self.click_element(loc.productiontype_loc,doc='产品类型选择')
        self.click_element(loc.productiontype_1_loc, doc='阴极铜')
        self.click_element(loc.constracttype_loc,doc='合同类型选择')
        self.click_element(loc.constracttype_1_loc, doc='零单合同')
        time.sleep(1)
        self.click_element(loc.standardtype_loc,doc='标准类型选择')
        self.click_element(loc.standardtype_1_loc,doc='非标准合同')

        self.click_element(loc.createdepartment_loc,doc='创建部门选择')
        self.click_element(loc.createdepartment_1_loc, doc='多金属部门')
        time.sleep(1)
        self.input_element(loc.cutomer_loc,"上海五锐金属集团有限公司",doc='客户信息选择')
        #客户信息确认
        self.driver.find_element(By.XPATH, "/html/body/div[15]/div[1]/div[1]/ul/li[2]/span").click()
        self.click_element(loc.addproductioninfo_loc, doc='新增产品信息')
        self.click_element(loc.materialcode_loc,doc='物料选择')
        self.click_element(loc.materialcode_table_loc, doc='物料选择阴极铜')
        self.input_element(loc.materialcodesearch_loc,"402003165",doc='输入编码')
        self.click_element(loc.materialcodesearchbtn_loc, doc='点击查询')
        self.click_element(loc.materialcodesearchselected_loc, doc='圆点选择')
        self.click_element(loc.materialcodesearchbtn_confirm_loc, doc='选择确定')
        self.input_element(loc.quantity_loc,"100",doc='产品数量填写100')
        self.click_element(loc.uploadconstractbtn_loc,doc='合同文件点击上传')
        self.upload_file(GD.constract_path)



        # self.click_element(loc.selecttemplate_loc, doc='选择模板')
        # self.click_element(loc.selecttemplate_selected_1_loc, doc='选择被选圆点')
        # self.click_element(loc.selecttemplate_confirm_loc, doc='选择模板确定')

        #self.click_element(loc.approvebtn_loc,doc='审批通过')

        #self.click_element(loc.preview_loc,doc='预览合同')
        # self.click_element(loc.promptbtn_cancel_loc,doc='取消提示')

    #保存非标准合同业务(阴极铜)
    def savesaleconstract_1(self):
        self.creatsaleconstract_1()
        self.click_element(loc.savebtn_loc, doc='保存')

    #提交合同审批通过(测试用)
    def approvesaleconstract_1(self):
        self.creatsaleconstract_1()
        self.click_element(loc.approvebtn_loc,doc='审批通过')
























