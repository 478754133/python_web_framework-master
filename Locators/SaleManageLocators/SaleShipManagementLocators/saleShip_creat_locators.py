from selenium.webdriver.common.by import By
class SaleShipCreatLocators:
    '''------基本信息------'''
    #发货类型
    #产品大类
    #销售单号
    #客户名称
    #运输方式
    transportmode_loc = (By.XPATH, "//form/div[1]/div[2]/div/div/div[5]/div/div/span/div/div/input")
    #运输方式(汽车)
    transportmode_1_loc = (By.XPATH, "//ul/li/span[text()='汽车']")
    #收货单位
    #收款条件
    #销售方式
    #交货方式
    #计划发货日期
    planshipdate_loc = (By.XPATH, "//form/div[1]/div[2]/div/div/div[10]/div/div/div/input")
    #有效期
    #出库允差
    #备注

    '''------发货信息------'''
    #发货地
    #发货仓库
    #收货地
    #收货仓库
    # #新增(从销售订单导物料)
    #物料信息
    #计划发货数量
    planshipquantity = (By.XPATH, "//div[3]/table/tbody/tr/td[5]/div/div/div/div[1]/input")
    #基价
    baseprice = (By.XPATH, "//div[3]/table/tbody/tr/td[9]/div/div/div/div[1]/input")
    #元素计价


    '''------费用信息------'''

    '''------贷款信息------'''
    #应收日期
    receivedate = (By.XPATH, "//div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/input")
    '''------组件类按钮提示框-------'''
    # 取消
    cancelbtn_loc = (By.XPATH, "//button/span[text()='取消']")
    # 保存并新建
    savebuild_loc = (By.XPATH, "//button/span[text()='保存并新建']")
    # 提交并新建
    submitbuild_loc = (By.XPATH, "//button/span[text()='提交并新建']")
    # 保存
    savebtn_loc = (By.XPATH, "//button/span[text()='保存']")
    # 提交
    submit_loc = (By.XPATH, "//button/span[text()='提交']")





