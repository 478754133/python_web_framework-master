from selenium.webdriver.common.by import By
class SaleOutboundCreatLocators:

    '''-------发货行查询--------'''
    #产品大类
    #发货地
    #客户名称
    #第一个选择圆点
    radio_selected1_loc = (By.XPATH,"//div[2]/table/tbody/tr/td[1]/div/label/span[1]/span")
    '''-------新建出库单---------'''
    #新增
    newadd_loc = (By.XPATH, "(//button/span[text()='新增'])")
    #行号
    #出库数量
    outquantity_loc = (By.XPATH,"//div[3]/table/tbody/tr/td[2]/div/div/div/div/input")
    #出库日期
    outdate_loc = (By.XPATH, "//div[3]/table/tbody/tr/td[3]/div/div/div/div/input")
    #运输车号
    #提货单号
    #备案证明号
    #品牌
    #物料规格批次
    #物料级别
    #出库月份
    #库存类型
    #箱号
    #目的港-地区
    #操作




    '''------组件类按钮提示框-------'''
    #重置
    resetbtn_loc = (By.XPATH, "//button/span[text()='重置']")
    #查询
    searchbtn_loc = (By.XPATH, "//button/span[text()='查询']")
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

    # 提示信息提交
    promptinfo_confirm = (By.XPATH, "//button/span[text()=' 确定 ']")
    # 提示信息取消
    promptinfo_cancel = (By.XPATH, "//button/span[text()=' 取消 ']")


