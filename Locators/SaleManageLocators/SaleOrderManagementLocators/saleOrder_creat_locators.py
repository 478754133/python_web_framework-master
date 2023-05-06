from selenium.webdriver.common.by import By
class SaleOrderCreatLocators:

    '''-------基本信息---------'''
    #来源单据
    #来源单号
    #产品大类
    #收单地点
    #客户名称
    #币种
    #订单类型
    #业务类型
    #收款条件
    #交货方式
    #运输方式
    #订单月份 start:开始月份  end:结束月份
    ordermonth_stat_loc = (By.CSS_SELECTOR, "div:nth-child(12)  div > div:nth-child(1) > input")
    ordermonth_end_loc = (By.CSS_SELECTOR, ".el-date-editor:nth-child(3) > .el-input__inner")
    #订单日期
    orderdate_loc = (By.CSS_SELECTOR, "div:nth-child(13) > div > div > div > input")
    #失效日期
    faildate_loc = (By.CSS_SELECTOR, "div:nth-child(14) div.el-date-editor.el-input.el-input--mini.el-input--prefix.el-input--suffix.el-date-editor--date > input")
    #交货允差
    deliverytolerance_loc = (By.CSS_SELECTOR, "div:nth-child(15) div > input")
    #定价方式-确定价
    pricingmethod_1_loc = (By.XPATH, "//div[16]/div/div/div/label[1]/span[1]/span")
    #定价方式-后定价
    pricingmethod_2_loc = (By.XPATH, "//div[16]/div/div/div/label[2]/span[1]/span")
    #关联采购单号

    #创建人部门下拉
    createdepartment_loc = (By.XPATH, "//div[18]/div/div/span/div/div/span/span/i")
    #创建人部门->第一个
    createdepartment_1_loc = (By.XPATH, "//ul/li[1]/span[text()='铜产品销售部']")

    '''-------物料信息---------'''
    # 新增物料
    addmeterialinfo_loc = (By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(2) > div > button")
    # 产品信息->物料编码
    materialcode_loc = (By.CSS_SELECTOR,".is-scrolling-left > table > tbody > tr > td.el-table_1_column_2 div > input")
    # 产品信息->物料编码->物料选择->阴极铜
    materialcode_table_loc = (By.CSS_SELECTOR, ".el-tree-node:nth-child(1) .el-tree-node__label")
    # 产品信息->物料编码->物料编码搜索栏
    materialcodesearch_loc = (By.CSS_SELECTOR, ".el-col:nth-child(1) > .search-item .el-input__inner")
    # 产品信息->物料编码->物料编码查询按钮
    materialcodesearchbtn_loc = (By.CSS_SELECTOR, ".btn-area > .el-button--primary > span")
    # 产品信息->物料编码->物料编码被选状态圆点
    materialcodesearchselected_loc = (By.XPATH, "(//div[2]/table/tbody/tr/td/div/label/span/span)[1]")
    # 产品信息->物料编码->物料编码确定按钮
    materialcodesearchbtn_confirm_loc = (By.CSS_SELECTOR, "div.el-dialog__body > div > div:nth-child(2) > button.el-button.el-button--primary.el-button--mini > span")
    # 物料信息->数量
    quantity_loc = (By.XPATH,"//div[3]/table/tbody/tr/td[6]/div/div/div/div/input")

    '''-------作价信息---------'''

    '''------组件类按钮提示框-------'''
    #取消
    cancelbtn_loc = (By.XPATH, "//button/span[text()='取消']")
    #保存并新建
    savebuildbtn_loc = (By.XPATH, "//button/span[text()='保存并新建']")
    #提交并新建
    submitbuildbtn_loc = (By.XPATH, "//button/span[text()='提交并新建']")
    #保存
    savebtn_loc = (By.XPATH, "//button/span[text()='保存']")
    #提交
    submitbtn_loc = (By.XPATH, "(//button/span[text()='提交'])")

    #审批信息提交
    auditinfo_submit_loc = (By.XPATH, "(//button/span[text()='提交'])[2]")
    #审批信息取消
    auditinfo_cancel_loc = (By.XPATH, "(//button/span[text()='取消'])[2]")
