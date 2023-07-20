from selenium.webdriver.common.by import By


class PurchaseContractManagementLocators:
    #新建按钮
    newbuilt_loc = (By.CSS_SELECTOR, ".el-col > .el-button--primary > span")

    #批量删除
    batchdeletebtn_loc = (By.CSS_SELECTOR, "button[title='批量删除']")
    #提示框删除确认-确认
    promptdelete_loc = (By.XPATH,"//div[3]/div/div[3]/button[2]/span")

    #批量作废
    batchcancelbtn_loc = (By.CSS_SELECTOR, "button[title='批量作废']")
    # 提示框作废信息填写
    prompcancelinfotext_loc = (By.CSS_SELECTOR, "input[placeholder='请输入作废说明']")
    # 提示框作废确认-确认
    prompcancelconfirm_loc = (By.CSS_SELECTOR, ".el-button--small.el-button--primary > span")

    #第一个操作下拉图标
    icon_arrowdown_loc = (By.XPATH,"(//div[5]/div[2]/table/tbody/tr/td[28]/div/div/span/i)[1]")
    #创建订单
    generatesaleorder_loc = (By.XPATH,"//body/ul/li[7]")


    #合同列表选择复选框--全选
    list_checkbox_loc = (By.XPATH, "//*[@id='hcBox']/div/div[2]/div/div[4]/div/div[2]/div[4]/div[1]/table/thead/tr/th[1]/div/label/span/span")
    #合同列表选择复选框--选泽第一个
    list_checkbox_loc_1 = (By.CSS_SELECTOR, ".el-table__fixed:nth-child(4) .el-table__row:nth-child(1) .el-checkbox__inner:nth-child(1)")

    #合同编号
    constractcode_loc = (By.XPATH, "(//th/div[@class='cell' and text()='合同编号'])[1]")





