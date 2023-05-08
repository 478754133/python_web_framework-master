from selenium.webdriver.common.by import By
class SaleNopointSettleLocators:

    '''-------基本信息--------'''
    #客户名称
    customname_loc = (By.XPATH, "//div[2]/div/div[1]/div/div/span/div/div/input")
    #选择第一个客户
    customname_1_loc = (By.XPATH, "//ul/li[11]/span[text()='上海五锐金属集团有限公司']")
    #销售订单号
    saleordernumber_loc = (By.XPATH, "//div[2]/div/div[2]/div/div/div[1]/input")

    #销售订单选择查询:1.产品大类 2.收单地点 3.订单月份 4.销售订单号
    saleordernumberfind_1_loc = (By.CSS_SELECTOR, "input[placeholder='产品大类']")
    saleordernumberfind_2_loc = (By.CSS_SELECTOR, "input[placeholder='收单地点']")
    saleordernumberfind_3_loc = (By.CSS_SELECTOR, "input[placeholder='选择月']")
    saleordernumberfind_4_loc = (By.CSS_SELECTOR, "input[placeholder='销售订单号']")
    #搜索出的第一个选择圆点
    selectedfind_1_loc = (By.XPATH, "//div[4]/div[2]/table/tbody/tr/td[1]/div/label/span[1]/span")

    #结算日期
    settledate_loc = (By.XPATH, "//div[2]/div/div[3]/div/div/div[1]/input")
    #创建人
    creator_loc = (By.XPATH, "//div[2]/div/div[4]/div/div/div[1]/input")
    #创建部门
    creatdepartment_loc = (By.XPATH, "//div[2]/div/div[5]/div/div/span/div/div[1]/input")
    #部门选择
    creatdepartment_selected_loc = (By.XPATH, "//li/span[text()='铜产品销售部']")



    '''-------待结算出库单出库单信息---------'''
    #本次结算数量


    '''-------结算汇总---------'''



    '''------组件类按钮提示框-------'''
    # 重置
    resetbtn_loc = (By.XPATH, "//button/span[text()='重置']")
    # 查询
    searchbtn_loc = (By.XPATH, "//button/span[text()='查询']")
    # 取消
    cancelbtn_loc = (By.XPATH, "(//button/span[text()='取消'])[1]")
    # 确定
    confirmbtn_loc = (By.XPATH, "//button/span[text()='确定']")
    # 保存并新建
    savebuildbtn_loc = (By.XPATH, "//button/span[text()='保存并新建']")
    # 提交并新建
    submitbuildbtn_loc = (By.XPATH, "//button/span[text()='提交并新建']")
    # 保存
    savebtn_loc = (By.XPATH, "//button/span[text()='保存']")
    # 提交
    submitbtn_loc = (By.XPATH, "(//button/span[text()='提交'])")

    # 提示信息确认
    promptinfo_confirm = (By.XPATH, "//button/span[text()='确认']")
    # 提示信息取消
    promptinfo_cancel = (By.XPATH, "(//button/span[text()='取 消'])[3]")
